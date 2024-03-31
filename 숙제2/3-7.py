import time

num = int(time.time()) % 26
print(chr(ord('A')+num))
