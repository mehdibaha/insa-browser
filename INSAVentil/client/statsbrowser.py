#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,'../..')
from basebrowser import BaseBrowser
from bs4 import BeautifulSoup

# Retrieves majors stats from the school's website
class StatsBrowser(BaseBrowser):
    # Parse html to get departments stats
    def resultFromHtml(self, result):
        data = []
        soup = BeautifulSoup(result)
        table = soup.find('table', attrs={'class':'portlet-table block-centered'})
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) != 0: # No empty columns.
                cols = [int(ele.text) for ele in cols] # Gets text, and strips it
                data.append([ele for ele in cols if ele]) # No empty elements.
        return data