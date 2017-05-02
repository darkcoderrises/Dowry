import urllib, urllib2
from bs4 import BeautifulSoup as bs4

f = open("in.html", "w")

base_url = "http://judis.nic.in/Judis_Andhra/"
url = base_url + "textqry_new.asp"

headers = {
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,*/*; q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded'
}

for year_int in range(1950, 2018):
	year = str(year_int)
	print year

	form_data = urllib.urlencode({'party': 'domestic violence', 'cyear': year, 'action': 'validate_login'})
	filehandle = urllib2.urlopen(urllib2.Request(url, form_data))
	data = filehandle.read()

	soup = bs4(data, 'html.parser')
	file_list = soup.find_all("tr")[2:-1]

	for i in file_list:
		file_name = "domestic/andhra/" + year + "_"
		for td in i.find_all("td"):
			if td.find_all("a") == []:
				file_name += td.get_text().replace(u"\xa0", "") + " "
		file_name = file_name[:-1].encode('ascii','ignore')

		file_url = base_url + i.find_all("a")[0].get('href')
		file_request = urllib2.urlopen(file_url)
		file_data = file_request.read()
		f.write(file_data)
		
		file_soup = bs4(file_data, 'html.parser')
		file_content = file_soup.find_all("textarea")[0].get_text()
		
		try:
			court_file = open(file_name, 'w+')
			court_file.write(file_content)
			court_file.close()
		except:
			pass
