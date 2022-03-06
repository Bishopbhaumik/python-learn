import os
import shutil

print(os.getcwd())
# os.mkdir('movies')
# print(os.path.exists('movies'))
if os.path.exists('movies'):
    print("already exists")
else:
    os.mkdir("movies")
open("fil_1.txt",'a').close()
# os.chdir()------->for changing directory
print(os.listdir())
pi=os.walk(r'C:')
# for cp,fn,fin in pi:
#     print(f"current path:{cp}")
#     print(f"folder name:{fn}")
#     print(f"filename:{fin}")
# shutil.rmtree("movies")

