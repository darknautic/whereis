"""
whereis daemon
1.- Read configuration file
2.- Build index
3.- Refresh index cache
"""

import sys,os
import json


def load_config():
    with open('config.json','r') as cf:
        config = json.load(cf);

    if os.path.exists( config['index'] ):
        print("[INFO] - Index cache found " + config['index'] )

    else:
        print("[WARN] - Index cache not found , creating index file ... ")

        try:
            open(config['index'],'a').close()
            print("[INFO] - Index created successfully  ", config['index'])
        except FileNotFoundError:
            print("[ERROR] - Index path does NOT exist.")



def main(argv):
    load_config()



if __name__ == "__main__":
    main(sys.argv)






