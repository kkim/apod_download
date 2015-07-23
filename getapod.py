#!/usr/bin/env python

import sys,os
import urllib
import urllib2
import re

WALL_PAPER_FILE_NAME = './apod.jpg'
APOD_URL = "http://antwrp.gsfc.nasa.gov/apod/astropix.html"

def get_image_file_name_from_apodhtml(apodhtml):
    matches = re.search('href..(image.*[jpg\|png\|gif])',apodhtml)
    image_file_name = matches and matches.group(1)
    #print 'matches', image_file_name
    return image_file_name

def get_youtube_id_from_apodhtml(apodhtml):
    matches = re.search('youtube.com/embed/([0-9a-zA-Z]+)?',apodhtml)
    youtube_id = matches and matches.group(1)
    #print 'matches', youtube_id
    return youtube_id


if __name__ == '__main__':
    try:
        apodhtml = urllib2.urlopen(APOD_URL).read()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        print "Internet connection problem?"
        sys.exit()

    imgfile = get_image_file_name_from_apodhtml(apodhtml)
    if imgfile:
        print "Downloading today's picture"
        urllib.urlretrieve("http://antwrp.gsfc.nasa.gov/apod/"+imgfile,WALL_PAPER_FILE_NAME)
        sys.exit()
    
    youtube_id = get_youtube_id_from_apodhtml(apodhtml)
    if youtube_id:
        print "Downloading today's youtube thumbnail"
        urllib.urlretrieve("https://img.youtube.com/vi/"+youtube_id+'/0.jpg',WALL_PAPER_FILE_NAME)
        sys.exit()
        
