# wid_tool.py - Wikipedia Image Downloader

wid_tool.py is tool for downloading images in Wikipedia articles.
Upto date usage instructions can always be found by running

    $ python3 wid_tool.py -h

## Requirements

The requirements are the following:
* A quite new version of Python 3
* lxml
* cssselect

## Quick start

Let's download all images from a particular article:

    $ python3 wid_tool.py https://en.wikipedia.org/wiki/List_of_screw_drives

We should be able to find all the images downloaded in the current
folder. There is also a url ending filter available. Let's download only
the SVG files from the article above:

    $ python3 wid_tool.py -f svg https://en.wikipedia.org/wiki/List_of_screw_drives

Now only files with their corresponding urls ending with _svg_ should be
downloading.
