#!/bin/bash
timestamp=`date +%h%d%Y_%H%M%S`
usbname=8F20-7989
filename=$timestamp.jpg
filepath="/media/admin/${usbname}/snapshots/"

logpath=$filepath
logname=log.txt

fswebcam "${filepath}${filename}"
echo "${timestamp} - script run"
echo "exit code ${?}"
