#!/home/jihoon/.pyenv/versions/ROS/bin/python

from beginner_tutorials.srv import AddTwoInts, AddTwoIntsResponse
import rospy

def handle_add_two_ints(req):
    print("Returnning [%s + %s = %s]" % (req.a, req.b, (req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Read to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()