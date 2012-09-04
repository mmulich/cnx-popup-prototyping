#!/bin/sh
# Use this Build script to put everything in the right place.

git clone https://github.com/wysiwhat/Aloha-Editor.git
git clone https://github.com/oerpub/oerpub.editor.git

git clone https://github.com/pumazi/bootstrap.git
# Some dependencies are required to build this.
# See the bootstrap README for details...
cd bootstrap && make
