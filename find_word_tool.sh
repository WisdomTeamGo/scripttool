#!/usr/bin/env bash

#获取文件的路径
export SOURCE_PATH=$1

#进到目录文件下
cd cocoapods_scripts

python find_words.py -f ${SOURCE_PATH}
