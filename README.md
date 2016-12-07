# pungen
Python Username Generator - for all your random username needs!


pungen is a simple to use Python script which generates "usernames" on demand.
The usernames are created on the spot using some pre-defined word-creating formulas.
I'm making this seem way fancier than it is.


###Usage

The format for generating usernames from command line is:

`pungen <username_length>`

This will generate ten usernames of the specified length. You can specify a range of lengths like this:

`pungen <min_username_length> <max_username_length>`

Note that a random number 1 - 3 digits long will be appended to the end of some usernames, ignoring the length value.
The text in the username will always be within the lengths specified.

I really just wrote this for fun, if you can come up with something to do with it, by all means, use it.
That should be all you need to know. Oh, it's for Python 3.
