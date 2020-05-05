#!/usr/bin/env python
import rospy
from my_services.srv import WordCount
import sys

rospy.init_node('service_client')

rospy.wait_for_service('word_count') # wait for registration
word_counter = rospy.ServiceProxy( # set up proxy
  'word_count', # service name
  WordCount     # service type
)
words_list_pass_1=[k for k in sys.argv if 'service_client.py' not in k]
words_list_pass_2=[k for k in words_list if '__' not in k]
words = ' '.join(words_list_pass_2) # parse args
word_count = word_counter(words) # use service

print(words+'--> has '+str(word_count.count)+' words')
print(words_list)
