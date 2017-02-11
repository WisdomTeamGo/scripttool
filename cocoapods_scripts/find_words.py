#encoding: utf-8

import logging
import re
import os
import sys
from optparse import OptionParser

find_words_reg = u'@\"[\u4e00-\u9fa5]+'

class FindWords:
    def __init__(self,file_dir = ""):
        self.file_dir = file_dir
    def find_word_infiles(self,file_dir):
        if os.path.isdir(file_dir):
            file_list = os.listdir(file_dir)
            for file_item in file_list:
                file_path = "/".join([file_dir,file_item])
                #是文件
                if os.path.isfile(file_path):
                    if file_item.endswith(".m"):
                        file1 = open(file_path,'r')
                        str1 = file1.read()
                        reg = re.compile(find_words_reg)
                        mo = reg.search(str1.decode('utf8'))
                        if mo:
                            print(mo.group(0) +"----"+file_item)
                        else:
                            continue
                elif os.path.isdir(file_path):
                    self.find_word_infiles(file_path)
                else:
                    continue
def main():
    usage ='''
    Example:
    Most common use case:
    '''
    parser = OptionParser(usage=usage)
    #log
    parser.add_option("-v", "--verbose", dest="verbose",
                      help="log",
                      action="store_true")
    #find
    parser.add_option("-f", "--find", dest="find",
                      help="find all words in files",
                      action="append")
    (options, args) = parser.parse_args()
    #检查参数是否有效
    if options.verbose:
        log = logging.INFO
    else:
        log = logging.ERROR

    if options.find:
        file_dir = options.find[0]
        find_word = FindWords()
        find_word.find_word_infiles(file_dir)

if __name__ == "__main__":
     sys.exit(main())
