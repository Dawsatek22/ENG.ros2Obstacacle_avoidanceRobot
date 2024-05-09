
#this is a  node to test the dc motors

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from time import sleep

from gpiozero import  PWMOutputDevice # using the Pwm class for the motors.
#this are the gpio pin setup for using L298N motor driver.
ena = PWMOutputDevice(14)
enb = PWMOutputDevice(25)
in1 = PWMOutputDevice(15)
in2 = PWMOutputDevice(18)

in3 = PWMOutputDevice(23)
in4 = PWMOutputDevice(24)
#this are the motor direction.
def stop():
    ena.value = 0
    enb.value = 0
    in1.value = 0
    in2.value = 0
    in3.value = 0
    in4.value = 0
def forward():
    
   
    ena.value = 1
    enb.value = 1
    in1.value = 1
    in2.value = 0
    in3.value = 1
    in4.value = 0
def backward():
    
    ena.value = 1
    enb.value = 1
    in1.value = 0
    in2.value = 1
    in3.value = 0
    in4.value = 1
def left():
    
   
    ena.value = 1
    enb.value = 1
    in1.value = 1
    in2.value = 0
    in3.value = 1
    in4.value = 0

def right():
    
    ena.value = 1
    enb.value = 1
    in1.value = 0
    in2.value = 1
    in3.value = 1
    in4.value = 0
    
def motortest(): #the motor test fuction.
    forward()
    print("forward")
    sleep(3)
    backward()
    print("backward")
    sleep(3)
    left()
    print("left ")
    sleep(3)
    right()
    print("right")
    sleep(3)
    stop()

        
class DcPublisher(Node):
    
    def __init__(self):
        super().__init__('motortest')
        self.dctest_ = self.create_publisher(String,'Dc_testtopic',10)
        timer_period = 0.5 # a seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
    def timer_callback(self):
        msg = String()
        msg.data = 'its Rolling: %d ' % self.i
        self.dctest_.publish(msg)
        self.get_logger().info('publishing motors: "%s"' %msg.data)
        self.i += 1
        motortest()
      
        
       
        
def main(args=None):
    rclpy.init(args=args)

    dcpub = DcPublisher()
    rclpy.spin(dcpub)
    rclpy.shutdown()
if __name__ == '__main__':
    main()