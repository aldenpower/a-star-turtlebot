#!/usr/bin/env python3

import sys
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()
    #goal.target_pose.header.frame_id = "odom"
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "base_link"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = float(sys.argv[1])
    goal.target_pose.pose.position.y = float(sys.argv[2])
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.x = 0.0    
    goal.target_pose.pose.orientation.y = 0.0   
    goal.target_pose.pose.orientation.z = 0.0 # 0.7 0.0 -0.7 (90 +, origem, 90 -)
    
    goal.target_pose.pose.orientation.w = 1.0 # 0.7 1.0 0.7
    #goal.target_pose.pose.orientation

    client.send_goal(goal)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

    

if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")