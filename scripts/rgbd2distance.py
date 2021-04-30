#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image

pub=rospy.Publisher("distance",String,queue_size=10)
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard  a  %d * %d image!" % (data.height, data.width))
    print(data.encoding)
    print(data.data[0][0])
    print("i have data now ,send it!")
    pub.publish("if get point?")
    
def listener():
    rospy.init_node('rgbd2distance', anonymous=True)
    rospy.Subscriber("/camera/depth/image_raw", Image, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()