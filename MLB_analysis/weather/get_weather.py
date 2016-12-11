# code to scrape the weather data for each MLB city

"""Currently, six of the 30 MLB stadiums have retractable roofs to counter uncooperative weather: 
Rogers Centre, home of the Toronto Blue Jays; Chase Field, home of the Arizona Diamondbacks; 
Safeco Field, home of the Seattle Mariners; Miller Park, home of the Milwaukee Brewers; 
Minute Maid Park, home of the Houston Astros; and Marlins Park, home of the Miami Marlins. 
A seventh park, Tropicana Field, home of the Tampa Bay Rays, has a fixed roof. The rest are open."""

team_to_URL = {}

# NYM and NYY are same
# CHC and CHW are same

team_to_URL["ARI"] = "http://www.wunderground.com/history/airport/KPHX/DATE/DailyHistory.html"
team_to_URL["ATL"] = "http://www.wunderground.com/history/airport/KMGE/DATE/DailyHistory.html" 
team_to_URL["BAL"] = "http://www.wunderground.com/history/airport/KBWI/DATE/DailyHistory.html"
team_to_URL["BOS"] = "http://www.wunderground.com/history/airport/KBOS/DATE/DailyHistory.html"
team_to_URL["CHC"] = "http://www.wunderground.com/history/airport/KMDW/DATE/DailyHistory.html"
team_to_URL["CHW"] = "http://www.wunderground.com/history/airport/KMDW/DATE/DailyHistory.html"
team_to_URL["CIN"] = "http://www.wunderground.com/history/airport/KLUK/DATE/DailyHistory.html"
team_to_URL["CLE"] = "http://www.wunderground.com/history/airport/KBKL/DATE/DailyHistory.html"
team_to_URL["COL"] = "http://www.wunderground.com/history/airport/KAPA/DATE/DailyHistory.html"
team_to_URL["DET"] = "http://www.wunderground.com/history/airport/KDET/DATE/DailyHistory.html"
team_to_URL["HOU"] = "http://www.wunderground.com/history/airport/KHOU/DATE/DailyHistory.html"
team_to_URL["KCR"] = "http://www.wunderground.com/history/airport/KNKA/DATE/DailyHistory.html"
team_to_URL["LAA"] = "http://www.wunderground.com/history/airport/KFUL/DATE/DailyHistory.html"
team_to_URL["LAD"] = "http://www.wunderground.com/history/airport/KCQT/DATE/DailyHistory.html"
team_to_URL["MIA"] = "http://www.wunderground.com/history/airport/KMIA/DATE/DailyHistory.html"
team_to_URL["MIL"] = "http://www.wunderground.com/history/airport/KMKE/DATE/DailyHistory.html"
team_to_URL["MIN"] = "http://www.wunderground.com/history/airport/KMIC/DATE/DailyHistory.html"
team_to_URL["NYM"] = "http://www.wunderground.com/history/airport/KLGA/DATE/DailyHistory.html"
team_to_URL["NYY"] = "http://www.wunderground.com/history/airport/KLGA/DATE/DailyHistory.html"
team_to_URL["OAK"] = "http://www.wunderground.com/history/airport/KOAK/DATE/DailyHistory.html"
team_to_URL["PHI"] = "http://www.wunderground.com/history/airport/KPNE/DATE/DailyHistory.html"
team_to_URL["PIT"] = "http://www.wunderground.com/history/airport/KAGC/DATE/DailyHistory.html"
team_to_URL["SDP"] = "http://www.wunderground.com/history/airport/KSAN/DATE/DailyHistory.html"
team_to_URL["SEA"] = "http://www.wunderground.com/history/airport/KBFI/DATE/DailyHistory.html"
team_to_URL["SFG"] = "http://www.wunderground.com/history/airport/KSFO/DATE/DailyHistory.html"
team_to_URL["STL"] = "http://www.wunderground.com/history/airport/KSTL/DATE/DailyHistory.html"
team_to_URL["TBR"] = "http://www.wunderground.com/history/airport/KTPF/DATE/DailyHistory.html"
team_to_URL["TEX"] = "http://www.wunderground.com/history/airport/KGKY/DATE/DailyHistory.html"
team_to_URL["TOR"] = "http://www.wunderground.com/history/airport/CYTZ/DATE/DailyHistory.html"
team_to_URL["WSN"] = "http://www.wunderground.com/history/airport/KDCA/DATE/DailyHistory.html"





#//*[@id="boxscore"]/div/div/section[1]/div/text()[8]

#DATE of form 2006/12/14


#away team, win percentage, home team, win percentage, date, temp, condition, wind, attendance, 


from lxml.html import etree, parse
from os import listdir
from os.path import isfile, join
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


mypath = "game_schedules"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles.remove(".DS_Store")

print onlyfiles
#ino about the columns in these files can be found here: http://www.retrosheet.org/gamelogs/glfields.txt
#other years can be downloaded here: http://www.retrosheet.org/gamelogs/index.html

driver = webdriver.PhantomJS()
#driver = webdriver.Firefox() 
driver.set_window_size(1120, 550)


for yearfile in onlyfiles:
	f = open(mypath + "/" + yearfile, 'r')

	lines = f.readlines()
	for line in lines:
		split_line = line.split(",")
		date = split_line[0].replace('"', '')
		visiting_team = split_line[3].replace('"', '').lower() + "mlb"
		home_team = split_line[6].replace('"', '').lower() + "mlb"

		date = date[:4] + "_" + date[4:6] + "_" + date[6:]
		print date, visiting_team, home_team

		site_url = "http://mlb.mlb.com/mlb/gameday/index.jsp?gid=" + date + "_" + visiting_team + "_" + home_team + "_1#game=" + date + "_" + visiting_team + "_" + home_team + "_1,game_tab=box,game_state=Wrapup"
		driver.get(site_url)

		#try:
		#    element = WebDriverWait(driver, 10).until(
		#        EC.presence_of_element_located((By.ID, "boxscore"))
		##    )
		#finally:
		#    driver.quit()

		WebDriverWait(driver, 20).until(lambda driver : driver.find_element_by_class_name('header'))
		print driver.find_element_by_class_name("header").text

		#print driver.find_element_by_xpath('//*[@id="boxscore"]/div/div/section[1]/div/').text
		#driver.find_element_by_id("search_button_homepage").click()
		#print driver.current_url

driver.quit()


