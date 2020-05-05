#!/usr/bin/python3

import os, sys
import threading
import requests


'''
Question1
'''
print("PID: ", os.getpid())

'''
Question2
'''
os_name = sys.platform
if os_name == "linux":
	print("Loadavg: ", os.getloadavg())

'''
Question3
'''

loadavg_list = os.getloadavg()
cpu_counter = os.cpu_count()
print("5min loadavg is ", loadavg_list[1])
print("Cpu core count:", cpu_counter)

if((cpu_counter - loadavg_list[1]) < 1):
	exit()
	
'''
Question4
'''

def check_url(internet_adress):
	response = requests.get(internet_adress)
	if response.status_code == 200:
		print("Working!", internet_adress, "PID: ", os.getpid())
	else:
		print("Not Working!", internet_adress, "PID: ", os.getpid())


thread1 = threading.Thread(target=check_url, args=("https://api.github.com", ))
thread2 = threading.Thread(target=check_url, args=("http://bilgisayar.mu.edu.tr/", ))
thread3 = threading.Thread(target=check_url, args=("https://www.python.org", ))
thread4 = threading.Thread(target=check_url, args=("http://akrepnalan.com/ceng2034", ))
thread5 = threading.Thread(target=check_url, args=("https://github.com/caesarsalad/wow", ))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()




	


