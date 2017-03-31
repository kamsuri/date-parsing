import urllib
import os,sys
from PIL import Image
from PIL.ExifTags import TAGS
import dateutil.parser
import moment
import dateparser
import pandas as pd

def download_photo(img_url,filename):

	try:
		with open(filename,'wb') as f:
			f.write(urllib.urlopen(img_url).read())
		dateparse(filename)
	except:
		return False
	return True

def dateparse(filename):
	for (k,v) in Image.open(filename)._getexif().iteritems():
		if("date" in TAGS.get(k).lower()):
			date,time=v.split()
			#m = moment.date(v)
			#print m.format('YYYY-M-D H:M')
			#p=dateparser.parse(date)
			print date
			d = pd.to_datetime(time)
			print d
			print '%s = %s' % (TAGS.get(k), v)
			#upload_date=datetime.datetime.now();
			#print upload_date
			#upload(orig_date,orig_time,upload_date,upload_time)


def main():
	test_url = ''
	name, ext = (test_url.split('/')[-1].split('.'))
	filename=str(name)+"."+str(ext)
	download_photo(test_url,filename)

if __name__ == '__main__':
	main()