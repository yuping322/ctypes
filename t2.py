from ctypes import *
cdll.LoadLibrary("libc.so.6")  
libc = CDLL("libc.so.6")       
printf = libc.printf
printf(b"Hello, %s\n", b"World!")