#!/bin/python3
import sys
import json
import socket
import random
import time

import threading
from config import *
from network import *
from address import *

def requires_connection(func):
	def inner(self, *args, **kwargs):
		self.open_connection()
		ret = func(self, *args, **kwargs)
		self.close_connection()
		return ret
	return inner


class ClientNode(object):
	def __init__(self,RemoteAddress = None):
		if RemoteAddress == None:
			print("Please enter one chord Node address !")
			exit(-1)

		self._serverAddress = RemoteAddress
		self.client_running = True
		self.start()
	
	def open_connection(self):
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.connect((self._serverAddress.ip, self._serverAddress.port))

	def close_connection(self):
		self._socket.close()
		self._socket = None
	
	def printPromt(self):
		print("Enter 1 to lookup")
		print("Enter 2 to insert")
		print("Enter 3 to load dictionary")
		print("Enter 4 to display finger table")
		print("Enter 5 to Exit")


	def send(self, msg):
		#self._socket.sendall(msg + "\r\n")
		send_to_socket(self._socket,msg)
		self.last_msg_send_ = msg

	def recv(self):
		# print "send: %s <%s>" % (msg, self._address)
		# we use to have more complicated logic here
		# and we might have again, so I'm not getting rid of this yet
		return read_from_socket(self._socket)
	
	@requires_connection
	def lookUpKey(self,key):
		self.send('lookUpKey '+key)
		return self.recv()

	@requires_connection
	def queryFingerTable(self):
		self.send("getFingerTable")
		return self.recv()

	@requires_connection
	def insertKeyVal(self,key,value):
		self.send('insertKeyVal '+key+' '+value)	
		return self.recv()

	def start(self):
		while self.client_running:
			self.printPromt()
			choice  = input("Enter your choice :")
			if choice=='1':
				key = input("Input Key :") #TODO check type
					
				returnvalue = self.lookUpKey(key)
				
				if returnvalue == '-1':
					print("Key :",key," not found !!")
				else:
					print("Key : ",key," :: Value : ",returnvalue)

			if choice=='2':
				key = input("Input Key :") # TODO type check
				value = input("Input Value :") # TODO type check

				returnvalue = self.insertKeyVal(key,value)
					# key-value are always inserted !

				print("Key : ",key," :: Value : ",value," inserted")
				
			if choice=='3':
				f = open("dictionary.txt")
				a = f.readline()

				while a:
					a = a.split()
					print(a)
					key = a[0]
					value = " ".join(a[1:])
					self.insertKeyVal(key,value)
					print("INSERTED :: key:"+key+"|| value:"+value)
					a = f.readline()

			if choice == '4':
				retval = self.queryFingerTable()
				print(retval)


			if choice =='5':
				exit(0)

	def automated_lookup(self, key):
		# Return value for a key
		returnvalue = self.lookUpKey(key)
		if returnvalue == '-1':
			print("Key :",key," not found !!")
		else:
			print("Key : ",key," :: Value : ",returnvalue)
	
	def automated_insert(self, key, value):
		# Insert a key value pair into the DHT
		returnvalue = self.insertKeyVal(key,value)
					# key-value are always inserted !
		print("Key : ",key," :: Value : ",value," inserted")
	
	def automated_load(self, sensors_dict):
		# Insert many key value pairs into the DHT
		for key,value in sensors_dict.items():
			self.insertKeyVal(key,value)
			#print("INSERTED :: key:"+key+"|| value:"+value)
		print(f"Inserted {len(sensors_dict)} key-value pairs into the DHT.")
	
	def automated_display(self):
		# Display finger table
		retval = self.queryFingerTable()
		print(retval)

	def generate_key_values(self, num_keys):
		# Generate a dictionary of N key-value pairs
		return_dict = {}
		for i in range(num_keys):
			key = "a" + str(i)
			value = str(i)
			return_dict[key] = value
		return return_dict

	def automated_script(self, num_keys):
		sensors_dict = self.generate_key_values(num_keys)
		current_time = time.time()
		# Insert key-value pairs from dictionary
		self.automated_load(sensors_dict)
		surpassed_time = time.time() - current_time
		print(f"Inserting {num_keys} key-value pairs took {surpassed_time} milliseconds.")
		# Check on random keys with flexible queries
		keys_lst = list(sensors_dict.keys())
		keys_lst = random.shuffle(keys_lst)
		current_time = time.time()
		for k in keys_lst:
			self.automated_lookup(k)
		surpassed_time = time.time() - current_time
		print(f"Checking {num_keys} key-value pairs (randomly) took {surpassed_time} milliseconds.")
		print("Successfully exited.")
		exit(0)

if __name__ == "__main__":
	import sys
	if len(sys.argv) == 4:
		local = ClientNode(Address(sys.argv[1], sys.argv[2]))
	else:
		print("Insufficient argumrnts")
		exit(0)
	local.automated_script(int(sys.argv[3]))		# arv[3] is num of keys