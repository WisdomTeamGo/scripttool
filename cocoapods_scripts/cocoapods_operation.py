# encoding: utf-8
__author__ = 'brucezhang'
import os
import re
import logging

dependency_reg = r's\.dependency\s*=\s*[\'"](.*)?[\'"]'
version_reg = r's\.version\s*=\s*[\'"](.*)[\'"]'
name_reg = r's\.name\s*=\s*[\'"](.*)[\'"]'

class PodSpecDependency:
    def __init__(self, name=None, version=None, dependencies=None):
        self.dependencies = dependencies
        self.name = name
        self.podSpecFilePath = None
        self.gitName = None
        self.version = version

def chang_podspec_dependency(path):
    #打开依赖的文件
    file = open(path)
    str = file.read()

    #去的podspect所在路径
    dir_name = os.path.dirname(path)
    dependency_obj = PodSpecDependency()
    dependency_obj.dependencies = []
    dependency_obj.gitName = os.path.basename(dir_name)
    dependency_obj.podSpecFilePath = path

    #获取版本号
    version_ret = re.compile(version_reg)
    vertion_mo = version_ret.search(str)
    if vertion_mo:
        dependency_obj.version = vertion_mo.group(1)

    #获取模块名称
    name_ret = re.compile(name_reg)
    name_mo = name_ret.search(str)
    if name_mo:
        dependency_obj.name = name_mo.group(1)

    #获取所有的依赖
    dependency_ret = re.compile(dependency_reg)
    dependency_mo = dependency_ret.findall(str,re.M)
    match_len = len(dependency_mo)
    if match_len < 1:
        return dependency_obj
    for item in dependency_mo:
        name = item
        obj = PodSpecDependency(name=name)
        dependency_obj.dependencies.append(obj)

    return dependency_obj


def add_version_number(dependency_obj,flag=3):
    """
    修改podspec版本号，加1

    :param dependency_obj: PodSpecDependency对象
    :param flag:  1:第一个加1 2：第2个加1 3：第3个加1
    :return:
    """
    ver = dependency_obj.version
    version_arr = ver.split('.')
    if flag == 1:
        sub_ver = int(version_arr[0]) + 1;
        sub_ver = str(sub_ver)
        ver = ".".join(sub_ver, "0", "0")
    elif flag == 2:
        sub_ver = int(version_arr[1]) + 1;
        sub_ver = str(sub_ver)
        ver = ".".join(version_arr[0], sub_ver, "0")
    else:
        sub_ver = int(version_arr[2]) + 1;
        sub_ver = str(sub_ver)
        ver = ".".join(version_arr[0], version_arr[1], sub_ver)
    dependency_obj.version = ver
    target_str = "s.version = '%$'" % dependency_obj.version
    pattern = re.compile(version_reg,re.M)

    file1 = open(dependency_obj.podSpecFilePath, 'r')
    str1 = file1.read()
    file1.close()

    str1 = re.sub(pattern,target_str,str1)

    file1 = open(dependency_obj.podSpecFilePath, 'w')
    file1.write(str1)
    file1.close()




def load_dependency(path):
    """
    加载.podspec文件，加载文件中 s.name, s.version, s.dependency
    :param model_path 项目路径，如:/Users/Bruce/work/deep/app_bj/app_bj_deep_core
    :return: PodSpecDependency对象或None
    """
    if os.path.isdir(path) is False:
        return  None;
    files = os.listdir(path)
    for item in files:
        if item.endswith(".podspec"):
            file_path = "/".join(path,item)
            return chang_podspec_dependency(file_path)
    return None



# 对文件进行操作
def add_and_commit_version(basedir,dependency_name,flag=3):
    """
    当做小版本更新，即bug修复时可以调用该方法
    用于实现创建tag，修改podspec, 自动修改version
    :param base_dir 要查找的路径，这个路径下包含所有的模块
    :param dependency_name: 如app_bj_deep_core
    :param flag:  1:第一个加1 2：第2个加1 3：第3个加1
    :return:
    """
    pod_item = None
    dependency_name = dependency_name.lower()
    file_path = '/'.join(basedir,dependency_name)
    pod_obj = load_dependency(path=file_path)
    if pod_obj is None:
        logging.info("版本更新失败: %s" %file_path)
    else:
        add_version_number(pod_obj,flag)
        target_dir = "/".join(basedir,pod_obj.gitName)
        cmd = 'sh commit.sh "%s" "%s" "%s"' % (target_dir, pod_obj.version, pod_obj.name)
        os.system(cmd)
















