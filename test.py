import urllib
import os,sys
from dateutil import parser
from xml.dom.minidom import parse, parseString
from urllib import urlopen

def main():
	test_url = 'http://cultureelerfgoed.adlibsoft.com/harvest/wwwopac.ashx?database=images&search=pointer%201009%20and%20BE=%22interieur%22&limit=10&xmltype=grouped'
	xmlstring=urlopen(test_url).read()
	xmldoc = parseString(xmlstring)
	itemlist = xmldoc.getElementsByTagName('production.date.start')
	for elem in itemlist:
		print parser.parse(elem.firstChild.nodeValue)

if __name__ == '__main__':
	main()