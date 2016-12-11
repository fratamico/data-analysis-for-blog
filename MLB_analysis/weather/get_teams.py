#this file iterates backwards through the years to determine when one team last changed cities
import httplib
import itertools
import sys

from datetime import datetime
from lxml import etree, html
from urllib2 import urlopen
from lxml.html import parse


years = range(2015,1875,-1)
all_teams = {}

for year in years:

    all_teams[year] = set()

    try:
        site_url = ("http://www.baseball-reference.com/leagues/MLB/" + str(year) + "-standings.shtml")
        doc = parse(site_url).getroot()
    except IOError:
        outfile_basic_info.write(str(patent) + "\t" + str(start) + "\tERROR\n")
        continue

    for row in doc.xpath('//*[@id="expanded_standings_overall"]/tbody/tr'):
    	#children = row.getchildren()
    	team = row.getchildren()[1].text_content().encode('utf8')
    	all_teams[year].add(team)

    if year < 2015:
    	if all_teams[year] != all_teams[year+1]:
    		# 2011/2012 FLA -> MIA (same city though)
    		# 2007/2008 TBD -> TBR (Devil Rays -> Rays)
    		print year, ":", list(all_teams[year].difference(all_teams[year+1])), "->"
    		print year+1, ":", list(all_teams[year+1].difference(all_teams[year])), "\n"


