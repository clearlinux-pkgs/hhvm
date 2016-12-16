#!/bin/bash

[ -d .git ] || die "Not starting in correct place"

moddirs=$(find .git -name config | grep modules)

geturl(){
    WP=$(realpath --relative-to $PWD "${1%config}$(sed -n 's/[ \t]//g;s/^worktree=//p' $1)")
    URL=$(sed -ne '/url = /{' -e 's/[ \t]*url = //p' -e q -e '}' $1)
}

for m in $moddirs
do
    name=${m##*/modules/}
    name=${name%%/*}
    geturl $m
    printf '\t%-90s %s \\\n' ${URL%.git}"/archive/$(< ${m%config}HEAD).tar.gz" ${WP}
done

