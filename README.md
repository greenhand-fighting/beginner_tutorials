# beginner_tutorials
这是一个功能包，放在ros工作空间中直接一起编译就行

前提：
在小车上运行：
roslaunch xtark_driver xtark_camera.launch
roslaunch xtark_opencv xtark_people_detection.launch
运行人体检测launch文件

之后运行：
rosrun beginner_tutorials get_rects_and_send_rate.py

get_rects_and_send_rate.py 订阅/people/found话题， 发布/rate话题

/rate话题信息数据类型 float32 Is_people
如果Is_people==1.0   证明前方有人，减速或停止
如果Is_people==0.0   证明前方无人，继续运行

