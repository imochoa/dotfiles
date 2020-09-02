
" -----------------------------------
" Autocommands
" -----------------------------------
au! BufWritePost $MYVIMRC ++nested source % " auto source when writing to init.vm alternatively you can run :source $MYVIMRC
" ++nested required for bufferline
" " Stops highlighting after saving!
" https://github.com/itchyny/lightline.vim/issues/406


" -----------------------------------
" HTML
" -----------------------------------
autocmd BufNewFile,BufRead *.html setlocal nowrap
" This will turn line wrapping off whenever you're working on an HTML file.
autocmd BufWritePre,BufRead *.html :normal gg=G"
" reindent the code whenever we read an HTML file as well as when we write it

" -----------------------------------
" YAML
" -----------------------------------
autocmd BufWritePre,BufRead *.yaml :normal gg=G"

" -----------------------------------
" JSON
" -----------------------------------
" Comments in JSON files
autocmd FileType json syntax match Comment +\/\/.\+$+
" reindent the file whenever we read or write it
autocmd BufWritePre,BufRead *.json :normal gg=G"


" -----------------------------------
" glTF
" -----------------------------------
" (has a json structure)
autocmd BufNewFile,BufRead *.gltf set syntax=json

" -----------------------------------
" Python
" -----------------------------------
autocmd BufNewFile,BufRead *.py set foldmethod=indent


""  ---- Minimal configuration:
"set smartindent   " Do smart autoindenting when starting a new line
"set shiftwidth=4  " Set number of spaces per auto indentation
"set expandtab     " When using <Tab>, put spaces instead of a <tab> character
"
"" ---- Good to have for consistency
"" set tabstop=4   " Number of spaces that a <Tab> in the file counts for
"" set smarttab    " At <Tab> at beginning line inserts spaces set in shiftwidth
"
"" ---- Bonus for proving the setting
"" Displays '-' for trailing space, '>-' for tabs and '_' for non breakable space
"set listchars=tab:>-,trail:-,nbsp:_
"set list
