#!/bin/sh
read -p "New name: " -r ProjectName
projectname=$(echo "$ProjectName" | sed -e 's/\(.*\)/\L\1/')

read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
fi

echo "del __pycache__ and migrations dir's"
find . -name "__pycache__" -type d -exec rm -r "{}" \;
find . -name "migrations" -type d -exec rm -r "{}" \; 
rm -f db.sqlite3

echo "remove .git"
rm -rf .git/

read -p "Remove config/settings.template.py configure.py?" -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    # do dangerous stuff
    rm config/settings.template.py configure.py
fi

echo "rename selectelhackaton/ dir"
mkdir $projectname
mv selectelhackaton/* $projectname
rm -fr selectelhackaton

echo "find&replace selectelhackaton and SelectelHackaton"
find . -type f -exec sed -i "s/selectelhackaton/$projectname/" {} + 
find . -type f -exec sed -i "s/SelectelHackaton/$ProjectName/" {} + 
#TODO: fix bug with docker-compose.yml
