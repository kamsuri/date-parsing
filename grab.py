import urllib
import os,sys
from PIL import Image
from PIL.ExifTags import TAGS

def download_photo(img_url,filename):

    try:
        f = open(filename,'wb')
        f.write(urllib.urlopen(img_url).read())
        f.close()
        dateparse(filename)
    except:
        return False
    return True

def dateparse(filename):
	for (k,v) in Image.open(filename)._getexif().iteritems():
		if("date" in TAGS.get(k).lower()):
			date,time=v.split()
			print '%s = %s' % (TAGS.get(k), date,time)


def main():
    test_url = 'http://www.csinsit.org/img/team/mansimar.jpg'
    name, ext = (test_url.split('/')[-1].split('.'))
    filename=str(name)+"."+str(ext)
    download_photo(test_url,filename)

if __name__ == '__main__':
    main()