import logging
import asyncio
import sys

from kademlia.network import Server

import time

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
bootstrap_node = ("0.0.0.0", 8470)
# print("about to write")
# while True:
	# f = open("demofile2.txt", "a")
	# 	f.write("Now the file has more content!")
	# f.close()
	# print("beginning while loop", sys.argv[1])
loop.run_until_complete(server.listen(8469 + int(sys.argv[1])))
loop.run_until_complete(server.bootstrap([bootstrap_node]))
	# next_time = time.time() + 1000000000000000
	# while time.time() < next_time:
	# while True:
		# f = open("sensors.txt", "a")
		# f.write("inserting", sys.argv[1], value)
		# f.close()
print("inserting")
# print("inserting", sys.argv[1], value)
f = open("devicefile.txt", "a")
for device in range(int(sys.argv[1]) * 10, int(sys.argv[1]) * 10 + 10):
	try:
		result = loop.run_until_complete(server.set(device, value))
		print(device, value)
		f.write("1")
	except:
		pass
f.close()
# print("device lookup", int(sys.argv[1]) - 1, loop.run_until_complete(server.get(str(int(sys.argv[1]) - 1))))
		# time.sleep(0.25)
		# exit(0)
# server.stop()
# loop.close()
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.stop()
    loop.close()
