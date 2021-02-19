#!/usr/bin/env python

import time
import rospy
import subprocess
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import Adafruit_SSD1306
from std_msgs.msg import String

global message
message = "Se inicio el sistema."

def callback(msg):

  global message
  message = msg.data

if __name__ == '__main__':

  rospy.init_node('sub_oled')
  rospy.Subscriber("status", String, callback)

  rate = rospy.Rate(2)

  disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_bus=1, gpio=1)

  disp.begin()
  disp.clear()
  disp.display()

  # Create blank image for drawing.
  # Make sure to create image with mode '1' for 1-bit color.
  width = disp.width
  height = disp.height
  image = Image.new('1', (width, height))

  # Get drawing object to draw on image.
  draw = ImageDraw.Draw(image)

  # Draw a black filled box to clear the image.
  draw.rectangle((0,0,width,height), outline=0, fill=0)

  # Draw some shapes. First define some constants to allow easy resizing of shapes.
  padding = -2
  top = padding
  bottom = height-padding
  # Move left to right keeping track of the current x position for drawing shapes.
  x = 0

  # Load default font.
  font = ImageFont.load_default()

  while not rospy.is_shutdown():
    
    message_var = "Status: "+message

    draw.rectangle((0,0,width,height), outline=0, fill=0)
    #print len(message_var)
    if(len(message_var)>20 and len(message_var)<=40):
      msg1 = message_var[0:20]
      msg2 = message_var[21:]
      draw.text((x, top+16), msg1, font=font, fill=255)
      draw.text((x, top+25), msg2, font=font, fill=255)

    if(len(message_var)>40 and len(message_var)<=60):
      msg1 = message_var[0:20]
      msg2 = message_var[20:40]
      msg3 = message_var[40:]
      print msg1
      print msg2
      print msg3
      draw.text((x, top+16), msg1, font=font, fill=255)
      draw.text((x, top+25), msg2, font=font, fill=255)
      draw.text((x, top+34), msg3, font=font, fill=255)

    if(len(message_var)>60 and len(message_var)<=80):
      msg1 = message_var[0:20]
      msg2 = message_var[20:40]
      msg3 = message_var[40:60]
      msg4 = message_var[60:]
      draw.text((x, top+16), msg1, font=font, fill=255)
      draw.text((x, top+25), msg2, font=font, fill=255)
      draw.text((x, top+34), msg3, font=font, fill=255)
      draw.text((x, top+43), msg4, font=font, fill=255)

    if(len(message_var)>80 and len(message_var)<=100):
      msg1 = message_var[0:20]
      msg2 = message_var[20:40]
      msg3 = message_var[40:60]
      msg4 = message_var[60:80]
      msg5 = message_var[80:]
      draw.text((x, top+16), msg1, font=font, fill=255)
      draw.text((x, top+25), msg2, font=font, fill=255)
      draw.text((x, top+34), msg3, font=font, fill=255)
      draw.text((x, top+43), msg4, font=font, fill=255)
      draw.text((x, top+52), msg5, font=font, fill=255)

    else:
      draw.text((x, top+16), message_var, font=font, fill=255)

    disp.image(image)
    disp.display()    
    
    rate.sleep()

