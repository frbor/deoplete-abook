# deoplete-abook

A plugin for [deoplete](https://github.com/Shougo/deoplete.nvim) to get abook
autocompletion functionality.

This plugin was created by looking at the implementation of [deoplete-flow](https://github.com/steelsojka/deoplete-flow).

## Installation

Currently only tested with NeoVim and Python3 client.
Check out the deoplete documentation to get the basic setup.

Install this plugin with your favourite plugin manager.

Also make sure `abook` is available as it will use this command for auto completion:

```
npm install abook --mutt-query
```

## Configuration

```
# Binary path to your abook, defaults to your $PATH flow
let g:deoplete#sources#abook#abook_bin = 'abook'
```
