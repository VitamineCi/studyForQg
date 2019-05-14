import urllib.request
import re

url = "https://itunes.apple.com/cn/app/%E5%AD%A6%E4%B9%A0%E5%BC%BA%E5%9B%BD/id1426355645?mt=8"
response = urllib.request.urlopen(url).read().decode("utf-8")

# 将页面源码保存
# data = open('index.html','w',encoding='utf-8')
# data.write(response)

appVersionHistoryRe = re.compile(r'<li class="version-history__item">(.*?)</li>')
#print(appVersionHistoryRe)

appVersionHistorys = appVersionHistoryRe.findall(response)

#print(appVersionHistorys)
