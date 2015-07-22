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
    image_file_name = matches and matches.group(1)
    #print 'matches', image_file_name
    return image_file_name

def get_youtube_id(url):
    try:
        apodhtml = urllib2.urlopen(url).read()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        print "Internet connection problem?"
        sys.exit()

    matches = re.search('youtube.com/embed/([0-9a-zA-Z]+)?',apodhtml)
    youtube_id = matches and matches.group(1)
    print 'matches', youtube_id
    return youtube_id

imgfile = get_image_file_name_from_url(APOD_URL)
if imgfile:
    urllib.urlretrieve("http://antwrp.gsfc.nasa.gov/apod/"+imgfile,WALL_PAPER_FILE_NAME)
else:
    print 'No image file found'    
    youtube_id = get_youtube_id(APOD_URL)
    if youtube_id:
        urllib.urlretrieve("https://img.youtube.com/vi/"+youtube_id+'/0.jpg',WALL_PAPER_FILE_NAME)
        
