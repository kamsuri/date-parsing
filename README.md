# date-parsing

In test.py, i have used URL("http://cultureelerfgoed.adlibsoft.com/harvest/wwwopac.ashx?database=images&search=pointer%201009%20and%20BE=%22interieur%22&limit=10&xmltype=grouped") to fetch the production date and used Dateutil module for date parsing.

I was also trying to do something with the image URL in grab.py. In this file i have given a URL of an image, downloaded it to local and using its exif data fetched metadata fields related to date.

I have tried Dateutil, Dateparser and Datetime modules for date parsing but found Dateutil to be the best one.
