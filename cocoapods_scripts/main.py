# encoding: utf-8
__author__ = 'brucezhang'

import logging
import os
import sys
import re
from optparse import  OptionParser
import cocoapods_operation

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

    #升级小的版本号
    parser.add_option("-c", "--commit", dest="commit",
                      help="commit small verdion",
                      action="append")
    #获取操作的路径
    parser.add_option("-d", "--directory", dest="directory",
                      help="dir which include submodules",
                      action="append")

    (options, args) = parser.parse_args()

    if options.verbose:
        log_level = logging.INFO
    else:
        log_level = logging.WARNING

    if options.commit is not None \
        or options.directory is not None:
        did_anything = True

    if options.commit is not None:
        print("%s" % options.directory)
        cocoapods_operation.add_and_commit_version(options.directory[0],options.commit[0],3)


if __name__ == "__main__":
    sys.exit(main())










