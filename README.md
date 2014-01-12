wp-audio-uploader
=================

Uploads audio files as media to WordPress, creating a covering post from the meta-data tags.

wp-audio-uploader is copyright (c) 2013 Stephen Parry.

1. Licensing

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version. The program source code is also freely
available as per Section 4 of this README.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
License for more details.

You should have received a copy of the GNU General Public License
along with this program (in a file called LICENSE.txt); if not, go
to http://www.gnu.org/licenses/old-licenses/gpl-2.0.html or write to

  Free Software Foundation, Inc.
  59 Temple Place - Suite 330
  Boston, MA 02111-1307 USA

2. Installing audio uploader

The following compnents are required to run wp-audio-uploader:

1) Python 3.x  (Documentation www.python.org)
- Download and install as per docs for your platform. Windows: tick 'Add python to path' option.
- On Windows Add C:\Python33\Scripts (or equivalent) to your system path.

2) setuptools (Documentation https://pypi.python.org/pypi/setuptools) :
- Install as per docs for your platform; for Windows:
  - Download: https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
  - Execute:
      python ez_setup.py
  - or -
  - Dowload and unpack: https://pypi.python.org/packages/source/s/setuptools/setuptools-2.1.tar.gz
  - Execute:
      python setup.py install

3) Pip (Documentation http://www.pip-installer.org/en/latest/installing.html):
- Download https://raw.github.com/pypa/pip/master/contrib/get-pip.py
- Execute:
    python get-pip.py
    pip install --upgrade setuptools

4) python-wordpress-xmlrpc (Documentation http://python-wordpress-xmlrpc.rtfd.org):
- Execute:
      pip install python-wordpress-xmlrpc

5) hsaudiotag3k (http://hg.hardcoded.net/hsaudiotag)
- Execute:
      pip install hsaudiotag3k

6) wp-audio-uploader.py
- Download from this repo
- Place in C:\audio-uploader\ if you are planning to use with Eutychus.

3 Using audio uploader

The audio uploader was intended to be run by Eutychus, but can be run from the command line or a script.
Typical usage:

C:\audio-uploader\audio-uploader.py
  "C:\Path\To\AudioFileToUpload.mp3" http://somesite.org/wordpress/xmlrpc.php "UserA" "Secret"

