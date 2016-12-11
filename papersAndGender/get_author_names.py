from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
baseurl = "http://confer.csail.mit.edu"
driver.get(baseurl)

# find the elements in teh tr tag (the conference names)
conferences = driver.find_elements_by_tag_name("tr")
print len(conferences)
#print conferences

outfile = open("papers.csv", 'w')
outfile.write('"conference","title","type","authors","abstract","keywords"\n')

for conference in conferences:
    conference_name = conference.find_elements_by_tag_name("a")[1].text.encode('utf8')
    conference_href = conference.find_elements_by_tag_name("a")[1].get_attribute("href")
    print (conference_name), conference_href
    
    subdriver = webdriver.Firefox()
    subdriver.get(conference_href)

    #need to click "Show More" so that all the papers are loaded
    while subdriver.find_element_by_id("show_papers"):
        try:
            subdriver.find_element_by_id("show_papers").click()
        except:
            break

    papers = subdriver.find_elements_by_tag_name("tr")
    print len(papers)

    for paper in papers:
        #not all papers have subtypes
        try:
            paper_subtype = paper.find_element_by_class_name("paper-subtype").text.replace("=", "").replace("- ", "").encode('utf8')
        except:
            paper_subtype = ""
        paper_authors = paper.find_element_by_class_name("paper-authors").text.encode('utf8')
        paper_title = paper.find_element_by_class_name("paper-title").text.encode('utf8')
        paper_abstract = paper.find_element_by_class_name("paper-cb").text.encode('utf8')
        
        #not all papers have keywords
        try:
            paper_keywords = paper.find_element_by_class_name("paper-keywords").text.encode('utf8')
        except:
            paper_keywords = ""
        outfile.write('"' + '","'.join([conference_name, paper_title, paper_subtype, paper_authors, paper_abstract, paper_keywords]) + '"\n')
    subdriver.quit()

driver.quit()




