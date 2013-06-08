#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib
import re

BaseUrl = 'http://gd.weather.com.cn/'

def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()
  page.close()
  return html

def getCity(html):
  reg = '<li><a href="(/.*?/index.shtml)">.*?</a></li>'
  cityList = re.compile(reg).findall(html)
  return cityList

def getWeather(html):
  reg = '<a title=.*?>(.*?)</a>.*?<span>(.*?)</span>.*?<b>(.*?)</b>'
  weatherList = re.compile(reg).findall(html)
  return weatherList

cities = getCity(getHtml(BaseUrl))
for i in range(len(cities)):
  cities[i] = BaseUrl + cities[i][1:]
for city in cities:
  content = getHtml(city)
  List = getWeather(content)
  First = True
  for item in List:
    if not First:
      print '   ',
    print 'City: %s, Low: %s, High: %s' % (item[0],item[1], item[2])
    First = False

