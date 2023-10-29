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
b()