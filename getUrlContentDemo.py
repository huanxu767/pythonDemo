#coding:utf-8
# pip install selenium
# http://npm.taobao.org/mirrors/chromedriver/
from selenium import webdriver
chromedriver = "/Applications/Google Chrome.app/Contents/MacOS/chromedriver"
browser = webdriver.Chrome(chromedriver)
con = browser.get("https://www.baidu.com")
# browser.quit()


