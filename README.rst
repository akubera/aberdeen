Aberdeen
========

Simple python script for taking a directory of markdown files and
generating/storing the backend of a blog.

The goal is to enable quick editing of simple text-files and posting them to a
database via a push to a git branch (default 'publish').

Upon running, a python JSON object is created from each file found. There is a
markdown header extracted from the file indicating post title, date posted,
authors, tags, etc. The content of the post is converted automatically to html
and added to the final object in the path.

The resulting objects (currently) are sent to a MongoDB session and saved to the
specified collection.

This process is strictly a 'model' management system, any view and controller
must be built/managed by you.

(The name comes from the "Aberdeen" fish hook 🎣)

Requirements
------------

- `Python 3.4 <https://www.python.org/>`__
- `Markdown <https://pythonhosted.org/Markdown>`__
- **Supported Databases**
    -  mongodb - `asyncio\_mongo <https://pypi.python.org/pypi/asyncio_mongo>`__

Installation
------------

Copy the ``post-update``, ``aberdeen.py`` and config files to the directory
``hooks`` in the git repository on the server. Edit the config file to your
specifications. This will be updated when uploaded to pypi.

Server Setup
------------

On your server, create a bare git repository, something like 'blog\_data'. This
will simply hold all your markdown (or maybe *other* type) files. Create a
'publish' branch in addition to another 'working' one (presumably 'master'). Add
the post-update webhook and configuration as explained in Installation. Clone
the repo to your working computer.

Usage
-----

This program requires a key-value pair header in each of the markdown files that
have typical elements required for blogging

::

    ---
    title : Post Title
    date  : Mar 15, 2015
    tags  : Example
            Feeling Happy
            XYZ
    author: Me
    ---

    # My New Post
    This is a great post! *All* my markdown works

The 'tags' attribute in this example will generate a list of strings; for more
information on how the metadata header works, `read this
<https://pythonhosted.org/Markdown/extensions/meta_data.html>`__.

Aberdeen creates a python 'time' object from the 'date' attribute. It will try
to be smart about the style of the date, and there are a few ways to interpret
the datetime from the string, but it has to be accepted in some form or another
by the `strptime
<https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`__
function of python ‘time’ library. The first way to work will be saved, so it
rewards consistency. It is recommended you put in a time field if you care about
that, else it will default to midnight of the determined date.

*Maybe this can be specified in the config file? (that's not implemented yet.)*

This kind of information is great for storing in NoSQL databases, so MongoDB is
the only database currently supported. The content of the markdown is converted
to HTML and added to the result as 'html\_content' field. The objects are sorted
in terms of date and written to the database. The previous table or collection
will dropped and the new items added. (***NO GUARANTEE*** that the items will be
in the same order).

Other Things
------------

Remeber this does not have any HTML structure or view-support for a blog. This
strictly converts one form of a model (markdown files) to another (database
entries). The view/controllers are totally up to you for retreiving and
displaying the posts.

Always assume that the database collection/table will be **erased** upon every
push. The idea is the database reflects the files, so changing a file will
replace that entry in the database. It is recommended to NOT use fixed links to
posts. It is suggested to used date+title as a unique identifier. Alternatively,
you could store a unique post id in the metadata field, if you want some
assurance that things will be fixed (but it's up to you to keep track of the and
their uniqueness).

LICENSE
-------

Apache 2.0
