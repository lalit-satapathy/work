#!/bin/bash
echo "Start export"
int_path="<PATH of integratopn repo>/integrations/packages"
dump_path="<PATH-of-dump>/all-dumps"

cd $int_path
pwd

for d in  * ; do
#for d in nginx oracle mongodb; do
    echo "$d installing"
    cd $d
    ~/work/code/elastic/main/elastic-package/elastic-package install
    cd  $dump_path
    mkdir $d
    cd $d
    echo "$d dumping"
    ~/work/code/elastic/main/elastic-package/elastic-package dump installed-objects  --package $d
    cd $int_path
    cd $d
    echo "uninstalling"
    ~/work/code/elastic/main/elastic-package/elastic-package uninstall
    cd ../
done

cd $dump_path
pwd
