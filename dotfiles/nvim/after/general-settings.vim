
"set somewhere else
" syntax enable                           " Enables syntax highlighing
" set splitbelow                          " Horizontal splits will automatically be below
" set splitright                          " Vertical splits will automatically be to the right
" set background=dark                     " tell vim what the background color looks like
" set clipboard=unnamedplus               " Copy paste between vim and everything else

" DEFAULTS
set hidden                              " Required to keep multiple buffers open multiple buffers

set nowrap                              " Display long lines as just one line
set fileformats=unix,dos,mac
set encoding=utf-8                      " The encoding displayed 
set fileencoding=utf-8                  " The encoding written to file
set fileencodings=utf-8

"tab & indenting
set tabstop=2                           " Insert 2 spaces for a tab
set shiftwidth=2                        " Change the number of space characters inserted for indentation
set smarttab                            " Makes tabbing smarter will realize you have 2 vs 4
set expandtab                           " Converts tabs to spaces
set smartindent                         " Makes indenting smart
set autoindent                          " Good auto indent
set showtabline=2                       " Always show tabs 

set iskeyword+=-                      	" treat dash separated words as a word text object"
set mouse=a                             " Enable your mouse
set t_Co=256                            " Support 256 colors
set conceallevel=0                      " So that I can see `` in markdown files
set laststatus=0                        " Always display the status line
set nobackup                            " This is recommended by coc
set nowritebackup                       " This is recommended by coc
set updatetime=300                      " Faster completion


set timeout " Set a timeout for MAPPINGS
set ttimeout " Set a timeout for KEYCODES

" Was problematic at 100, 200 is also kind of short...
set timeoutlen=300   " FOR MAPPINGS
" set timeoutlen=200   " FOR MAPPINGS
set ttimeoutlen=50   " FOR KEYCODES


set formatoptions-=cro                  " Stop newline continution of comments
"set autochdir                           " Your working directory will always be the same as your working directory

set termguicolors " True colors?


" Keeping undo's between sessions
set undofile
" Default undo dir: ~/.config/nvim/undo (you have to create it)
augroup vimrc
  autocmd!
  " For privacy reasons, don't keep a history of temp files
  autocmd BufWritePre /tmp/* setlocal noundofile
augroup END


" Searching defaults
set hlsearch
set incsearch
set ignorecase
set smartcase

if exists('$SHELL')
    set shell=$SHELL
else
    set shell=/bin/sh
endif


" COPY/PASTING
"" Copy/Paste/Cut with the system clipboard!
set clipboard^=unnamed,unnamedplus
noremap YY "+y<CR>
noremap XX "+x<CR>
"noremap <leader>p "+gP<CR>


" Making the terminal cursor easier to see
if has('nvim')
  highlight! link TermCursor Cursor
  highlight! TermCursorNC guibg=red guifg=white ctermbg=1 ctermfg=15
endif

" Don't start nested nvim instances!
if has('nvim') && executable('nvr')
  let $VISUAL="nvr -cc split --remote-wait +'set bufhidden=wipe'"
  " let $VISUAL="nvr -cc tabedit --remote-wait +'set bufhidden=wipe'"
  "# export VISUAL="nvim -cc tabedit --remote-wait +'set bufhidden=wipe'"
  " let $EDITOR="$VISUAL"
  "
  " " Not working...
  " let $PS1="[nvr]" + $PS1

endif

" -----------------------------------
" NETRW
" -----------------------------------

" netrw problems closing buffer
" https://vi.stackexchange.com/questions/14622/how-can-i-close-the-netrw-buffer
autocmd FileType netrw setl bufhidden=wipe
let g:netrw_fastbrowse = 0

" netrw style
" list style
" let g:netrw_liststyle = 3
" Show banner?
let g:netrw_banner = 0
" How to open files by default
" let g:netrw_browse_split = 1

" How wide should the directory explorer be
" let g:netrw_winsize = 25 " [%]


