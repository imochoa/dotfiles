" ~/.config/nvim/local_init.vim

"*****************************************************************************
" Terminal mode
"*****************************************************************************
tnoremap <Esc> <C-\><C-n>

"*****************************************************************************
" Nerd Tree
"*****************************************************************************
map <silent> <C-n> :NERDTreeFocus<CR>


"*****************************************************************************
" Folding
"*****************************************************************************
nnoremap <space> za
vnoremap <space> zf

"*****************************************************************************
" Python
"*****************************************************************************
augroup vimrc-python
  autocmd!
  autocmd FileType python setlocal expandtab shiftwidth=4 tabstop=8 colorcolumn=79
      \ formatoptions+=croq softtabstop=4 foldmethod=indent
      \ cinwords=if,elif,else,for,while,try,except,finally,def,class,with
augroup END


"*****************************************************************************
" Autoformat 
"*****************************************************************************

" vim-autoformat python files when you press F3...
" noremap <F3> :Autoformat<CR>

" When saving...
autocmd FileType json,yaml,python autocmd BufWritePre <buffer> :Autoformat
" Will autoformat JSON and NOT overwrite your buffer if there's an error
" autocmd FileType json autocmd BufWritePre <buffer> %!python3 -m json.tool 2>/dev/null || echo <buffer>

"*****************************************************************************
" Autocomplete 
"*****************************************************************************

" Autocomplete NCM2
augroup NCM2
  autocmd!
  " enable ncm2 for all buffers
  autocmd BufEnter * call ncm2#enable_for_buffer()
  " :help Ncm2PopupOpen for more information
  set completeopt=noinsert,menuone,noselect
  " When the <Enter> key is pressed while the popup menu is visible, it only
  " hides the menu. Use this mapping to close the menu and also start a new line.
  inoremap <expr> <CR> (pumvisible() ? "\<c-y>\<cr>" : "\<CR>")
  " uncomment this block if you use vimtex for LaTex
  " autocmd Filetype tex call ncm2#register_source({
  "           \ 'name': 'vimtex',
  "           \ 'priority': 8,
  "           \ 'scope': ['tex'],
  "           \ 'mark': 'tex',
  "           \ 'word_pattern': '\w+',
  "           \ 'complete_pattern': g:vimtex#re#ncm2,
  "           \ 'on_complete': ['ncm2#on_complete#omni', 'vimtex#complete#omnifunc'],
  "           \ })
augroup END

"*****************************************************************************                                  
" Snippets                                                                                                      
"*****************************************************************************                                  
" Trigger configuration. Do not use <tab> if you use https://github.com/Valloric/YouCompleteMe.                 
let g:UltiSnipsExpandTrigger="<tab>"                                                                            
" let g:UltiSnipsJumpForwardTrigger="<c-b>"                                                                     
" let g:UltiSnipsJumpBackwardTrigger="<c-z>"                                                                    
" If you want :UltiSnipsEdit to split your window.                                                              
" let g:UltiSnipsEditSplit="vertical"                                                                           
