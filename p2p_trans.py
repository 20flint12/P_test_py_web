#!/usr/bin/env python
# -*- coding: utf-8 -*-1

# __author__ = 'sergey'
#
#
# import stun
# nat_type, external_ip, external_port = stun.get_ip_info()
# print "1)", nat_type, external_ip, external_port
#
#
# # nat_type, external_ip, external_port = \
# #     stun.get_ip_info(stun_host='stun.ekiga.net')
# nat_type, external_ip, external_port = \
#     stun.get_ip_info(stun_host='stun.noc.ams-ix.net')
# print "2)", nat_type, external_ip, external_port
#
#
# nat_type, external_ip, external_port = stun.get_ip_info(stun_port=3478)
# print "3)", nat_type, external_ip, external_port
#
#
# external_ip = "localhost"
#
# SERVER_IP = external_ip
# SERVER_PORT = external_port
# print "====================", SERVER_IP, SERVER_PORT
#
#
# import time
# import datetime
# import os
# import sys
#
# import re
#
# import zmq
# import multiprocessing as mp
#
# import random
# import pprint
#
#
#
# def send_zmq_7000_push():
#
#     print("zmq.pyzmq_version() = {0}".format(zmq.pyzmq_version()))
#
#     context = zmq.Context()
#     # pub_sock_zmq = context.socket(zmq.DEALER)
#     pub_sock_zmq = context.socket(zmq.PUSH)
#     identity = "test{}".format( random.randint(1,10000) )
#     pub_sock_zmq.setsockopt(zmq.IDENTITY,identity)
#
#     SOCK_ZMQ = "tcp://%s:%s" % (SERVER_IP, SERVER_PORT)
#     pub_sock_zmq.connect(SOCK_ZMQ)
#     print "### Connected:", SOCK_ZMQ
#
#
#     try:
#
#         # Send messages forever
#         while True:
#
#             str2send = "Hello!"
#             print "zmq>", str2send
#             pub_sock_zmq.send("#win " + str2send)
#
#             time.sleep(1.2)
#
#         pub_sock_zmq.close()
#
#     except KeyboardInterrupt:
#
#         print '^C, pub_sock_zmq.close()'
#         pub_sock_zmq.close()
#
#
#
# send_zmq_7000_push()


import zmq
import time

port = "5556"

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)


socket.bind("tcp://*:%s" % port)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print "Received request: ", message
    time.sleep (1)
    socket.send("World from %s" % port)



