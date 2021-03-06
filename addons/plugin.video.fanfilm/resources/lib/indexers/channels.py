# -*- coding: utf-8 -*-

'''
    Covenant Add-on

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
'''
try:
    import urlparse
except:
    import urllib.parse as urlparse
import requests
from bs4 import BeautifulSoup
from resources.lib.indexers import navigator

filmweb_url = "http://www.filmweb.pl"
result = requests.get("http://www.filmweb.pl/program-tv").content
soup = BeautifulSoup(result, "html.parser")


class channels:
    def get(self):
        for movief in soup.find_all('div', attrs={'class': 'area'}):
            linkrf = movief.find('a').get("href")
            titlef = movief.find('a', attrs={'class': 'name'}).text
            tvh = movief.find('div', attrs={'class': 'cap'}).text
            img = movief.find('img').get("src").replace(".2.", ".3.")
            navigator.navigator().addDirectoryItem(titlef + ' [B](' + tvh + ')[/B]', 'movieSearchterm&name=%s' % titlef,
                                                   img, img)
        navigator.navigator().endDirectory()
