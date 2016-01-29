from lxml import html
import requests

root_url = 'http://results.tfmeetpro.com/Athletic_Timing/TrackTown_USA_High_Performance_Meet_2/results_'
page_id = '11.html'
targeturl = root_url + page_id
	
page = requests.get(targeturl)
tree = html.fromstring(page.content)
places = tree.xpath('//td[@class="place"]/text()')
runners = tree.xpath('//tr/td[@class="athlete"]/a/text()')
times = tree.xpath('//td[@class="time"]/text()')
print 'Places:', places
print 'Runners: ', runners
print 'Times: ', times

#this function takes in a base URL and concatenates it with a number and .html
def buildUrl(generalUrl,addOn):
	urltoscrape = generalUrl + str(addOn) + '.html' #brings together a general URL, an integer converted to a string and .html
	addOn = addOn + 1
	print urltoscrape
	print addOn
	pageb = requests.get(urltoscrape)
	treeb = html.fromstring(pageb.content)
	runnersb = treeb.xpath('//tr/td[@class="athlete"]/a/text()')
	print 'Runners B:', runnersb

generalUrl = 'http://results.tfmeetpro.com/Athletic_Timing/TrackTown_USA_High_Performance_Meet_2/results_'
addOn = 13
buildUrl(generalUrl,addOn)

