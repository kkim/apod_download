# apod_download
This program downloads the astronomy picture of the day to the current directory. 

# How to use it to automatically set the desktop wallpaper

1. Run `getapod.py` in the directory you want to keep the wallpaper file.
2. [Set the file as the wallpaper](http://askubuntu.com/a/69500).
3. Open crontab (`crontab -e`) and add `getapod.py` to it.
 0 0 * * * cd /home/<username>; ./scripts/apod_download/getapod.py

