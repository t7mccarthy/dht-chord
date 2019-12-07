import logging
import asyncio
import sys
import random
import time

from kademlia.network import Server


def generate_key_values(num_keys):
		# Generate a dictionary of N key-value pairs
		return_dict = {}
		for i in range(num_keys):
			key = "a" + str(i)
			value = str(i)
			return_dict[key] = value
		return return_dict


def put(sensors_dict, loop, address, port):
	server = Server()
	server.listen(8469)
	bootstrap_node = (address, int(port))
	loop.run_until_complete(server.bootstrap([bootstrap_node]))

	for key,value in sensors_dict.items():
		loop.run_until_complete(server.set(key, value))

	print(f"Inserted {len(sensors_dict)} key-value pairs into the DHT.")

	# loop.run_until_complete(server.set(sys.argv[3], sys.argv[4]))
	server.stop()

def get(keys_lst, loop, address, port):
	server = Server()
	server.listen(8469)
	bootstrap_node = (address, int(port))
	loop.run_until_complete(server.bootstrap([bootstrap_node]))
	for k in keys_lst:
		result = loop.run_until_complete(server.get(k))
	server.stop()


num_keys = 10

# Loop initialization
loop = asyncio.get_event_loop()
loop.set_debug(True)
# Server initialization
server = Server()
loop.run_until_complete(server.listen(8469))
bootstrap_node = ("0.0.0.0", 8468)


# _________________Inserting_________________
sensors_dict = generate_key_values(num_keys)
current_time = time.time()
# Put calls
loop.run_until_complete(server.bootstrap([bootstrap_node]))
for key,value in sensors_dict.items():
	loop.run_until_complete(server.set(key, value))

print(f"Inserted {len(sensors_dict)} key-value pairs into the DHT.")
#put(sensors_dict, loop, "0.0.0.0", "8468")
surpassed_time = time.time() - current_time
print(f"Inserting {num_keys} key-value pairs took {surpassed_time} milliseconds.")



# _______________Querying_______________

keys_lst = list(sensors_dict.keys())
random.shuffle(keys_lst)
current_time = time.time()
#get(keys_lst, loop, "0.0.0.0", "8468")
for k in keys_lst:
	result = loop.run_until_complete(server.get(k))
surpassed_time = time.time() - current_time
print(f"Checking {num_keys} key-value pairs (randomly) took {surpassed_time} milliseconds.")


server.stop()
loop.close()
print("Successfully exited.")
exit(0)






# def something():
# 	sensors_dict = self.generate_key_values(num_keys)
# 	current_time = time.time()
# 	self.automated_load(sensors_dict)
# 	surpassed_time = time.time() - current_time
# 	print(f"Inserting {num_keys} key-value pairs took {surpassed_time} milliseconds.")
# 	keys_lst = list(sensors_dict.keys())
# 	random.shuffle(keys_lst)
# 	current_time = time.time()
# 	for k in keys_lst:
# 		self.automated_lookup(k)
# 	surpassed_time = time.time() - current_time
# 	print(f"Checking {num_keys} key-value pairs (randomly) took {surpassed_time} milliseconds.")
# 	print("Successfully exited.")
# 	exit(0)



# def put(count, address, port):
# 	loop = asyncio.get_event_loop()
# 	loop.set_debug(True)

# 	server = Server()
# 	loop.run_until_complete(server.listen(8469))
# 	bootstrap_node = (address, int(port))
# 	# print("bootstrap_node", bootstrap_node)
# 	loop.run_until_complete(server.bootstrap([bootstrap_node]))
# 	loop.run_until_complete(server.set(sys.argv[3], sys.argv[4]))
# 	server.stop()
# 	loop.close()

# def get():
# 	put():
# 	loop = asyncio.get_event_loop()
# 	loop.set_debug(True)

# 	server = Server()
# 	loop.run_until_complete(server.listen(8469))
# 	bootstrap_node = (sys.argv[1], int(sys.argv[2]))
# 	print("bootstrap_node", bootstrap_node)
# 	loop.run_until_complete(server.bootstrap([bootstrap_node]))
# 	loop.run_until_complete(server.set(sys.argv[3], sys.argv[4]))
# 	server.stop()
# 	loop.close()


# for i in range(N):
