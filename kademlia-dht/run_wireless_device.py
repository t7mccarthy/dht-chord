import logging
import asyncio
import sys

from kademlia.network import Server

import math
import random

import time
import os

def nextTime(rateParameter = 1/5):
    return -math.log(1.0 - random.random()) / rateParameter

# f = open("sensors.txt", "a")
# f.write("starting device")
# f.close()
# print("starting_device")


# handler = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# log = logging.getLogger('kademlia')
# log.addHandler(handler)
# log.setLevel(logging.DEBUG)

loop = asyncio.get_event_loop()
loop.set_debug(True)

value = 0
server = Server()
bootstrap_node = ("0.0.0.0", 8468)
# print("about to write")
while True:
	# f = open("demofile2.txt", "a")
	# 	f.write("Now the file has more content!")
	# f.close()
	print("beginning while loop", sys.argv[1])
	loop.run_until_complete(server.listen(8475 + int(sys.argv[1])))
	loop.run_until_complete(server.bootstrap([bootstrap_node]))
	next_time = time.time() + nextTime()
	# next_time = time.time() + 1000000000000000
	# while time.time() < next_time:
	while True:
		# f = open("sensors.txt", "a")
		# f.write("inserting", sys.argv[1], value)
		# f.close()
		print("inserting")
		# print("inserting", sys.argv[1], value)
		for device in range(int(sys.argv[1]) * 10, int(sys.argv[1]) * 10 + 10):
			sys.stdout = open(os.devnull, 'w')
			try:
				result = loop.run_until_complete(server.set(device, value))
				print(result)
			except:
				pass
		sys.stdout = sys.__stdout__
		# print("device lookup", int(sys.argv[1]) - 1, loop.run_until_complete(server.get(str(int(sys.argv[1]) - 1))))
		value += 1
		# time.sleep(0.25)
		# exit(0)
	server.stop()
loop.close()
