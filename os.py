import os

pid = os.fork()  # fork反复拷贝
if pid == 0:
    print("A", os.getpid(), os.getppid())
else:
    print("B", os.getpid(), os.getppid())

# os.getpid()获取当前进程id     os.getppid()获取父进程id