# https://medium.com/@777rip777/simple-network-scanner-with-python-and-scapy-802645073190

import scapy.all as scapy
import argparse

def get_argments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target", help="Target IP/IP range")
	options = parser.parse_args()
	return options

def scan(ip):
	arp_repuest = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst)




# for ping in range(1, 255):
# 	address = "192.168.1." + str(ping)
# 	res = subprocess.call(['ping', '-c' '1', address])
# 	if res == 0:
# 		print("ping to", address, "OK")
# 	elif res == 2:
# 		print("no response from", address)
# 	else: 
# 		print("ping to", address, "failed!")