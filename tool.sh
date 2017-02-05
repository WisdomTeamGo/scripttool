#!/usr/bin/env bash

# 用法 升级小版本号
# ./tools.sh "-c tao800config -v"

#获取当前目录
export ORIGINAL_DIR=`pwd`

#回到上一级目录
cd ../

#获取目标目录
export TARGET_DIR=`pwd`

cd ${ORIGINAL_DIR}

cd cocoapods_scripts

python main.py -d ${TARGET_DIR} $1