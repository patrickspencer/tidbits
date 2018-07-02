# -*- coding: utf-8 -*-

"""
get-all-links.py
~~~~~~~~~~~~~~~~
Get all the links from a webpage
"""
from lxml import html
import requests

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
webpage = html.fromstring(page.content)

paths = webpage.xpath('//a/@href')
print(paths)
