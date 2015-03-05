#!/usr/bin/python
# -*- coding: utf-8 -*-

# main.py is a path of sun.

# Copyright 2015 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# sun is a tray notification applet for informing about
# package updates in Slackware.

# https://github.com/dslackw/sun

# sun is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import pynotify


class Notify(object):

    def __init__(self):
        pynotify.uninit()
        pynotify.init("sun")
        self.n = pynotify.Notification("sun", "test",
                                       "/home/dslackw/sun/icon/sun.png")

    def show(self):
        self.n.show()

Notify().show()
