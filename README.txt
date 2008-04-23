== SOM Letter Categorizer ==

=== Dependencies ===
To run, you will require:
    * python    - http://www.python.org/
        * python2.5
    * wxpython  - http://www.wxpython.org/
        * python-wxgtk2.8
    * pil       - http://www.pythonware.com/products/pil/
        * python-imaging

You can install these with the following command on Debian/Ubuntu Linux:
sudo apt-get install python2.5 python-wxgtk2.8 python-imaging


If helpful, the other wxpython dependencies are: libwxbase2.8-0 libwxgtk2.8-0

=== Image files ===
Images files are stored in the data directory. New images must be run through the normalize script before they can be used. You must run normalize.py for _all_ input images. To add new fonts, add them to the list at the top of imagedata.py in the function getFontList(). It is recommended that you do not use spaces in the names.

normalize.py will normalize (in place) any files with the input font name for the letters A-F
    python normalize.py TimesNewRoman Arial
will normalize TimesNewRoman_A.png ... TimesNewRoman_F.png and Arial_A.png .. Arial_F.png

=== Running ===
You can run using
    make run
Or
    python main.py
