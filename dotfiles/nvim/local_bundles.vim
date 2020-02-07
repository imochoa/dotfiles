" ~/.config/nvim/local_init.vim

" To leave terminal mode easily
tnoremap <Esc> <C-\><C-n>

" vim-autoformat python files when you press F3...
noremap <F3> :Autoformat<CR>
"... and when you save
autocmd BufWritePre *.py :Autoformat

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


"" So that vim-flake8 can fix PEP-8 problems in file automatically
"autocmd BufWritePost *.py call Flake8()
"autocmd BufWritePost *.py wincmd p
"autocmd BufWritePost *.py set ft=python
