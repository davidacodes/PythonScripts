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
	broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
	arp_request_broadcast = broadcast/arp_repuest
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

	clients_list = []
	for element in answered_list:
		client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list

def print_result(result_list):
	print("IP\t\t\tMac Address")
	print("---------------------------------------")
	for client in result_list:
		print(client["ip"] + "\t\t" + client["mac"])

options = get_argments()
scan_result = scan(options.target)
print_result(scan_result)




# for ping in range(1, 255):
# 	address = "192.168.1." + str(ping)
# 	res = subprocess.call(['ping', '-c' '1', address])
# 	if res == 0:
# 		print("ping to", address, "OK")
# 	elif res == 2:
# 		print("no response from", address)
# 	else: 
# 		print("ping to", address, "failed!")