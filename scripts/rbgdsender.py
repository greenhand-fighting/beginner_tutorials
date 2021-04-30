#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub=rospy.Publisher('rgbd',String, queue_size=10)
    rospy.init_node('rbgdsender', anonymous=True)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        rgbd_str="this is rgbd"
        rospy.loginfo(rgbd_str)
        pub.publish(rgbd_str)
        rate.sleep()

if __name__=="__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass