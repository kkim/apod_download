#!/usr/bin/env python

import sys,os
import urllib

WALL_PAPER_FILE_NAME = './apod.jpg'

def get_img_url():
    return os.popen("grep href..image.*[jpg\|png\|gif] astropix.html").readline().rstrip('\n')

def get_vimeo_url():
    return os.popen("grep player.vimeo.com astropix.html").readline().rstrip('\n')

def get_youtube_url():
    return os.popen("grep youtube astropix.html").readline().rstrip('\n')

def get_image_file_name_from_url(apodimg):
    return apodimg.split("\"")[1];

def get_vimeo_id_from_url(apodimg):
    return apodvimeo.split("\"")[1].split("/")[-1] # last element

if os.path.isfile("astropix.html"): os.remove("astropix.html")

try:
    urllib.urlretrieve("http://antwrp.gsfc.nasa.gov/apod/astropix.html","./astropix.html")
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    print "Internet connection problem?"
    sys.exit()
    
apodimg = get_img_url()
apodvimeo = get_vimeo_url()
apodyoutube = get_youtube_url()

if len(apodimg) > 0 :
    imgfile = get_image_file_name_from_url(apodimg)
    urllib.urlretrieve("http://antwrp.gsfc.nasa.gov/apod/"+imgfile,WALL_PAPER_FILE_NAME)
elif len(apodvimeo) > 0 :
    vimeoid = get_vimeo_id_from_url(apodvimeo)
    

