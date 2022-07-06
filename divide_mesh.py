import maya.cmds as mc
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma

def get_skinned_faces_per_joint(mesh, as_selection=False):
    """
    Generate a dictionary with faces per joint for a skinned mesh.
    The faces will the assigned to the joint with the highest weight
    Args:
        mesh (str): skinned mesh
        as_selection (bool): get the output values in form of selectable list

    Returns:
        dict
    """
    vert_cnt = mc.polyEvaluate(mesh, v=True)

    skin_cluster = mc.ls(mc.listHistory(mesh), type='skinCluster')

    faces_per_joint = {}

    if skin_cluster:

        skin_cluster = skin_cluster[0]

        sel = om.MSelectionList()
        sel.add(mesh)
        sel.add(skin_cluster)

        dag_path = sel.getDagPath(0)
        it_poly = om.MItMeshPolygon(dag_path)
        verts_per_face = []
        while not it_poly.isDone():
            verts_per_face.append(it_poly.getVertices())
            it_poly = it_poly.next()

        dag_path.extendToShape()
        sc_node = sel.getDependNode(1)

        fn_skin_cluster = oma.MFnSkinCluster(sc_node)

        influences = fn_skin_cluster.influenceObjects()
        joints = [infl.partialPathName() for infl in influences]

        infl_ids = om.MIntArray(range(len(joints)))

        weights_per_vert = []
        for vert_idx in range(vert_cnt):
            # vert_idx=0
            fn_comp = om.MFnSingleIndexedComponent()
            components = fn_comp.create(om.MFn.kMeshVertComponent)
            fn_comp.addElement(vert_idx)
            # this will give us the weights for all the joints for each vertex
            # the order of joints is determined by the list of indices in the influences
            weights = fn_skin_cluster.getWeights(dag_path, components, infl_ids)
            weight_data = {}
            for jnt, value in zip(joints, weights):
                if value:
                    weight_data[jnt] = value
            weights_per_vert.append(weight_data)

        default_dict = dict.fromkeys(joints, 0)
        for face_idx, verts in enumerate(verts_per_face):
            weights_per_face = dict(default_dict)
            for vert in verts:
                weights_data = weights_per_vert[vert]
                for joint, value in weights_data.items():
                    weights_per_face[joint] += value

            # get the maximum value
            max_value = 0
            max_joint = None
            for joint, value in weights_per_face.items():
                if value > max_value:
                    max_value = value
                    max_joint = joint

            faces = faces_per_joint.setdefault(max_joint, [])
            faces.append(face_idx)

        if as_selection:
            tmp_dict = {}
            for joint, face_ids in faces_per_joint.items():
                if not face_ids:
                    continue

                fn_comp = om.MFnSingleIndexedComponent()
                components = fn_comp.create(om.MFn.kMeshPolygonComponent)
                fn_comp.addElements(face_ids)

                new_sel = om.MSelectionList()
                new_sel.add((dag_path, components))
                tmp_dict[joint] = new_sel.getSelectionStrings()

            faces_per_joint = tmp_dict

    return faces_per_joint


def auto_split_skinned_mesh(mesh):
    """
    Split a skinned mesh based on its skincluster weights
    Args:
        mesh (str):

    Returns:
        dict: mesh piece per joint
    """
    faces_per_joint = get_skinned_faces_per_joint(mesh, as_selection=False)

    mesh_per_joint = {}

    all_faces_set = set(range(mc.polyEvaluate(mesh, f=True)))
    for joint, face_ids in faces_per_joint.items():
        if not face_ids:
            continue

        face_ids_to_delete = all_faces_set - set(face_ids)

        mesh_piece_name = '{}_{}'.format(mesh.split('|')[-1], joint.split('|')[-1])
        mesh_dup = mc.ls(mc.duplicate(mesh), l=True)[0]
        path_els = mesh_dup.split('|')
        if len(path_els) > 2:
            mesh_dup = mc.parent(mesh_dup, w=True)[0]

        mesh_dup = mc.rename(mesh_dup, mesh_piece_name)

        tmp_sel = om.MSelectionList()
        tmp_sel.add(mesh_dup)
        tmp_dag_path = tmp_sel.getDagPath(0)

        fn_comp = om.MFnSingleIndexedComponent()
        components = fn_comp.create(om.MFn.kMeshPolygonComponent)
        fn_comp.addElements(face_ids_to_delete)

        new_sel = om.MSelectionList()
        new_sel.add((tmp_dag_path, components))
        to_delete = new_sel.getSelectionStrings()
        mc.delete(to_delete)

        mesh_per_joint[joint] = mesh_dup

    return mesh_per_joint

split_data = auto_split_skinned_mesh('<skinned mesh>')
