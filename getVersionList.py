from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import json
import os

def getVersion(versionHtml):
    version = re.search(r'<h4 class="version-history__item__version-number">(.*?)</h4>',versionHtml,re.M|re.I).group(1)
    time = re.search(r'<time (.*)>(.*?)</time>',versionHtml,re.M|re.I).group(2)
    dict = {'version':version,'time':time}
    return dict

# 将记录存储
def saveData(appVersionList):
    jsObj = json.dumps(appVersionList)
    data = open('version.json','w')
    data.write(jsObj)
    data.close()


# 无需吊起浏览器)
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options = chrome_options)

# 需吊起浏览器
# browser = webdriver.Chrome()

url = "https://itunes.apple.com/cn/app/%E5%AD%A6%E4%B9%A0%E5%BC%BA%E5%9B%BD/id1426355645?mt=8"
browser.get(url)

# 由于id一直会变化,所以根据class找到标签并模拟点击操作
browser.find_element_by_css_selector("[class='we-modal__show link']").click()

# appVersions = browser.find_element_by_class_name("version-history__item")
# print('源码为：'+ appVersions.get_attribute('innerHTML'))

# 获取每个版本列表的源码准确地说这一步得到的不是html代码里边的元素需使用get_attribute('innerHTML')
# 才能转化为html代码
versionsHtmlList = browser.find_elements_by_class_name("version-history__item")

# for appVersion in appVersions:
#     print(appVersion.text)
# browser.quit()

appVersionList = []

for versionHtml in versionsHtmlList:
    appVersionList.append(getVersion(versionHtml.get_attribute('innerHTML')))
i = 1
for appVersion in appVersionList:
    print("\nNo%d" %i)
    print("version: " + appVersion['version'] + "\ntime:" + appVersion['time'])
    i = i + 1

if os.path.exists('version.json') == True:
    dataFile = open('version.json','r')
    listFile = json.load(dataFile)
    if appVersionList[0] == listFile[0]:
        print("App未更新")
    else:
        print("App已更新")
        print("最新版本为：%s" %appVersionList[0]['version'])
        print("更新日期为：%s" %appVersionList[0]['time'])
        saveData(appVersionList)
else:
    saveData(appVersionList)


