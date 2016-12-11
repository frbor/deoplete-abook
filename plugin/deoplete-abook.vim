if exists('g:loaded_deoplete_abook')
  finish
endif

let g:loaded_deoplete_abook = 1

let g:deoplete#sources#abook#abook_bin = get(g:, 'deoplete#sources#abook#abook_bin', 'abook')
