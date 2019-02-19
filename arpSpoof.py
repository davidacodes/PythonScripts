import scapy.all as scapy
import time
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argumnet("-t", "--target", dest="target", help="Target IP")
    parser.add_argument()

def get_mac(ip):
    # Create arp packet object. pdst - destination host ip address
    arp_request = scapy.ARP(pdst=ip)
    # Create