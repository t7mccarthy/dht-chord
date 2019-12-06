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

print('RUNNING SIMULATION:')

# command = ['python3 start_network.py']

subprocess.run(['python3 start_network.py'])
