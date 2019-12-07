# import logging
# import asyncio
# import sys
#
# from kademlia.network import Server
#
# if len(sys.argv) != 5:
#     print("Usage: python set.py <bootstrap node> <bootstrap port> <key> <value>")
#     sys.exit(1)
#
# handler = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# log = logging.getLogger('kademlia')
# log.addHandler(handler)
# log.setLevel(logging.DEBUG)
#
# loop = asyncio.get_event_loop()
# loop.set_debug(True)


import subprocess
import time

print('RUNNING SIMULATION:')

# command = ['python3 start_network.py']

# subprocess.run(['python3', 'start_network.py', 'python3', 'new_node.py'])
# # print("Done")
# subprocess.run(['python3', 'new_node.py'])
# subprocess.run(['python3', 'new_node.py'])
# subprocess.run(['python3', 'new_node.py'])
# subprocess.run(['python3', 'new_node.py'])
# subprocess.run(['python3', 'new_node.py'])
N=4
print(f"This will initialize {N} gnome terminals.")
command = ['gnome-terminal','--tab','-e',"python3 start_network.py"]
for i in range(N):
	new_port = 8469 + i
	new_gnome = ['--tab','-e',f"python3 new_node.py 0.0.0.0 8468 {new_port}"]
	command.extend(new_gnome)
print('This is the comamnd:', command)
current_time = time.time()
subprocess.run(command)
surpassed_time = time.time() - current_time
print(f"Initializing {N} nodes took {surpassed_time} milliseconds.")