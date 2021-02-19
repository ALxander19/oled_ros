#!/usr/bin/env python

import roslib; roslib.load_manifest('oled_ros')
import sys
import time
import rospy
from std_msgs.msg import String

if __name__ == '__main__':

  rospy.init_node('pub_oled')
  pub = rospy.Publisher("status", String, latch=True, queue_size=1)

  msg = String()
  msg.data = str(sys.argv[1])
  #msg.data = "Hola"
  #print str(sys.argv[1])
  pub.publish(msg)
  time.sleep(1)
