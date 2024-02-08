def a():
    import time
    t0 = time.time()
    print(t0)
    print(type(t0))

def b():
    import os
    file_list = os.listdir("/usr/bin")
    print(file_list)
    print(type(file_list))

def aaa():
    print("aaa")

def bbb():
    print("bbb")
#options = {
#    1: aaa,
#    2: bbb,}
#i_appscho = int(input("请输入"))
#if i_appscho in options:
#    options[i_appscho]()
#else:
#    input("输入错误")

from tqdm import trange
#for i in trange(100000000):
#    i = i+1
#print("done")
from tqdm import tqdm
from time import sleep
bar=tqdm(total=100)
bar.set_description("Processing1")
sleep(5)
bar.update(10)
