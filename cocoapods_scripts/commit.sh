#!/usr/bin/env bash

export TARGET_DIR=$1
export POD_VERSION=$2
export POD_NAME=$3

cd ${TARGET_DIR}
git commit -am "${TARGET_DIR}"
git tag ${POD_VERSION}
git push
git push --tags



#提交podspec文件
cd ../app_bj_deep_cocaopods/Specs
git pull
mkdir ${POD_NAME}
cd ${POD_NAME}
mkdir ${POD_VERSION}
cd ${POD_VERSION}

#将podspec文件拷贝到Specs下
echo "拷贝${TARGET_DIR}/${POD_NAME}.podspec文件到deep_cocoapods目录下"
cp ${TARGET_DIR}/${POD_NAME}.podspec ${POD_NAME}.podspec
git add *
git commit -am "${POD_NAME}: [${POD_VERSION}]"
git push

