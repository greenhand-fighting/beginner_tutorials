#!/usr/bin/env python
from __future__ import print_function

import sys
import rospy
import cv2
import numpy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from beginner_tutorials.msg import Num
from cv_bridge import CvBridge, CvBridgeError

class NumType:
    def __init__(self,distance=5,mi_distance_x=0,mi_distance_y=0):
        self.mi_distance=distance
        self.mi_distance_x=mi_distance_x
        self.mi_distance_y=mi_distance_y

class image_converter:

    def __init__(self):
        rospy.init_node('image_converter', anonymous=True)
        self.max=0
        self.point=NumType()
        self.image_pub = rospy.Publisher("distance",Num,queue_size=10)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/depth/image_raw",Image,self.callback)
        

    def callback(self,data):
        #print(data.data)
        print("i get max: %f " % self.max)
        #print(data.header.seq)
        #print(data.height)
        #print(data.data)
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "32FC1")
            print(cv_image.shape)
            print(cv_image)
        except CvBridgeError as e:
            print(e)

        (rows,cols) = cv_image.shape
        self.point.mi_distance=5
        nan_num=0
        for i in range(rows):
            for j in range(cols):
                if numpy.isnan(cv_image[i][j]):
                    nan_num+=1
                elif cv_image[i][j]>=self.max:
                    print("max position is here : %d , %d" % (i, j))
                    self.max=cv_image[i][j]
                elif cv_image[i][j]<self.point.mi_distance:
                    self.point.mi_distance=cv_image[i][j]
                    self.point.mi_distance_x=j
                    self.point.mi_distance_y=i
        print("nan_number: %d" % nan_num)
        print("not_nan_number: %d" % (480*640-nan_num))
        #if cols > 60 and rows > 60 :
        cv2.circle(cv_image, (self.point.mi_distance_x,self.point.mi_distance_y), 10, 0)     # this function is draw circle!
        cv2.circle(cv_image,(self.point.mi_distance_x,self.point.mi_distance_y), 15, 255)
        cv2.circle(cv_image,(0,0), 15, 255)
        cv2.circle(cv_image,(0,0), 10, 0)
        cv2.circle(cv_image,(640, 480), 15, 255)
        cv2.circle(cv_image,(640, 480), 10, 0)


        cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)

        try:
            self.image_pub.publish(self.point.mi_distance, self.point.mi_distance_x, self.point.mi_distance_y)   # parameters number !!!
        except CvBridgeError as e:
            print(e)

def main(args):
    ic = image_converter()
    #rospy.init_node('image_converter', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
