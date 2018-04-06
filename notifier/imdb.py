import lxml.html
from lxml.cssselect import CSSSelector
import requests
import json
released = []

def aired_or_not(link):
	r = requests.get(link)
	tree = lxml.html.fromstring(r.text)
	selector = CSSSelector('div.subtext a')
	result = selector(tree)
	for index, val in enumerate(result):
		if 'airs' or 'aired' in result[index].text:
			match = result[index]

	status = match.text
	if 'aired' in status:
		return True 



def season_scan(link):
	released.clear()
	r = requests.get(link)
	tree = lxml.html.fromstring(r.text)
	#selector = CSSSelector('div.subtext a')
	#result = selector(tree)
	selector = CSSSelector('div.info strong a')
	series_name_selector = CSSSelector('div.parent h3 a')
	series_name_result = series_name_selector(tree)
	series_name = series_name_result[0].text
	result = selector(tree)
	for item in result:
		link = "https://www.imdb.com"+item.get('href')
		title = item.text
		if aired_or_not(link):
			released.append(title)
	print("Total Series released-", released)
	print("Total Number-", len(released))
	info = {'total-released': len(released), 'episodes': released, 'series_name': series_name}
	return info

def dump_json(dict):
	return json.dumps(dict)