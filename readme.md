gfmTodo for Sublime Text
------------------

gfmTodo add a shortcut to mark your task done, in a Github Flavoured Markdown way.
I wanted this syntax after reading this Article by Carl Sednaoui :
http://carlsednaoui.com/post/70299468325/the-best-to-do-list-a-private-gist

Installation
------------------

To install this plugin :

* Clone source code to Sublime Text 2 app folder, eg. ~/Library/Application Support/Sublime Text 2/gfmTodo.


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

Contribution
------------------

This is just a fork of mdTodo (https://github.com/groenewege/mdTodo).
