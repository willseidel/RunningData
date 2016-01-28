from lxml import html
import requests

page 				= requests.get('http://results.tfmeetpro.com/Athletic_Timing/TrackTown_USA_High_Performance_Meet_2/results_28.html')
tree 				= html.fromstring(page.content)
runners 			= tree.xpath('//td[@class="athlete"]/text()')
times 				= tree.xpath('//td[@class="time"]/text()')
print 'Runners: ', runners
print 'Times: ', times 