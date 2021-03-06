#!/bin/zsh

# text create
pipenv run python main.py

# ini setting
INI_FILE=config.ini
INI_SECTION=FILE

# ini parser
eval `sed -e 's/[[:space:]]*\=[[:space:]]*/=/g' \
    -e 's/;.*$//' \
    -e 's/[[:space:]]*$//' \
    -e 's/^[[:space:]]*//' \
    -e "s/^\(.*\)=\([^\"']*\)$/\1=\"\2\"/" \
   < $INI_FILE \
    | sed -n -e "/^\[$INI_SECTION\]/,/^\s*\[/{/^[^;].*\=.*/p;}"`

# text open
month=`date '+%-m'`
year=`date '+%-Y'`

if [ $month -eq 1 ]; then
    open ./text/12-$(($month+1))$FILE$year.txt
elif [ $month -eq 12 ]; then
    open ./text/$(($month-1))-1$FILE$year.txt
else
    open ./text/$(($month-1))-$(($month+1))$FILE$year.txt
fi

exit