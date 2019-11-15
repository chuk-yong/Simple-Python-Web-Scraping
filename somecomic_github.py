import requests
from lxml import html
import csv

# scrape hbrowse for title and thumbnails
# http://www.somecomic.com/browse/title/A

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36',
    'Content-Type': 'application/json',
    'Referer': 'http://droughtmonitor.unl.edu/MapsAndData/DataTables.aspx',
    'X-Requested-With': 'XMLHttpRequest',
}

url = 'http://www.somecomic.com/browse/title/A'

r = requests.get(url)
tree = html.fromstring(r.content)
for table in tree.xpath('//table'):
        t = str(table.xpath('.//td[@class="thumbTitleTd"]/text()')) #['\nAn Older Woman\n']
        title = t.replace('\\n','').replace('\'','').replace('[','').replace(']','').replace(' ','').replace('"','').replace('.','')
        for imageUrl in table.xpath('.//img[@class="thumbImg"]/@src'):
                fileName = imageUrl.split('/thumbnails/') #becomes ['http://www.somecomic.com', '13991_2.jpg']
                fileName = fileName[1]
                fileName = title + '-' + str(fileName)
                f = open(fileName,'wb') #must use wb
                image = requests.get(imageUrl)
                f.write(image.content)
                f.close
                
