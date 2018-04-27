"""
whereis daemon
1.- Read configuration file
2.- Build index
3.- Refresh index cache
"""

import sys,os
import json
import time
from Utilities import  printInf,printWrn,printErr


index_cache_file = ""
user_paths = []
user_valid_paths = []
index_cache = []


def load_config():

    global index_cache_file
    global user_paths

    with open('config.json','r') as cf:
        try:
            config = json.load(cf)
            index_cache_file = config['INDEX_CACHE_FILE']
            user_paths = config['USER_PATHS']
        except :
            printErr("Configuration File Corrupted")
            sys.exit(1)


def verify_paths():

    if os.path.exists(index_cache_file):
        printInf("Index cache found " + index_cache_file)
    else:

        printWrn("Index cache not found , creating index file ... ")

        try:
            open(index_cache_file, 'a').close()
            printInf("Index created successfully  "+ index_cache_file)
        except FileNotFoundError:
            printErr("Index path does NOT exist.")
            sys.exit(1)

    for user_path in user_paths:
        if not os.path.exists(user_path):
            printWrn("Path to be indexed does NOT exist  " + user_path)
        else:
            user_valid_paths.append(user_path)

    printInf("Valid paths "+ str(len(user_valid_paths)))

def indexing(path):
    global index_cache

    for f in os.listdir(path):
        full_path_f = os.path.join(path,f)
        if os.path.isdir(full_path_f):
            indexing(full_path_f)
        else:
            index_cache.append(full_path_f)


def build_index():
    t_start = time.time()
    for path in user_valid_paths:
        indexing(path)
        print("Indexing \"" + path + " \" ... ")

    printInf("Index Size : "+ str(len( index_cache)))
    printInf("Total Indexing Time : "+ str(time.time() - t_start))

def main(argv):
    load_config()
    verify_paths()
    build_index()


if __name__ == "__main__":
    main(sys.argv)






