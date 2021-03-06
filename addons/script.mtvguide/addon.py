#      Copyright (C) 2018 Mariusz Brychcy
#      Copyright (C) 2016 Andrzej Mleczko
#      Copyright (C) 2014 Krzysztof Cebulski
#      Copyright (C) 2013 Szakalit
#
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import re, sys, os
import xbmcaddon, xbmcgui, xbmcplugin, xbmc
from strings import *
from skins import Skin
Skin.fixSkinIfNeeded()
import gui

class Start:
    def __init__(self):
        self.Run()

    def Run(self):
        try:
            Skin.checkForUpdates()
            w = gui.mTVGuide()
            w.doModal()
            w.close()
            del w
            xbmc.Player().stop()
            deb('')
            deb('###################################################################################')
            deb('')
            deb('m-TVGuide successfully closed')
            deb('')
            deb('###################################################################################')
            deb('')
        except Exception, ex:
            deb('addon.py exception: %s' % getExceptionString())

init = Start()
