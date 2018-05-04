"""
whereis daemon
1.- Read configuration file
2.- Build index
3.- Refresh index cache

l = []  ; limit in python 2.7 32 bits   => 120898752
"""

import sys,os
import json
import time
import re


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
            print("[ERROR] - Configuration File Corrupted")
            sys.exit(1)


def verify_paths():

    if os.path.exists(index_cache_file):
        print("[INFO] - Index cache found " + index_cache_file )
    else:
        print("[WARN] - Index cache not found , creating index file ... ")

        try:
            open(index_cache_file, 'a').close()
            print("[INFO] - Index created successfully  ", index_cache_file)

        except FileNotFoundError:
            print("[ERROR] - Index path does NOT exist.")
            sys.exit(1)

    for user_path in user_paths:
        if not os.path.exists(user_path):
            print("[WARN] - Path to be indexed does NOT exist  " + user_path)
        else:
            user_valid_paths.append(user_path)

    print("[INFO] - Valid paths ", len(user_valid_paths) )


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

    print("[INFO] - Index Size : ", len( index_cache))
    print("[INFO] - Total Indexing Time : ", time.time() - t_start )

#def printError():
 #   str_err=re.compile('ERROR')
  #  error=

def main(argv):
    load_config()
    verify_paths()
    build_index()


if __name__ == "__main__":
    main(sys.argv)






