syntax on
filetype plugin indent on

set termguicolors
" Enable transparent floating windows
set winblend=70
set pumblend=70
highlight Normal guibg=#1c1c1c


" Enable line numbers
: set number

" Set tabs and indentation
: set autoindent
: set tabstop=4
: set shiftwidth=4
": set smarttab
: set softtabstop=4

" Enable mouse support
: set mouse=a

" set clipboard to use the system clipboard
set clipboard=unnamedplus

"Enable auto compltion menu
set completeopt=menuone,noinsert,noselect


call plug#begin()

Plug 'https://github.com/vim-airline/vim-airline'

" Autocompletion plugin
Plug 'neoclide/coc.nvim',{'branch':'release'}


" Syntax highlighting and language support

Plug 'sheerun/vim-polyglot'
Plug 'kyazdani42/nvim-tree.lua'
Plug 'neovim/nvim-lspconfig' " LSP configurations
Plug 'hrsh7th/nvim-cmp' " Completion framework
Plug 'hrsh7th/cmp-nvim-lsp' " LSP source for nvim-cmp
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'} " Syntax highlighting
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'
Plug 'nvim-telescope/telescope-fzf-native.nvim', { 'do': 'make' }
Plug 'nvim-lualine/lualine.nvim' " Statusline
Plug 'onsails/lspkind-nvim' " Icons for completion
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/cmp-nvim-lua'
Plug 'hrsh7th/cmp-vsnip'
Plug 'hrsh7th/vim-vsnip'
Plug 'hrsh7th/cmp-cmdline'
Plug 'L3MON4D3/LuaSnip' " For snippet support

Plug 'morhetz/gruvbox'
Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'joshdick/onedark.vim'
Plug 'arcticicestudio/nord-vim'
Plug 'folke/tokyonight.nvim'
Plug 'EdenEast/nightfox.nvim'

Plug 'kyazdani42/nvim-web-devicons'

" Add nvim-autopairs plugin
Plug 'windwp/nvim-autopairs'

call plug#end()

lua << EOF
vim.diagnostic.config({
  virtual_text = {
    prefix = '', -- You can use a different character if you prefer
  },
  signs = true,
  update_in_insert = true,
  underline = true,
})

local lspconfig = require('lspconfig')
lspconfig.clangd.setup{}
EOF



" Map Alt+m to Right Arrow Key
nnoremap <A-m> <Right>
inoremap <A-m> <Right>
vnoremap <A-m> <Right>


" Map Alt+n to Left Arrow key
nnoremap <A-n> <Left>
inoremap <A-n> <Left>
vnoremap <A-n> <Left>

" Map Alt+j to Up Arrow key
nnoremap <A-j> <Up>
inoremap <A-j> <Up>
vnoremap <A-j> <Up>

" Map Alt+k to Down Arrow key
nnoremap <A-k> <Down>
inoremap <A-k> <Down>
vnoremap <A-k> <Down>

" Map Alt+, to Home key
nnoremap <A-,> <Home>
inoremap <A-,> <Home>
vnoremap <A-,> <Home>

" Map Alt+. to End key
nnoremap <A-.> <End>
inoremap <A-.> <End>
vnoremap <A-.> <End>



" Initialize nvim-autopairs
lua << EOF
require('nvim-autopairs').setup{}
EOF

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

" Enable transparent popup menu
set pumblend=40

" Configure nvim-cmp
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
      ['<CR>'] = cmp.mapping.confirm({ select = true }),
    },
    sources = cmp.config.sources({
      { name = 'nvim_lsp' },
      { name = 'luasnip' },
    }, {
      { name = 'buffer' },
    })
  })

  -- Use buffer source for `/` (if you enabled `native_menu`, this won't work anymore).
  cmp.setup.cmdline('/', {
    sources = {
      { name = 'buffer' }
    }
  })

  -- Use cmdline & path source for ':' (if you enabled `native_menu`, this won't work anymore).
  cmp.setup.cmdline(':', {
    sources = cmp.config.sources({
      { name = 'path' }
    }, {
      { name = 'cmdline' }
    })
  })
EOF






" Python settings for coc-python
let g:coc_python_settings = {
  \ 'python.pythonPath': '/usr/bin/python3.12'
  \ }



" Use Tab for confirming completion and inserting a tab character when no suggestions are available
inoremap <silent><expr> <Tab> pumvisible() ? "\<C-y>" : "\<Tab>"
inoremap <silent><expr> <S-Tab> pumvisible() ? "\<C-e>" : "\<Tab>"

" Use Enter to insert a newline as usual
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
local nvim_lsp = require('lspconfig')
local cmp = require'cmp'
local lspkind = require('lspkind')

-- Setup nvim-cmp.
cmp.setup({
  snippet = {
    expand = function(args)
      vim.fn["vsnip#anonymous"](args.body) -- For `vsnip` users.
    end,
  },
  mapping = {
    ['<Tab>'] = cmp.mapping.select_next_item(),
    ['<S-Tab>'] = cmp.mapping.select_prev_item(),
    ['<CR>'] = cmp.mapping.confirm({ select = true }),
  },
  sources = cmp.config.sources({
    { name = 'nvim_lsp' },
    { name = 'vsnip' },
  }, {
    { name = 'buffer' },
  }),
  formatting = {
    format = lspkind.cmp_format({ with_text = true, maxwidth = 50 })
  }
})

-- Setup lspconfig.
local on_attach = function(client, bufnr)
  local function buf_set_keymap(...) vim.api.nvim_buf_set_keymap(bufnr, ...) end
  local function buf_set_option(...) vim.api.nvim_buf_set_option(bufnr, ...) end

  buf_set_option('omnifunc', 'v:lua.vim.lsp.omnifunc')

  -- Mappings.
  local opts = { noremap=true, silent=true }

  -- See `:help vim.lsp.*` for documentation on any of the below functions
  buf_set_keymap('n', 'gD', '<Cmd>lua vim.lsp.buf.declaration()<CR>', opts)
  buf_set_keymap('n', 'gd', '<Cmd>lua vim.lsp.buf.definition()<CR>', opts)
  buf_set_keymap('n', 'K', '<Cmd>lua vim.lsp.buf.hover()<CR>', opts)
  buf_set_keymap('n', 'gi', '<cmd>lua vim.lsp.buf.implementation()<CR>', opts)
  buf_set_keymap('n', '<C-k>', '<cmd>lua vim.lsp.buf.signature_help()<CR>', opts)
  buf_set_keymap('n', '<space>wa', '<cmd>lua vim.lsp.buf.add_workspace_folder()<CR>', opts)
  buf_set_keymap('n', '<space>wr', '<cmd>lua vim.lsp.buf.remove_workspace_folder()<CR>', opts)
  buf_set_keymap('n', '<space>wl', '<cmd>lua print(vim.inspect(vim.lsp.buf.list_workspace_folders()))<CR>', opts)
  buf_set_keymap('n', '<space>D', '<cmd>lua vim.lsp.buf.type_definition()<CR>', opts)
  buf_set_keymap('n', '<space>rn', '<cmd>lua vim.lsp.buf.rename()<CR>', opts)
  buf_set_keymap('n', 'gr', '<cmd>lua vim.lsp.buf.references()<CR>', opts)
  buf_set_keymap('n', '<space>e', '<cmd>lua vim.lsp.diagnostic.show_line_diagnostics()<CR>', opts)
  buf_set_keymap('n', '[d', '<cmd>lua vim.lsp.diagnostic.goto_prev()<CR>', opts)
  buf_set_keymap('n', ']d', '<cmd>lua vim.lsp.diagnostic.goto_next()<CR>', opts)
  buf_set_keymap('n', '<space>q', '<cmd>lua vim.lsp.diagnostic.set_loclist()<CR>', opts)
  buf_set_keymap('n', '<space>f', '<cmd>lua vim.lsp.buf.formatting()<CR>', opts)
end

-- Use a loop to conveniently call 'setup' on multiple servers and
-- map buffer local keybindings when the language server attaches
local servers = { 'pyright', 'tsserver', 'clangd' }
for _, lsp in ipairs(servers) do
  nvim_lsp[lsp].setup {
    on_attach = on_attach,
    flags = {
      debounce_text_changes = 150,
    }
  }
end
EOF


lua << EOF
local cmp = require'cmp'
local lspkind = require'lspkind'

cmp.setup({
  formatting = {
    format = lspkind.cmp_format({
      mode = 'symbol',
      maxwidth = 50,
      ellipsis_char = '...',
    })
  },
  mapping = {
    ['<CR>'] = cmp.mapping.confirm({ select = false }),  -- Accept currently selected item. Set `select` to `false` to only confirm explicitly selected items.
    ['<Tab>'] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_next_item()
      else
        fallback()
      end
    end, { 'i', 's' }),
    ['<S-Tab>'] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_prev_item()
      else
        fallback()
      end
    end, { 'i', 's' }),
  },
  sources = {
    { name = 'nvim_lsp' },
    { name = 'buffer' },
    { name = 'path' },
  },
})
EOF



lua << EOF
local cmp = require'cmp'
local lspkind = require'lspkind'

cmp.setup({
  formatting = {
    format = lspkind.cmp_format({
      mode = 'symbol',
      maxwidth = 50,
      ellipsis_char = '...',
    })
  },
  mapping = {
    ['<CR>'] = cmp.mapping.confirm({ select = false }),  -- Accept currently selected item. Set `select` to `false` to only confirm explicitly selected items.
    ['<Tab>'] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_next_item()
      else
        fallback()
      end
    end, { 'i', 's' }),
    ['<S-Tab>'] = cmp.mapping(function(fallback)
      if cmp.visible() then
        cmp.select_prev_item()
      else
        fallback()
      end
    end, { 'i', 's' }),
  },
  sources = {
    { name = 'nvim_lsp' },
    { name = 'buffer' },
    { name = 'path' },
  },
  window = {
    completion = {
      winhighlight = "Normal:Pmenu,FloatBorder:Pmenu,Search:None",
      col_offset = -3,
      side_padding = 0,
    },
    documentation = {
      winhighlight = "NormalFloat:Pmenu,FloatBorder:Pmenu,Search:None",
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

" Toggle between terminal and code editing window with Alt + F
nnoremap <A-f> <C-w>w
tnoremap <A-f> <C-\><C-n><C-w>w

" Save current file, open terminal in a resized horizontal split, and enter insert mode with F9
nnoremap <F9> :w<CR>:belowright 10split<CR>:terminal<CR>

" Automatically enter insert mode when entering a terminal buffer
autocmd TermOpen * startinsert

" Function to compile and run C code, showing errors or output in the same terminal
function! CompileAndRun()
  " Save the current file
  w

  " Get the current file name and path
  let l:file = expand('%')
  let l:filename = expand('%:t:r')

  " Create a command to compile and run the code
  let l:cmd = 'gcc ' . shellescape(l:file) . ' -o ' . shellescape(l:filename) . ' 2>&1 && ./' . shellescape(l:filename) . ' || echo "Compilation failed"'

  " Open a new terminal split to run the command
  execute 'belowright 10split | terminal bash -c "' . l:cmd . '"'
endfunction

" Map F5 to compile and run the current C file
nnoremap <F5> :call CompileAndRun()<CR>

" Map F6 to close the current window
nnoremap <F6> :q<CR>

