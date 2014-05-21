gfmTodo for Sublime Text
------------------

gfmTodo add a shortcut to mark your task done, in a Github Flavoured Markdown way.


Installation
------------------

To install this plugin, you have two options:

* Clone source code to Sublime Text 2 app folder, eg. ~/Library/Application Support/Sublime Text 2/mdTodo.


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
    - [X] call mum tomorrow at 8 am. @done (2014-05-22 01:01)
    - [X] send pull request @done (2014-05-22 01:00)

Contribution
------------------

This is just a fork of mdTodo (https://github.com/groenewege/mdTodo).
