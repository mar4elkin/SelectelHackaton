#!/bin/sh
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