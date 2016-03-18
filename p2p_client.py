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
# def sub_zmq_7001():
#
#     ctx_sub = zmq.Context()
#     sub_sock_zmq = ctx_sub.socket(zmq.SUB)
#
#     sub_chan = ""
#     sub_sock_zmq.setsockopt(zmq.SUBSCRIBE, sub_chan)
#
#     str_tcp = "tcp://" + SERVER_IP + ":" + str(SERVER_PORT)
#
#     sub_sock_zmq.connect(str_tcp)
#     print "### Connected:", str_tcp
#
#     try:
#         # Wait for incoming messages
#         while True:
#
#             ###################################################################
#             # if datetime.datetime.now() > checkout_test:
#             #     break
#             ###################################################################
#
#
#             str_ans = sub_sock_zmq.recv_string()
#             print "str_ans=", str_ans
#
#             time.sleep(0.1)
#
#         sub_sock_zmq.close()
#
#     except KeyboardInterrupt:
#
#         print '^C, sub_sock_zmq.close()'
#         sub_sock_zmq.close()
#
#
# sub_zmq_7001()


import zmq
import sys

port = "5556"

port1 = "5557"


context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)

socket.connect ("tcp://localhost:%s" % port1)


#  Do 10 requests, waiting each time for a response
for request in range (1,10):
    print "Sending request ", request,"..."
    socket.send ("Hello")
    #  Get the reply.
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"