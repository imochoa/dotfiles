


" -----------------------------------
" Plugins!
" -----------------------------------

packadd minpac
call minpac#init()

" Optional packages have to be loaded explicitly with `packadd`.

" In case minpac has any updates
call minpac#add('k-takata/minpac', {'type': 'opt'})

" Lots of shortcuts, see :help unimpaired
call minpac#add('tpope/vim-unimpaired')

" Better comments
call minpac#add('tpope/vim-commentary')

" Makes navigating around projects easier
call minpac#add('tpope/vim-projectionist')

" Running a build and navigating failures
call minpac#add('tpope/vim-dispatch')
call minpac#add('radenling/vim-dispatch-neovim') " Adapter for vim-dispatch

" Asynchronous linting engine
" call minpac#add('w0rp/ale')


" For debugging
call minpac#add('sakhnik/nvim-gdb', { 'do': ':!./install.sh \| UpdateRemotePlugins' })

" Adds the 'line' text object 'l' (like 'w')
call minpac#add('kana/vim-textobj-user')
call minpac#add('kana/vim-textobj-line')

" ?
call minpac#add('tpope/vim-scriptease', {'type': 'opt'})


" netrw extensions
call minpac#add('tpope/vim-vinegar')

" managing sessions
call minpac#add('tpope/vim-obsession', {'type': 'opt'})

" File finding using fzf (install it separately with apt)
call minpac#add('junegunn/fzf')
call minpac#add('junegunn/fzf.vim')
" Displate

"COC
call minpac#add('neoclide/coc.nvim', {'branch':'release'})
" Plug 'neoclide/coc.nvim', {'do': { -> coc#util#install()}}
" Plug 'neoclide/coc-snippets', {'do': 'yarn install --frozen-lockfile'}
" Plug 'neoclide/coc-tsserver', {'do': 'yarn install --frozen-lockfile'}
" Plug 'neoclide/coc-prettier', {'do': 'yarn install --frozen-lockfile'}
" Plug 'neoclide/coc-eslint', {'do': 'yarn install --frozen-lockfile'}
" Plug 'neoclide/coc-tslint', {'do': 'yarn install --frozen-lockfile'}
" Plug 'neoclide/coc-css', {'do': 'yarn install --frozen-lockfile'}
" Plug 'neoclide/coc-lists', {'do': 'yarn install --frozen-lockfile'} " mru and stuff
" Plug 'neoclide/coc-highlight', {'do': 'yarn install --frozen-lockfile'} " color highlighting
" requires nodejs:
" curl -sL install-node.now.sh/lts | sudo bash
" Visuals.....

" Rainbow parentheses
call minpac#add('junegunn/rainbow_parentheses.vim')

" See colors on color codes!
call minpac#add('norcalli/nvim-colorizer.lua')

" Icons on things (netrw not yet supported but there's an issue for it!)
call minpac#add('ryanoasis/vim-devicons')

" Themes should be OPTIONAL. 
" They have to be explicitly loaded with 'packadd!' in the theme section!
call minpac#add('joshdick/onedark.vim', {'type': 'opt'})

" lightline + themes
call minpac#add('itchyny/lightline.vim', {'type': 'opt'})
call minpac#add('mengelbrecht/lightline-bufferline', {'type': 'opt'})

" Add other plugins here.
" call minpac#add('vim-jp/syntax-vim-ex')

" Load the plugins right now. (optional)
"packloadall

" Install with
" :call minpac#update()
"
" See messages with :messages
" Uninstall with
" :call minpac#clean()

" command! PackUpdate call minpac#update()
command! PackUpdate call minpac#update() 
command! PackDocs silent helptags ALL
command! PackClean call minpac#clean()

" function! PackList(...)
"   call PackInit()
"   return join(sort(keys(minpac#getpluglist())), "\n")
" endfunction

command! PackList :echo join(split(join(sort(keys(minpac#getpluglist())), "\n"), ','),"\n")
" nnoremap  <leader>rt :echo join(split(&runtimepath, ','),"\n") <CR>

" -----------------------------------
" Plugin config
" -----------------------------------

" set leader key
let g:mapleader=','


" ---------
" fzf.vim 
" ---------
" 

" " Search with icons!
" function! Fzf_dev()
"   function! s:files()
"     let files = split(system($FZF_DEFAULT_COMMAND), '\n')
"     return s:prepend_icon(files)
"   endfunction

"   function! s:prepend_icon(candidates)
"     let result = []
"     for candidate in a:candidates
"       let filename = fnamemodify(candidate, ':p:t')
"       let icon = WebDevIconsGetFileTypeSymbol(filename, isdirectory(filename))
"       call add(result, printf("%s %s", icon, candidate))
"     endfor

"     return result
"   endfunction

"   function! s:edit_file(item)
"     let parts = split(a:item, ' ')
"     let file_path = get(parts, 1, '')
"     execute 'silent e' file_path
"   endfunction

"   call fzf#run({
"         \ 'source': <sid>files(),
"         \ 'sink':   function('s:edit_file'),
"         \ 'options': '-m -x +s',
"         \ 'down':    '40%' })
" endfunction


" command! FilesWithIcon :call Fzf_dev()


" export FZF_DEFAULT_COMMAND='rg --files' # smarter about ignoring some files
" making it faster
set wildmode=list:longest,list:full
set wildignore+=*.o,*.obj,.git,*.rbc,*.pyc,__pycache__
let $FZF_DEFAULT_COMMAND =  "find * -path '*/\.*' -prune -o -path 'node_modules/**' -prune -o -path 'target/**' -prune -o -path 'dist/**' -prune -o  -type f -print -o -type l -print 2> /dev/null"


" The Silver Searcher
if executable('ag')
  let $FZF_DEFAULT_COMMAND = 'ag --hidden --ignore .git -g ""'
  set grepprg=ag\ --nogroup\ --nocolor
endif

" ripgrep
if executable('rg')
  let $FZF_DEFAULT_COMMAND = 'rg --files --hidden --follow --glob "!.git/*"'
  set grepprg=rg\ --vimgrep
  command! -bang -nargs=* Find call fzf#vim#grep('rg --column --line-number --no-heading --fixed-strings --ignore-case --hidden --follow --glob "!.git/*" --color "always" '.shellescape(<q-args>).'| tr -d "\017"', 1, <bang>0)
endif

nnoremap <C-p> :<C-u>FZF<CR>
" cnoremap <C-P> <C-R>=expand("%:p:h") . "/" <CR>
nnoremap <silent> <leader>b :Buffers<CR>
nnoremap <silent> <leader>e :FZF -m<CR>
"Recovery commands from history through FZF
nmap <leader>y :History:<CR>

" ---------
" Projectionist
" ---------
" You need to make a .projections JSON file. Go back to this in the future...
" Tips 8 & 9

" ---------
" ALE
" ---------


" For JavaScript files, use `eslint` (and only eslint)
" linters.vim
" let g:ale_linters = {
" \   'javascript': ['eslint'],
" \ }

" traversal.vim
" Mappings in the style of unimpaired-next
" nmap <silent> [W <Plug>(ale_first)
" nmap <silent> [w <Plug>(ale_previous)
" nmap <silent> ]w <Plug>(ale_next)
" nmap <silent> ]W <Plug>(ale_last)
" toggle.vim
" Mappings inspired by unimpaired-toggling
" nnoremap [oa :ALEEnable<CR>
" nnoremap ]oa :ALEDisable<CR>
" nnoremap =oa :ALEToggle<CR>

" manual.vim
" nnoremap <Leader>l :ALELint<CR>
" let g:ale_lint_on_text_changed = 'never'
" let g:ale_lint_on_save = 0
" let g:ale_lint_on_enter = 0
" let g:ale_lint_on_filetype_changed = 0

" " automatic.vim
" let g:ale_lint_on_text_changed = 'always' " default
" let g:ale_lint_on_save = 1                " default
" let g:ale_lint_on_enter = 1               " default
" let g:ale_lint_on_filetype_changed = 1    " default
" let g:ale_sign_column_always = 1

" ---------
" nvim-gdb
" ---------
" To disable the plugin
" let g:loaded_nvimgdb = 1

" For more info:
" https://github.com/sakhnik/nvim-gdb

" ---------------------------
" MAPPING STUFF
" ---------------------------


" Leader commands?



"" Close buffer
" noremap <leader>c :bd<CR>
nnoremap <Leader>d :bp\|bd #<CR>
nnoremap <Leader>D :bp\|bd! #<CR>
noremap <Leader>q :q<CR>
noremap <Leader>Q :q!<CR>

" "" Git
" noremap <Leader>ga :Gwrite<CR>
" noremap <Leader>gc :Gcommit<CR>
" noremap <Leader>gsh :Gpush<CR>
" noremap <Leader>gll :Gpull<CR>
" noremap <Leader>gs :Gstatus<CR>
" noremap <Leader>gb :Gblame<CR>
" noremap <Leader>gd :Gvdiff<CR>
" noremap <Leader>gr :Gremove<CR>

" " session management
" nnoremap <leader>so :OpenSession<Space>
" nnoremap <leader>ss :SaveSession<Space>
" nnoremap <leader>sd :DeleteSession<CR>
" nnoremap <leader>sc :CloseSession<CR>

"" Set working directory
nnoremap <leader>. :lcd %:p:h<CR>

"" Opens an edit command with the path of the currently edited file filled in
noremap <Leader>e :e <C-R>=expand("%:p:h") . "/" <CR>

"" Opens a tab edit command with the path of the currently edited file filled
noremap <Leader>te :tabe <C-R>=expand("%:p:h") . "/" <CR>


" ---------
" COC
" ---------
function! SetupCommandAbbrs(from, to)
  exec 'cnoreabbrev <expr> '.a:from
        \ .' ((getcmdtype() ==# ":" && getcmdline() ==# "'.a:from.'")'
        \ .'? ("'.a:to.'") : ("'.a:from.'"))'
endfunction

" Use C to open coc config
call SetupCommandAbbrs('C', 'CocConfig')

source $HOME/.config/nvim/after/plugin/coc.vim
" source $HOME/.config/nvim/coc_config.vim 

" nvim-editcommand 
" -----------------
" " Editing terminal-mode commands in buffer using <C-x><C-e>
" call minpac#add('brettanomyces/nvim-editcommand')
" let g:editcommand_prompt = '>'   
" The default mapping is <c-x><c-e>, to change it:
" let g:editcommand_no_mappings = 1    " default is 0
" tmap <C-x> <Plug>EditCommand         " default is <c-x><c-e>

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


" -----------------------------------
" Autocommands
" -----------------------------------
au! BufWritePost $MYVIMRC ++nested source % " auto source when writing to init.vm alternatively you can run :source $MYVIMRC
" ++nested required for bufferline
" " Stops highlighting after saving!
" https://github.com/itchyny/lightline.vim/issues/406


" JSON
autocmd FileType json syntax match Comment +\/\/.\+$+

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
set ttimeoutlen=50   " FOR KEYCODES


set formatoptions-=cro                  " Stop newline continution of comments
"set autochdir                           " Your working directory will always be the same as your working directory

set termguicolors " True colors?

" -----------------------------------
" Mappings
" -----------------------------------

" See the runtimepath
nnoremap  <leader>rt :echo join(split(&runtimepath, ','),"\n") <CR>

" Expand %% to the directory of the current file
cabbr <expr> %% expand('%:p:h')

" Better nav for omnicomplete
inoremap <expr> <c-j> ("\<C-n>")
inoremap <expr> <c-k> ("\<C-p>")

" <TAB>: completion.
inoremap <expr><TAB> pumvisible() ? "\<C-n>" : "\<TAB>"


" Don't use selection when indenting
vnoremap > >gv
vnoremap < <gv

"" Move visual block
vnoremap J :m '>+1<CR>gv=gv
vnoremap K :m '<-2<CR>gv=gv


" New buffer
" BAD
" nmap <silent> bb :enew<CR>
" command Bd bp\|bd \#


" Better window navigation
" splits
nmap <silent> vv :vsplit<CR>
nmap <silent> ss :split<CR>
" :vertical ball " Rearrange splits VERTICALLY
" :ball " Rearrange splits HORIZONTALLY
set splitright " When splitting vertically, split to the right
set splitbelow " When splitting horizontally, split below

" Resize the widows
" nnoremap <silent> <Leader>+ :exe "resize " . (winheight(0) * 3/2)<CR>
" nnoremap <silent> <Leader>- :exe "resize " . (winheight(0) * 2/3)<CR>

" ... for normal mode
nnoremap <M-h> <C-w>h
nnoremap <M-j> <C-w>j
nnoremap <M-k> <C-w>k
nnoremap <M-l> <C-w>l

nnoremap <M-H> <C-w>H
nnoremap <M-J> <C-w>J
nnoremap <M-K> <C-w>K
nnoremap <M-L> <C-w>L

nnoremap <M-q> <C-w>q " Close current split
nnoremap <M-o> <C-w>o " Close all except current split
nnoremap <M-=> <C-w>= " Make all splits equal

" ... for insert mode
inoremap <M-h> <C-o><C-w>h
inoremap <M-j> <C-o><C-w>j
inoremap <M-k> <C-o><C-w>k
inoremap <M-l> <C-o><C-w>l

inoremap <M-H> <C-w>H
inoremap <M-J> <C-w>J
inoremap <M-K> <C-w>K
inoremap <M-L> <C-w>L

" ... for visual mode
vnoremap <M-h> <C-w>h
vnoremap <M-j> <C-w>j
vnoremap <M-k> <C-w>k
vnoremap <M-l> <C-w>l

vnoremap <M-H> <C-w>H
vnoremap <M-J> <C-w>J
vnoremap <M-K> <C-w>K
vnoremap <M-L> <C-w>L

" ... for terminal mode
if has('nvim')
  tnoremap <M-h> <C-\><C-n><C-w>h
  tnoremap <M-j> <C-\><C-n><C-w>j
  tnoremap <M-k> <C-\><C-n><C-w>k
  tnoremap <M-l> <C-\><C-n><C-w>l

  "works?
  tnoremap <M-H> <C-\><C-n><C-w>H
  tnoremap <M-J> <C-\><C-n><C-w>J
  tnoremap <M-K> <C-\><C-n><C-w>K
  tnoremap <M-L> <C-\><C-n><C-w>L
endif

" Tab navigation
nmap <silent> tt :tabnew<CR>
" g conflicts with coc
" w conflicts with ale (not using it now though)
nmap <silent> [w :tabprevious<CR>
nmap <silent> ]w :tabnext<CR>
nmap <silent> [W :tabrewind<CR>
nmap <silent> ]W :tablast<CR>

" nnoremap <Leader>o o<Esc>^Da
" nnoremap <Leader>O O<Esc>^Da

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

"*****************************************************************************
" Folding
"*****************************************************************************
nnoremap <space> za
vnoremap <space> zf


" -----------------------------------
" Terminal mode
" -----------------------------------

" terminal emulation
nnoremap <silent> <leader>sh :terminal<CR>

if has('nvim')
" Leaving terminal emulation with Esc as well
  tnoremap <Esc> <C-\><C-n>
  " For sending a literal <Esc> to the running process
  tnoremap <C-v><Esc> <Esc>


  " Go to insert mode whenver opening a new terminal
  " autocmd TermOpen * startinsert
  autocmd TermOpen term://* startinsert
    
endif


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
"  Paths
" -----------------------------------
" let g:python3_host_prog = expand("~/.config/nvim/py3-provider/bin/python")
" Overwrite this for each venv!

" -----------------------------------
" Visual stuff
" -----------------------------------

" ---------
" nvim-colorizer.lua
" ---------
" " NOT WORKING
" lua require'colorizer'.setup()

" rainbow parentheses
" commands
" " Activate
" :RainbowParentheses
" " Deactivate
" :RainbowParentheses!
" " Toggle
" :RainbowParentheses!!
" " See the enabled colors
" :RainbowParenthesesColors

" Activation based on file type
augroup rainbow_lisp
  autocmd!
  autocmd FileType json,cpp,python,lisp,clojure,scheme RainbowParentheses
augroup END


" Use nicer symbols for tabstops and EOLs
 set listchars=tab:\ ,eol:⏎

" -----------------------------------
" Theme config
" -----------------------------------
packadd! onedark.vim

set cmdheight=2                         " More space for displaying messages

set pumheight=10                        " Makes popup menu smaller

set background=dark                     " tell vim what the background color looks like

set number                              " Line numbers

set cursorline                          " Enable highlighting of the current line
set ruler              			            " Show the cursor position all the time

" syntax on
syntax enable
" The ':syntax enable' command will keep your current color settings.  This
" allows using ':highlight' commands to set your preferred colors before or
" after using this command.  If you want Vim to overrule your settings with the
" defaults, use: >
"     :syntax on

" more minimalist...
" set noshowmode                          " We don't need to see things like -- INSERT -- anymore

colorscheme onedark

" -----------------------------------
" Lightline config
" -----------------------------------

" For lightline use https://github.com/itchyny/lightline.vim
packadd! lightline.vim
packadd! lightline-bufferline


" icons in lightline?
let g:lightline#bufferline#enable_devicons = 1

" Vertical splits hiding status bar...

"
let g:lightline = {
          \ 'enable': {
            \ 'statusline': 1,
            \ 'tabline': 1
            \ },
          \ 'component_function': {
          \   'fileformat': 'LightlineFileformat',
          \ },
         \ }

function! LightlineFileformat()
  return &filetype ==# 'netrw' ? '' : &fileformat
endfunction

" lightline-bufferline
" More at https://github.com/mengelbrecht/lightline-bufferline
"

" Stops highlighting after saving!
" https://github.com/itchyny/lightline.vim/issues/406

set showtabline=2 " Very important actually...
let g:lightline#bufferline#show_number  = 1
let g:lightline#bufferline#shorten_path = 0
let g:lightline#bufferline#unnamed      = '[No Name]'

let g:lightline                  = {}
let g:lightline.tabline          = {'left': [['buffers']], 'right': [['close']]}
let g:lightline.component_expand = {'buffers': 'lightline#bufferline#buffers'}
let g:lightline.component_type   = {'buffers': 'tabsel'}
let g:lightline.colorscheme = "one"
