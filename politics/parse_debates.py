import requests
import bs4


response = requests.get(site_url)
soup = bs4.BeautifulSoup(response.text)

paragraphs = soup.findall('p')


from selenium import webdriver

driver = webdriver.Firefox()

site_url = "https://www.washingtonpost.com/news/the-fix/wp/2016/02/13/the-cbs-republican-debate-transcript-annotated/"
driver.get(site_url)

paragraphs = driver.find_elements_by_xpath('//*[@id="article-body"]/article/p')

for paragraph in paragraphs:
	print paragraph.text
