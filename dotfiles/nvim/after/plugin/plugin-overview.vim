
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

" Git wrapper
call minpac#add('tpope/vim-fugitive')

" Better comments
call minpac#add('tpope/vim-commentary')

" Makes navigating around projects easier
call minpac#add('tpope/vim-projectionist')

" Running a build and navigating failures
call minpac#add('tpope/vim-dispatch')
call minpac#add('radenling/vim-dispatch-neovim') " Adapter for vim-dispatch

" For tests
call minpac#add('janko-m/vim-test')

" snippet engine
call minpac#add('SirVer/ultisnips')

" Comprehensive list of snippets for each file type
call minpac#add('honza/vim-snippets')

" Asynchronous linting engine
" call minpac#add('w0rp/ale')


" For debugging
call minpac#add('sakhnik/nvim-gdb', { 'do': ':!./install.sh \| UpdateRemotePlugins' })
call minpac#add('puremourning/vimspector')

" Adds the 'line' text object 'l' (like 'w')
call minpac#add('kana/vim-textobj-user')
call minpac#add('kana/vim-textobj-line')

" easier aligning 
call minpac#add('godlygeek/tabular')

" ?
call minpac#add('tpope/vim-scriptease', {'type': 'opt'})


" netrw extensions
call minpac#add('tpope/vim-vinegar')

" managing sessions
call minpac#add('tpope/vim-obsession')
", {'type': 'opt'})

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


" Visuals.....

" Rainbow parentheses
call minpac#add('junegunn/rainbow_parentheses.vim')

" See colors on color codes!
" call minpac#add('norcalli/nvim-colorizer.lua') " Not working...

" Icons on things (netrw not yet supported but there's an issue for it!)
call minpac#add('ryanoasis/vim-devicons')

" Themes should be OPTIONAL -> {'type': 'opt'}
"     They have to be explicitly loaded with 'packadd!' in the theme section!
call minpac#add('joshdick/onedark.vim', {'type': 'opt'})

" lightline + themes
call minpac#add('itchyny/lightline.vim', {'type': 'opt'})
call minpac#add('mengelbrecht/lightline-bufferline', {'type': 'opt'})

" Add other plugins here.
" call minpac#add('vim-jp/syntax-vim-ex')

" Load the plugins right now. (optional)
"packloadall

" For installing
command! PackUpdate call minpac#update() 
" For uninstalling
command! PackClean call minpac#clean()
" Make tags
command! PackDocs silent helptags ALL
" List installed packages
command! PackList :echo join(split(join(sort(keys(minpac#getpluglist())), "\n"), ','),"\n")
" nnoremap  <leader>rt :echo join(split(&runtimepath, ','),"\n") <CR>

