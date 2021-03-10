#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
import rospy
from std_msgs.msg import String
from pyax12.connection import Connection
import time

serial_connection = "global"
dynamixel_id = "global"

def callback(data):
    print(rospy.get_caller_id() + 'I heard %s', data.data)
    is_available=serial_connection.ping(dynamixel_id)
    rospy.loginfo('Servo is ready')
    serial_connection.goto(dynamixel_id, 0, speed=512, degrees=True)
    time.sleep(1)
    serial_connection.goto(dynamixel_id, -45, speed=512, degrees=True)
    time.sleep(1)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('servo', anonymous=True)

    rospy.Subscriber('servo_control', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    
if __name__ == '__main__':
    # Connect to the serial port
    serial_connection = Connection(port="/dev/ttyACM0", baudrate=57600)
    dynamixel_id = 5
    is_available=serial_connection.ping(dynamixel_id)
    print('Servo is ready')
    serial_connection.goto(dynamixel_id, -15, speed=512, degrees=True)
    time.sleep(1)
    serial_connection.goto(dynamixel_id, 0, speed=512, degrees=True)
    time.sleep(1)
    print('Servo Node Opened')
    listener()
    serial_connection.close()