# scrapes the http://www.baseball-reference.com/postseason/ site for the game-by-game results of the World Series games

#outputs a csv with this header:
#year, away_team, away_team_score, home_team, home_team_score

import httplib
import re
from lxml import etree, html
from urllib2 import urlopen
from lxml.html import parse

def process(year):
    #try:
    site_url = ("http://www.baseball-reference.com/postseason/" + str(year) + "_WS.shtml")
    doc = parse(site_url).getroot()
    #except IOError:
    #    outfile.write(str(year) + "\tERROR\n")
    #    return
    print year

    for game in doc.xpath('//*[@id="page_content"]/pre'):
    	#print game.text_content()
    	content_split = game.text_content().split("\n")
    	print content_split[3] # the header info
    	print content_split[5] # the away team
    	away_team = content_split[5].split("     ")[0].lstrip()
    	#print away_team
    	away_score = content_split[5].split()[-3]
    	#print away_score
    	print content_split[6] # the home team
    	home_team = content_split[6].split("     ")[0].lstrip()
    	#print home_team
    	home_score = content_split[6].split()[-3]
    	#print home_score

    	to_write = [str(year), away_team, away_score, home_team, home_score]
    	outfile.write(",".join(to_write) + "\n")


outfile = open("world_series_stats.csv", 'w')
outfile.write("year,away_team,away_score,home_team,home_score\n")
years = [1903] + range(1905,2016) #go through 2015. no game in 1904
for year in years:
	process(year)


