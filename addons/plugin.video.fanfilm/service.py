# -*- coding: utf-8 -*-

"""
    FanFilm Add-on

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import threading

from resources.lib.libraries import control
from resources.lib.libraries import log_utils

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))


def syncTraktLibrary():
    control.execute(
        'RunPlugin(plugin://%s)' % 'plugin.video.fanfilm/?action=tvshowsToLibrarySilent&url=traktcollection')
    control.execute(
        'RunPlugin(plugin://%s)' % 'plugin.video.fanfilm/?action=moviesToLibrarySilent&url=traktcollection')


try:
    MediaVersion = control.addon('script.fanfilm.media').getAddonInfo('version')
    AddonVersion = control.addon('plugin.video.fanfilm').getAddonInfo('version')

    log_utils.log('######################### FANFILM ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT FANFILM VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log('### FANFILM PLUGIN VERSION: %s ###' % str(AddonVersion), log_utils.LOGNOTICE)
    log_utils.log('### FANFILM MEDIA VERSION: %s ###' % str(MediaVersion), log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
except:
    log_utils.log('######################### FANFILM ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT FANFILM VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log(
        '### ERROR GETTING FANFILM VERSIONS - NO HELP WILL BE GIVEN AS THIS IS NOT AN OFFICIAL FANFILM INSTALL. ###',
        log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)

if control.setting('autoTraktOnStart') == 'true':
    syncTraktLibrary()

if int(control.setting('schedTraktTime')) > 0:
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
    log_utils.log('#################### STARTING TRAKT SCHEDULING ################', log_utils.LOGNOTICE)
    log_utils.log(
        '#################### SCHEDULED TIME FRAME ' + control.setting('schedTraktTime') + ' HOURS ################',
        log_utils.LOGNOTICE)
    timeout = 3600 * int(control.setting('schedTraktTime'))
    schedTrakt = threading.Timer(timeout, syncTraktLibrary)
    schedTrakt.start()
