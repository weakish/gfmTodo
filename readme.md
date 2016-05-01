gfmTodo for Sublime Text
------------------

gfmTodo add a shortcut to mark your task done, in a Github Flavoured Markdown way.

more info about task-lists in GFM :
https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments

Installation
------------------

To install this plugin :

### For Sublime 2

Clone source code to Sublime Text 2 app folder,
e.g. `~/Library/Application Support/Sublime Text 2/gfmTodo`.

### For Sublime 3

Clone source code to Sublime Text 3 `Packages` folder, e.g.
`~/Library/Application Support/Sublime Text 3/Packages/gfmTodo`

Usage
------------------

CTRL + SHIFT + d : toggle task completed


Samples 
------------------

Suppose we have the following todo file:

    # Project A:
    - [ ] call mum tomorrow at 8 am.
    - [ ] send pull request

Highlight this item line and press "CTRL + SHIFT + d", it marks a tag "@done" and also appends timestamp.

    # Project A:
    - [X] call mum tomorrow at 8 am. _@done (2014-05-22 11:31)_
    - [X] send pull request _@done (2014-05-22 11:31)_

Those will produce checkbox :

- [ ] call mum tomorrow at 8 am.
- [X] send pull request _@done (2014-05-22 11:31)_

Contribution
------------------

I started this project forking mdTodo (https://github.com/groenewege/mdTodo).
