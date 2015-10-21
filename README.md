# insidebotcc
InsideTheAsylum's classic bot updated to work with ClassiCube

Description copy-pasted, originally written by InsideTheAsylum for MinecraftForum.net

#Things the bot can do
* Draw lines
* Draw cuboids (solid 2D or 3D areas). This means that you can draw cuboids out of blocks (ie: brick) or you can draw negative cuboids (ie: air) to flatten areas, etc.
* Copy & Paste 2D or 3D areas of the map from one part of the map to another, or due to how a chunk of the map is saved to your computer, to other servers.
* Backup & Restore parts of the map. You can selectively restore part of the map to say.. backup12, and then another part of the map to backup13.
* Sponge an area of the map by placing sponges every 5 blocks in 3 dimensions. Doesn't work the best right now since it won't place sponges inside of objects and so won't completely erase all of the water. Works somewhat with .restore in that you first place sponges with .sponge and then .restore them away.
* Erase blocks of a certain type from an area. This is what I'm using to get rid of sponges at the moment if I don't have an area .backup'd.

#Installation

You need to have the following installed on your computer:
* [Python 2.7](https://www.python.org/downloads/release/python-2710/)
* [Twisted for Python 2.7](http://twistedmatrix.com/trac/)
* [zope.interface for python 2.7](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
* [mechanize](http://wwwsearch.sourceforge.net/mechanize/download.html)

Once you have all of those installed, you can lunch the bot from the command line. Just follow the onscreen directions.

#Configuring the bot:
**Limiting who can use the bot:**
Create a users.txt file in the same directory as the script with the name of one allowed user per line. If the users.txt file does not exist, then anyone can use the bot. If it exists, then only the people named can use the bot.

**Configuring some bot settings:**
Open up the bot.py file with notepad and then at the very top, where it says 'User Configuration Section', you can edit some variables. Each variable has a little blurb next to it as to what it does. Do not change anything under the user configuration section part. I won't help you if you do.
