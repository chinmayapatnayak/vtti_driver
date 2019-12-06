#!/usr/bin/env python

# For VTTI Use Only

import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import TwistWithCovarianceStamped

### ROS MSGS
## IMU
# imu.orientation.x
# imu.orientation.y
# imu.orientation.z
# imu.linear_acceleration.x
# imu.linear_acceleration.y
# imu.linear_acceleration.z
# imu.angular_acceleration.x
# imu.angular_acceleration.y
# imu.angular_acceleration.z

## Speed
# speed.twist.twist.linear.x
# speed.twist.twist.linear.y
# speed.twist.twist.linear.z

# CONSTANTS / WEIGHTS
W1 = 1000
W2 = 9999
W3 = 0
W4 = 0

class Driver:
    def __init__(self):
        self.imu = None
        self.orientation = None
        self.velocity = None
        self.speed = None
        self.score = None

    def imu_callback(self, data):
        self.imu = data
        # Print and Compute
        # Debug
	# rospy.loginfo(rospy.get_caller_id() + "\nlinear acceleration:\nx: [{}]\ny: [{}]\nz: [{}]".format(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z))
        self.compute_callback()

    def speed_callback(self, data):
        self.speed = data
        # Print and Compute
        # Debug
        # rospy.loginfo(rospy.get_caller_id() + "\nSpeed:\nx: [{}]\ny: [{}]\nz: [{}]".format(data.twist.twist.linear.x, data.twist.twist.linear.y, data.twist.twist.linear.z))
        self.compute_callback()

    def compute_callback(self):
        if self.speed is not None and self.imu is not None:
           # The Driver Equation Goes Here 
           self.score = (W1*self.speed.twist.twist.linear.x) + (W2*self.imu.linear_acceleration.x) 
           rospy.loginfo("Driver Score: [{}]".format(self.score))

if __name__ == '__main__':
    rospy.init_node('listener')

    driver = Driver()

    rospy.Subscriber("/imu/imu", Imu, driver.imu_callback)
    rospy.Subscriber("/speed", TwistWithCovarianceStamped, driver.speed_callback)
    
    rospy.spin()
