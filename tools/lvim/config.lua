--[[
lvim is the global options object

Linters should be
filled in as strings with either
a global executable or a path to
an executable
]]
-- THESE ARE EXAMPLE CONFIGS FEEL FREE TO CHANGE TO WHATEVER YOU WANT

-- general
lvim.log.level = "warn"
lvim.format_on_save = true
lvim.colorscheme = "angr"

-- keymappings [view all the defaults by pressing <leader>Lk]
lvim.leader = "space"
-- add your own keymapping
lvim.keys.normal_mode["<C-s>"] = ":w<cr>"
-- unmap a default keymapping
-- lvim.keys.normal_mode["<C-Up>"] = false
-- edit a default keymapping
-- lvim.keys.normal_mode["<C-q>"] = ":q<cr>"

-- Change Telescope navigation to use j and k for navigation and n and p for history in both input and normal mode.
-- we use protected-mode (pcall) just in case the plugin wasn't loaded yet.
-- local _, actions = pcall(require, "telescope.actions")
-- lvim.builtin.telescope.defaults.mappings = {
--   -- for input mode
--   i = {
--     ["<C-j>"] = actions.move_selection_next,
--     ["<C-k>"] = actions.move_selection_previous,
--     ["<C-n>"] = actions.cycle_history_next,
--     ["<C-p>"] = actions.cycle_history_prev,
--   },
--   -- for normal mode
--   n = {
--     ["<C-j>"] = actions.move_selection_next,
--     ["<C-k>"] = actions.move_selection_previous,
--   },
-- }

-- Use which-key to add extra bindings with the leader-key prefix
-- lvim.builtin.which_key.mappings["P"] = { "<cmd>Telescope projects<CR>", "Projects" }
-- lvim.builtin.which_key.mappings["t"] = {
--   name = "+Trouble",
--   r = { "<cmd>Trouble lsp_references<cr>", "References" },
--   f = { "<cmd>Trouble lsp_definitions<cr>", "Definitions" },
--   d = { "<cmd>Trouble lsp_document_diagnostics<cr>", "Diagnostics" },
--   q = { "<cmd>Trouble quickfix<cr>", "QuickFix" },
--   l = { "<cmd>Trouble loclist<cr>", "LocationList" },
--   w = { "<cmd>Trouble lsp_workspace_diagnostics<cr>", "Diagnostics" },
-- }

-- TODO: User Config for predefined plugins
-- After changing plugin config exit and reopen LunarVim, Run :PackerInstall :PackerCompile
lvim.builtin.dashboard.active = true
lvim.builtin.notify.active = true
lvim.builtin.terminal.active = true
lvim.builtin.nvimtree.setup.view.side = "left"
lvim.builtin.nvimtree.show_icons.git = 0

-- if you don't want all the parsers change this to a table of the ones you want
lvim.builtin.treesitter.ensure_installed = {
  "bash",
  "c",
  "javascript",
  "json",
  "lua",
  "python",
  "typescript",
  "tsx",
  "css",
  "rust",
  "java",
  "yaml",
}

lvim.builtin.treesitter.ignore_install = { "haskell" }
lvim.builtin.treesitter.highlight.enabled = true

-- generic LSP settings

-- ---@usage disable automatic installation of servers
-- lvim.lsp.automatic_servers_installation = false

-- ---@usage Select which servers should be configured manually. Requires `:LvimCacheReset` to take effect.
-- See the full default list `:lua print(vim.inspect(lvim.lsp.override))`
-- vim.list_extend(lvim.lsp.override, { "pyright" })

-- ---@usage setup a server -- see: https://www.lunarvim.org/languages/#overriding-the-default-configuration
-- local opts = {} -- check the lspconfig documentation for a list of all possible options
-- require("lvim.lsp.manager").setup("pylsp", opts)

-- -- you can set a custom on_attach function that will be used for all the language servers
-- -- See <https://github.com/neovim/nvim-lspconfig#keybindings-and-completion>
-- lvim.lsp.on_attach_callback = function(client, bufnr)
--   local function buf_set_option(...)
--     vim.api.nvim_buf_set_option(bufnr, ...)
--   end
--   --Enable completion triggered by <c-x><c-o>
--   buf_set_option("omnifunc", "v:lua.vim.lsp.omnifunc")
-- end

-- -- set a formatter, this will override the language server formatting capabilities (if it exists)
-- local formatters = require "lvim.lsp.null-ls.formatters"
-- formatters.setup {
  -- { command = "black", filetypes = { "python" } },
--   { command = "isort", filetypes = { "python" } },
--   {
--     -- each formatter accepts a list of options identical to https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md#Configuration
--     command = "prettier",
--     ---@usage arguments to pass to the formatter
--     -- these cannot contain whitespaces, options such as `--line-width 80` become either `{'--line-width', '80'}` or `{'--line-width=80'}`
--     extra_args = { "--print-with", "100" },
--     ---@usage specify which filetypes to enable. By default a providers will attach to all the filetypes it supports.
--     filetypes = { "typescript", "typescriptreact" },
--   },
-- }

-- -- set additional linters
local linters = require "lvim.lsp.null-ls.linters"
linters.setup {
  { command = "flake8", filetypes = { "python" } },
  {
    -- each linter accepts a list of options identical to https://github.com/jose-elias-alvarez/null-ls.nvim/blob/main/doc/BUILTINS.md#Configuration
    command = "shellcheck",
    -- -@usage arguments to pass to the formatter
    -- these cannot contain whitespaces, options such as `--line-width 80` become either `{'--line-width', '80'}` or `{'--line-width=80'}`
    extra_args = { "--severity", "warning" },
  },
  {
    command = "codespell",
    ---@usage specify which filetypes to enable. By default a providers will attach to all the filetypes it supports.
    filetypes = { "javascript", "python" },
  },
}

-- Additional Plugins
lvim.plugins = {
    {"folke/tokyonight.nvim"},
    {
      "folke/trouble.nvim",
      cmd = "TroubleToggle",
    },
{
  "sindrets/diffview.nvim",
  event = "BufRead",
},
{
  "tools-life/taskwiki",
  event = "BufRead",
},
{
  "f-person/git-blame.nvim",
  event = "BufRead",
  config = function()
    vim.cmd "highlight default link gitblame SpecialComment"
    vim.g.gitblame_enabled = 0
  end,
},
{
  "mattn/vim-gist",
  event = "BufRead",
  requires = "mattn/webapi-vim",
},
{
  "nvim-treesitter/playground",
  event = "BufRead",
},
{
  "tzachar/cmp-tabnine",
  run = "./install.sh",
  requires = "hrsh7th/nvim-cmp",
  event = "InsertEnter",
},
{
  "rmagatti/goto-preview",
  config = function()
  require('goto-preview').setup {
        width = 120; -- Width of the floating window
        height = 25; -- Height of the floating window
        default_mappings = false; -- Bind default mappings
        debug = false; -- Print debug information
        opacity = nil; -- 0-100 opacity level of the floating window where 100 is fully transparent.
        post_open_hook = nil -- A function taking two arguments, a buffer and a window to be ran as a hook.
        -- You can use "default_mappings = true" setup option
        -- Or explicitly set keybindings
        -- vim.cmd("nnoremap gpd <cmd>lua require('goto-preview').goto_preview_definition()<CR>")
        -- vim.cmd("nnoremap gpi <cmd>lua require('goto-preview').goto_preview_implementation()<CR>")
        -- vim.cmd("nnoremap gP <cmd>lua require('goto-preview').close_all_win()<CR>")
    }
  end
},
{
  "ahmedkhalf/lsp-rooter.nvim",
  event = "BufRead",
  config = function()
    require("lsp-rooter").setup()
  end,
},
{
  "metakirby5/codi.vim",
  cmd = "Codi",
},
{
  "szw/vim-maximizer",
},
{
  "preservim/vim-pencil",
},
{
  "vimwiki/vimwiki",
},

{
  "lukas-reineke/indent-blankline.nvim",
  event = "BufRead",
  setup = function()
    vim.g.indentLine_enabled = 1
    vim.g.indent_blankline_char = "▏"
    vim.g.indent_blankline_filetype_exclude = {"help", "terminal", "dashboard"}
    vim.g.indent_blankline_buftype_exclude = {"terminal"}
    vim.g.indent_blankline_show_trailing_blankline_indent = false
    vim.g.indent_blankline_show_first_indent_level = false
  end
},
{
  "karb94/neoscroll.nvim",
  event = "WinScrolled",
  config = function()
  require('neoscroll').setup({
        -- All these keys will be mapped to their corresponding default scrolling animation
        mappings = {'<C-u>', '<C-d>', '<C-b>', '<C-f>',
        '<C-y>', '<C-e>', 'zt', 'zz', 'zb'},
        hide_cursor = true,          -- Hide cursor while scrolling
        stop_eof = true,             -- Stop at <EOF> when scrolling downwards
        use_local_scrolloff = false, -- Use the local scope of scrolloff instead of the global scope
        respect_scrolloff = false,   -- Stop scrolling when the cursor reaches the scrolloff margin of the file
        cursor_scrolls_alone = true, -- The cursor will keep on scrolling even if the window cannot scroll further
        easing_function = nil,        -- Default easing function
        pre_hook = nil,              -- Function to run before the scrolling animation starts
        post_hook = nil,              -- Function to run after the scrolling animation ends
        })
  end
},
	{
		"ethanholz/nvim-lastplace",
		event = "BufRead",
		config = function()
			require("nvim-lastplace").setup({
				lastplace_ignore_buftype = { "quickfix", "nofile", "help" },
				lastplace_ignore_filetype = {
					"gitcommit", "gitrebase", "svn", "hgcommit",
				},
				lastplace_open_folds = true,
			})
		end,
	},
  {
  "folke/todo-comments.nvim",
  event = "BufRead",
  config = function()
    require("todo-comments").setup()
  end,
},
{
  "itchyny/vim-cursorword",
    event = {"BufEnter", "BufNewFile"},
    config = function()
      vim.api.nvim_command("augroup user_plugin_cursorword")
      vim.api.nvim_command("autocmd!")
      vim.api.nvim_command("autocmd FileType NvimTree,lspsagafinder,dashboard,vista let b:cursorword = 0")
      vim.api.nvim_command("autocmd WinEnter * if &diff || &pvw | let b:cursorword = 0 | endif")
      vim.api.nvim_command("autocmd InsertEnter * let b:cursorword = 0")
      vim.api.nvim_command("autocmd InsertLeave * let b:cursorword = 1")
      vim.api.nvim_command("augroup END")
      end
},
{
  "tpope/vim-surround",
},
{
  "wakatime/vim-wakatime"
},
{
  "iamcco/markdown-preview.nvim",
  run = "cd app && npm install",
  ft = "markdown",
  config = function()
    vim.g.mkdp_auto_start = 1
  end,
},
{
  "ggandor/lightspeed.nvim"
},
{
  "ayu-theme/ayu-vim"
},
{
  "tpope/vim-fugitive"
},
{
  "sagarrakshe/toggle-bool"
},
{
  "laurentgoudet/vim-howdoi"
},
{
  "felipec/vim-sanegx",
  event = "BufRead",
},
{
  "nacro90/numb.nvim"
},
{
  "rafi/awesome-vim-colorschemes"
},
{
  "kevinhwang91/nvim-bqf",
  event = { "BufRead", "BufNew" },
  config = function()
  require("bqf").setup({
          auto_enable = true,
          preview = {
          win_height = 12,
          win_vheight = 12,
          delay_syntax = 80,
          border_chars = { "┃", "┃", "━", "━", "┏", "┓", "┗", "┛", "█" },
          },
          func_map = {
          vsplit = "",
          ptogglemode = "z,",
          stoggleup = "",
          },
          filter = {
          fzf = {
          action_for = { ["ctrl-s"] = "split" },
          extra_opts = { "--bind", "ctrl-o:toggle-all", "--prompt", "> " },
          },
          },
          })
  end,
},
{
  "ruifm/gitlinker.nvim",
  event = "BufRead",
  config = function()
  require("gitlinker").setup {
        opts = {
          -- remote = 'github', -- force the use of a specific remote
            -- adds current line nr in the url for normal mode
            add_current_line_on_normal_mode = true,
          -- callback for what to do with the url
            action_callback = require("gitlinker.actions").open_in_browser,
          -- print the url after performing the action
            print_url = false,
          -- mapping to call url generation
            mappings = "<leader>gy",
        },
      }
  end,
  requires = "nvim-lua/plenary.nvim",
},
{
  "pwntester/octo.nvim",
  event = "BufRead",
},
}


vim.cmd(' set relativenumber')

vim.cmd('let g:UltiSnipsExpandTrigger="<tab>"') 
vim.cmd('let g:UltiSnipsListSnippets="<c-l>"')
-- init.lua

-- require `new_config.lua` from the nvim/lua folder:

-- vim.cmd('source /Users/copernico/.config/nvim/config/keymaps.vim')
-- Autocommands (https://neovim.io/doc/user/autocmd.html)
-- lvim.autocommands.custom_groups = {
--   { "BufWinEnter", "*.lua", "setlocal ts=8 sw=8" },
-- }




lvim.builtin.dashboard.custom_header={
'>>----------MONSTERS ALIENS ROBOTS AND ZOMBIES----------<<',
 '  █████████████ █████████████ ████████████ ████████████ ',
 '  ████ ███ ████ █████   █████ █████   ████	   █████  ',
 '  ████ ███ ████ █████████████ ████████████    █████    ',
 '  ████ ███ ████ ████████████  █████████     ████        ',
 '  ████ ███ ████ █████   ██    ████   █████ ████████████ ',
 '                  |   UMA Console   |                   ',
 '                          W.W.                          '}




vim.cmd(' let g:which_key_timeout = 70')
require('numb').setup() 


lvim.builtin.dashboard.custom_section= {
      a = {
        description = { "  My Open Issues          " },
        command = "!issues",
      },
      b = {
        description = { "  My Task                 "},
        command = "!task",
      },
      c = {
        description = { "  Recent Projects         " },
        command = "Telescope projects",
      },
      d = {
        description = { "  Recently Used Files     " },
        command = "Telescope oldfiles",
      },
      e = {
        description = { "  Create Issue            " },
        command = "Telescope live_grep",
      },
      f = {
        description = { "  Review PR's             " },
        command = "Telescope live_grep",
      },

      g = {
        description = { "   Wiki                   " },
        command = "VimwikiIndex",
      },
      }


require("luasnip.loaders.from_vscode").load({ paths = { ".config/lvim/snippets" } })

vim.g.texwidth = 80
vim.cmd('let g:UltiSnipsSnippetDirectories=[" /Users/copernico/.config/lvim/snippets",]')


-- source a vimscript file
vim.cmd('source ~/.config/nvim/config/keymaps.vim')

vim.cmd('source ~/.config/nvim/config/general.vim')
