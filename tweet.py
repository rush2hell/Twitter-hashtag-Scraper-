from selenium import webdriver
import time
import pandas as pd
webpage = webdriver.Chrome('Chromedriver.exe')
webpage.get('https://twitter.com/explore/tabs/trending')

time.sleep(30)

trends = webpage.find_elements_by_tag_name('span')
#print(trends)
trend_list = []
for i in trends:
	a = i.get_attribute('textContent')
	if (a.startswith('#')):
		if a not in trend_list:
			trend_list.append(a)
urls = []

for i in trend_list:
	i = i[1:]
	link = 'https://twitter.com/search?q=%23'+i+'&src=promoted_trend_click'
	urls.append(link)
dic = {'HashTag':trend_list,'URL':urls}
df = pd.DataFrame(dic)
df.to_csv("F:\\Projects\\My project\\Alien Brains\\Twitter Latest Tweets\\tweets.csv",index=False)
