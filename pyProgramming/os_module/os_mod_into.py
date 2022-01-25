import os
import pathlib
import glob
# gets the currrent working directory
print(os.getcwd())
# returns three tuples
#file path,sub-directories,files
#the goes in each subdirectory and prints file path,sub-directory, file recursively
""" print(os.environ.get('HOME')) """
path1 = pathlib.Path('/media/onesmus/dev/dev/python/pyProgramming/os_module')
print(path1.absolute())
# print(len(list(path1.glob('os_module/*'))))
print(pathlib.Path.cwd())
print(pathlib.Path.home())
# print(path)
# print(dir(pathlib))
# print("*"*100)
# print(dir(os))