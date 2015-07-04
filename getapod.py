#!/usr/bin/env python

import sys,os
import urllib
import urllib2
import re

WALL_PAPER_FILE_NAME = './apod.jpg'
APOD_URL = "http://antwrp.gsfc.nasa.gov/apod/astropix.html"

def get_image_file_name_from_url(url):
    try:
        apodhtml = urllib2.urlopen(url).read()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        print "Internet connection problem?"
        sys.exit()

    matches = re.search('href..(image.*[jpg\|png\|gif])',apodhtml)
    image_file_name = matches.group(1)
    #print 'matches', image_file_name
    return image_file_name


imgfile = get_image_file_name_from_url(APOD_URL)
urllib.urlretrieve("http://antwrp.gsfc.nasa.gov/apod/"+imgfile,WALL_PAPER_FILE_NAME)
    

