" Enable syntax highlighting
syntax on

" Enable filetype detection and plugins
filetype plugin indent on

" Set termguicolors for better colors
set termguicolors

" Enable transparent floating windows
set winblend=70
set pumblend=70

" Highlight Normal with a background color
highlight Normal guibg=#1c1c1c

" Enable line numbers
set number

" Set tabs and indentation
set autoindent
set tabstop=4
set shiftwidth=4
set softtabstop=4

" Enable mouse support
set mouse=a

" Use system clipboard
set clipboard=unnamedplus

" Enable auto completion menu
set completeopt=menuone,noinsert,noselect

call plug#begin()

Plug 'vim-airline/vim-airline'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'sheerun/vim-polyglot'
Plug 'kyazdani42/nvim-tree.lua'
Plug 'neovim/nvim-lspconfig'
Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'
Plug 'nvim-telescope/telescope-fzf-native.nvim', { 'do': 'make' }
Plug 'nvim-lualine/lualine.nvim'
Plug 'onsails/lspkind-nvim'
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/cmp-nvim-lua'
Plug 'hrsh7th/cmp-vsnip'
Plug 'hrsh7th/vim-vsnip'
Plug 'hrsh7th/cmp-cmdline'
Plug 'L3MON4D3/LuaSnip'
Plug 'morhetz/gruvbox'
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'joshdick/onedark.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'folke/tokyonight.nvim'
Plug 'EdenEast/nightfox.nvim'
Plug 'kyazdani42/nvim-web-devicons'
Plug 'windwp/nvim-autopairs'

" Floating terminal
Plug 'voldikss/vim-floaterm'

call plug#end()

" Save the file and open a terminal in a horizontal split
nnoremap <leader>t :w<CR>:botright split<CR>:resize 10<CR>:term<CR>

" Switch back to the previous window from terminal
tnoremap <C-w> <C-\><C-n><C-w>p

" Map Alt+m to Right Arrow Key
nnoremap <A-m> <Right>
inoremap <A-m> <Right>
vnoremap <A-m> <Right>

" Map Alt+n to Left Arrow Key
nnoremap <A-n> <Left>
inoremap <A-n> <Left>
vnoremap <A-n> <Left>

" Map Alt+j to Up Arrow Key
nnoremap <A-j> <Up>
inoremap <A-j> <Up>
vnoremap <A-j> <Up>

" Map Alt+k to Down Arrow Key
nnoremap <A-k> <Down>
inoremap <A-k> <Down>
vnoremap <A-k> <Down>

" Map Alt+, to Home Key
nnoremap <A-,> <Home>
inoremap <A-,> <Home>
vnoremap <A-,> <Home>

" Map Alt+. to End Key
nnoremap <A-.> <End>
inoremap <A-.> <End>
vnoremap <A-.> <End>

" Comment selected lines with #
vnoremap <leader>c :s/^/#/<CR>

" Uncomment selected lines with #
vnoremap <leader>u :s/^#//<CR>

" Initialize nvim-autopairs
lua << EOF
require('nvim-autopairs').setup{}
EOF

" Set background and colorscheme
set background=dark
colorscheme gruvbox

" CoC (Conquer of Completion) configuration
let g:coc_global_extensions = [
  \ 'coc-python',
  \ 'coc-clangd',
  \ 'coc-sh',
  \ 'coc-snippets',
  \ 'coc-json',
  \ 'coc-html',
  \ 'coc-css',
  \ 'coc-tsserver'
  \]

" Use Tab for confirming completion and inserting a tab character when no suggestions are available
inoremap <silent><expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <silent><expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

" Ensure Enter only inserts a newline
inoremap <silent><expr> <CR> "\<CR>"

" Trigger completion with <C-Space>
inoremap <silent><expr> <C-Space> coc#refresh()

" Use Up and Down to navigate the completion menu
inoremap <silent><expr> <Up> pumvisible() ? "\<C-p>" : "\<Up>"
inoremap <silent><expr> <Down> pumvisible() ? "\<C-n>" : "\<Down>"

" Use [c and ]c to navigate diagnostics
nmap <silent> [c <Plug>(coc-diagnostic-prev)
nmap <silent> ]c <Plug>(coc-diagnostic-next)

lua << EOF
local cmp = require'cmp'

cmp.setup({
  snippet = {
    expand = function(args)
      require('luasnip').lsp_expand(args.body)
    end,
  },
  mapping = {
    ['<C-b>'] = cmp.mapping(cmp.mapping.scroll_docs(-4), { 'i', 'c' }),
    ['<C-f>'] = cmp.mapping(cmp.mapping.scroll_docs(4), { 'i', 'c' }),
    ['<C-Space>'] = cmp.mapping(cmp.mapping.complete(), { 'i', 'c' }),
    ['<C-y>'] = cmp.config.disable,
    ['<C-e>'] = cmp.mapping({
      i = cmp.mapping.abort(),
      c = cmp.mapping.close(),
    }),
    ['<CR>'] = cmp.config.disable,
  },
  sources = cmp.config.sources({
    { name = 'nvim_lsp' },
    { name = 'luasnip' },
  }, {
    { name = 'buffer' },
  }),
  formatting = {
    format = require('lspkind').cmp_format({ with_text = false, maxwidth = 50 })
  },
  window = {
    completion = {
      winhighlight = "Normal:Pmenu,FloatBorder:Pmenu",
      col_offset = -3,
      side_padding = 0,
    },
    documentation = {
      winhighlight = "NormalFloat:Pmenu,FloatBorder:Pmenu",
    },
  },
  experimental = {
    ghost_text = true,
  },
})

-- Set the transparency
vim.o.pumblend = 10  -- Set the transparency for the popup menu (0 to 100, where 100 is fully transparent)
vim.cmd [[highlight Pmenu ctermbg=NONE guibg=NONE]]
EOF

" Python settings for coc-python
let g:coc_python_settings = {
  \ 'python.pythonPath': '/usr/bin/python3.12'
  \ }

