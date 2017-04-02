from urllib import urlopen
import os,sys
from PIL import Image
from PIL.ExifTags import TAGS
from dateutil import parser
import time

def get_month(mn):
    months=['January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'Novemner',
    'December'
    ]
    return months[mn-1]

def download_photo(img_url,filename):
    
    try:
        with open(filename,'wb') as f:
            f.write(urlopen(img_url).read())
    except OSError as e:
        if e.errno == errno.ENOENT:
            print "File not found error"
    except Exception as e:
        print e

def dateparse(filename):
    
    for k, v in Image.open(filename)._getexif().iteritems():
        if "date" in TAGS.get(k).lower():
            #print '%s = %s' % (TAGS.get(k), v)
            conv = time.strptime(v,"%Y:%m:%d %H:%M:%S")
            ti = time.strftime("%H:%M", conv)
            day  = time.strftime("%d", conv)
            year = time.strftime("%Y", conv)
            month = time.strftime("%m", conv)
            print '%s %s %s %s' % (ti, day, get_month(int(month)), year)
            
def main():
    
    test_url = 'http://enigmata.csinsit.org/levels/try.jpg'
    filename = test_url.split('/')[-1]
    f = urlopen(test_url)
    if f.code == 200:
        download_photo(test_url,filename)
        dateparse(filename)
    else:
        print "File does not exist at given URL"
    
if __name__ == '__main__':
    main()