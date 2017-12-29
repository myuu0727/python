from urllib import request
url = 'https://movie.douban.com/cinema/nowplaying/shenzhen/'
resp = request.urlopen('https://movie.douban.com/cinema/nowplaying/shenzhen/')
htmlNowPlayData = resp.read().decode('utf-8')

from bs4 import BeautifulSoup
soup = BeautifulSoup(htmlNowPlayData,"html.parser")
nowPlayMovie = soup.find_all('div',id='nowplaying')
nowPlayMovieList = nowPlayMovie[0].find_all('li',class_='list-item')
MovieSaveList = []
for item in nowPlayMovieList:
	nowPlayDict = {}
	nowPlayDict['id'] = item['data-subject']
	for tag_img_item in item.find_all('img'):
		nowPlayDict['name'] = tag_img_item['alt']
		MovieSaveList.append(nowPlayDict)
print(MovieSaveList)

comUrl = 'https://movie.douban.com/subject/' + MovieSaveList[4]['id']
resp = request.urlopen(comUrl)
htmlComData = resp.read().decode('utf-8')
soup = BeautifulSoup(htmlComData,"html.parser")
comDivList = soup.find_all('div', class_='comment')

comSaveList = []
for item in comDivList:
	if item.find_all('p')[0].string is not None:
		comSaveList.append(item.find_all('p')[0].string)
print(comSaveList[1])

