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


" ---------
" COC (move to the plugin config?)
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



" ---------
" nvim-gdb
" ---------
" We're going to define single-letter keymaps, so don't try to define them
" in the terminal window.  The debugger CLI should continue accepting text commands.
" function! NvimGdbNoTKeymaps()
"   tnoremap <silent> <buffer> <esc> <c-\><c-n>
" endfunction

" let g:nvimgdb_config_override = {
"   \ 'key_next': 'n',
"   \ 'key_step': 's',
"   \ 'key_finish': 'f',
"   \ 'key_continue': 'c',
"   \ 'key_until': 'u',
"   \ 'key_breakpoint': 'b',
"   \ 'set_tkeymaps': "NvimGdbNoTKeymaps",
"   \ }

" ---------
" Vimspector
" ---------

let g:vimspector_enable_mappings = 'HUMAN'
