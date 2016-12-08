__author__ = 'aman'

import hashlib
import os
import sys
import urllib.request, urllib.parse
import urllib3


def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()

# Add as necessary
videoExtensions = [".avi",".mp4",".mkv",".mpg",".mpeg",".mov",".rm",".vob",".wmv",".flv",".3gp"]

def subGetter(filename):
    try:

        originalFileName = filename
        for videoExt in videoExtensions:
            filename = filename.replace(videoExt, "")
        if originalFileName == filename:
            return "Not a media file."

        hash = get_hash(originalFileName)
        headers = { 'User-Agent' : 'SubDB/1.0 (subtitle-downloader/1.0; http://github.com/amanthedorkknight/subtitleDownloader)' }
        link = "http://api.thesubdb.com/?action=download&hash=" + hash + "&language=en"
        req = urllib.request.Request(link, None, headers)
        response = urllib.request.urlopen(req).read()

        with open (filename + ".srt", "wb") as subtitle:
            subtitle.write(response)
            print("Success! " + filename)

    except:
        print ("Not found! " + filename)

# Replace with the path to your movie directory        
rootdir = "/home/aman/Downloads/"

# Iterate the root directory recursively using os.walk and for each video file present get the subtitle
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        fname = os.path.join(root, file)
        subGetter(fname)


