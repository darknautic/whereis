"""
This script is intended to build the directory structure with enough density to challenge
and  test indexing method in  "whereis" daemon .

"""
import os,sys
import time

root_dir="C:\\0\\DIRS"
num_dirs=30
num_files=100
num_levels=10


def level_creator(base_path,level):
    if level <= num_levels:
        for d in range(1,num_dirs+1):
            new_dir=os.path.join(base_path, str(level) + "_" + str(d))
            try:
                os.makedirs(new_dir)
            except FileExistsError:
                pass

            level_creator(new_dir,level+1)
        for f in range(1,num_files+1):
            new_file=os.path.join(base_path,str(level)+"_"+str(f)+".txt")
            open(new_file, 'a').close()


def main(argv):
    t = time.time()
    level_creator(root_dir,0)
    print("Building Time : ", time.time() - t )



if __name__ == "__main__":
    main(sys.argv)