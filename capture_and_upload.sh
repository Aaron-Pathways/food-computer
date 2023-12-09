#!/bin/bash
timestamp=`date +%h%d%Y_%H%M%S`
filename=$timestamp.jpg
filepath=`pwd`/projects/food-computer/

echo $filename
echo "filepath: ${filepath}"
echo $timestamp 
fswebcam -r 1280x720 --no-banner "${filepath}${filename}"
python ~/projects/food-computer/upload.py $filepath $filename $timestamp
echo "exit code $?"
rm -r "${filepath}${filename}"
