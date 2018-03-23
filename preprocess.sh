#! /bin/bash
##
# Preprocessing for summaries
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
files=`ls SUMMARIES/*`

for file in $files; do
    is_first=false
    if [[ "`head -c 1 $file`" == "*" ]]; then
        cat $file >> SUMMARY.md
    else
        cat $file | sed 's/^/    /g' >> SUMMARY.md
    fi
done
