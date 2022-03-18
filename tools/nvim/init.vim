
set number
set relativenumber
set autoindent
set tabstop=44
set shiftwidth=4
set smarttab
set softtabstop=4
set mouse=a

" Pathogen load



filetype off

call pathogen#infect()
call pathogen#helptags()

filetype plugin indent on
syntax on


command -nargs=0  -bar StudioConfig :rightbelow :e $MYVIMRC "Mapping is :StudioConfig 
command -nargs=0  -bar Config :rightbelow :e $MYVIMRC "Mapping is :StudioConfig 
command -nargs=0  -bar Reload :so $MYVIMRC "Mapping is :StudioConfig 



     
source /Users/copernico/.config/nvim/config/keymaps.vim

let g:dashboard_custom_header=[ 
            \'>>----------MONSTERS ALIENS ROBOTS AND ZOMBIES----------<<',
            \'  █████████████ █████████████ ████████████ ████████████ ',
            \'  ████ ███ ████ █████   █████ █████   ████       █████  ',
            \'  ████ ███ ████ █████████████ ████████████    █████    ',
            \'  ████ ███ ████ ████████████  █████████     ████        ',
            \'  ████ ███ ████ █████   ██    ████   █████ ████████████ ',
            \'                  |   UMA Console   |                   ',
            \'                          W.W.                          ']




let g:dashboard_default_executive ='telescope'
let g:which_key_timeout = 70
colorscheme sierra




"Wiki settings



let g:vimwiki_list = [{'path': '~/marz_wiki/',
                       \ 'syntax': 'markdown', 'ext': '.md'}]


python3 import sys 
python3 sys.path.append("/usr/local/lib/python3.9/site-packages")




nnoremap <silent> <leader>      :<c-u>WhichKey '<Space>'<CR>
nnoremap <silent> <localleader> :<c-u>WhichKey  ','<CR>
