#this a node to test the distance sensor
import rclpy
from rclpy.node import Node
# from time import sleep #if you needed it.
from std_msgs.msg import  Float64                    
import board # is needed for the sensor to work if. you dont have circuitpython installed or need mor info 
#here is the link : https://github.com/adafruit/circuitpython
import adafruit_hcsr04 #is to make the distance sensor work if you dont have the library or need more info here is the link: https://github.com/adafruit/Adafruit_CircuitPython_HCSR04


sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D17, echo_pin=board.D4) # setting up of the sensor pins


class SonarTest(Node):
  
  

    def __init__(self):
        super().__init__('sonartest')
        self.hctest_ = self.create_publisher(Float64,'sonar_testtopic',10)
        #self.stringtest_ = self.create_publisher(String,'sonar_string',10)
        timer_period = 0.5 # a seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        
    def timer_callback(self):
        Smsg = Float64()
        Smsg.data= (sonar.distance)
        self.hctest_.publish(Smsg)
        self.get_logger().info(  'cm "%s"' % Smsg.data ) # logs the sensor data

def main(args=None):
    rclpy.init(args=args)

    sonartest = SonarTest()

    rclpy.spin(sonartest)

    


if __name__ == '__main__':
    main()




        
    
   
       
  
        
                  

    
    
        
   
     
            