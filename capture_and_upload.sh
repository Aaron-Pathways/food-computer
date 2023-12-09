#!/bin/bash
timestamp=`date +%h%d%Y_%H%M%S`
filename=$timestamp.jpg
filepath=`pwd`/

echo $filename
echo "filepath: ${filepath}"
echo $timestamp 
fswebcam -r 1280x720 --no-banner "${filename}"
python upload.py $filepath $filename $timestamp
rm -r $filename
