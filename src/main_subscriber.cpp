#include "ros/ros.h"
#include "std_msgs/String.h"
#include <cstdlib>

ros::Subscriber sub;
ros::Publisher servo_pub;
std_msgs:: String servo_msg;
std::stringstream ss_message;

/**
 * This tutorial demonstrates simple receipt of messages over the ROS system.
 */
void voiceCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
  if (strcmp(msg->data.c_str(), "hello") == 0)
    {
      std::system("espeak -vf4 \"hello\"");
    }
  if (strcmp(msg->data.c_str(), "move") == 0)
    {
      std::stringstream ss_message;
      ss_message << "hello servo";
      servo_msg.data = ss_message.str();
      ROS_INFO("%s", servo_msg.data.c_str());
      servo_pub.publish(servo_msg);
    }
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "main_subscriber");
  ros::NodeHandle n;

  sub = n.subscribe("voice", 1000, voiceCallback);
  servo_pub = n.advertise<std_msgs::String>("servo_control", 1000);
  
  ros::spin();

  return 0;
}