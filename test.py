from urllib import urlopen
from dateutil import parser
from xml.dom.minidom import parseString


def get_month(mn):
    months = ['January',
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


def main():
    test_url = 'http://cultureelerfgoed.adlibsoft.com/harvest/wwwopac.ashx?database=images&search=pointer%201009%20and%20BE=%22interieur%22&limit=10&xmltype=grouped' # noqa
    link = urlopen(test_url)
    if link.code == 200:
        xmlstring = link.read()
        xmldoc = parseString(xmlstring)
        itemlist = xmldoc.getElementsByTagName('production.date.start')
        for elem in itemlist:
            dt = parser.parse(elem.firstChild.nodeValue)
            ti = dt.strftime("%H:%M")
            day = dt.strftime("%d")
            year = dt.strftime("%Y")
            month = dt.strftime("%m")
            print '%s %s %s %s' % (ti, day, get_month(int(month)), year)
    else:
        print "File does not exist at given URL"


if __name__ == '__main__':
    main()
