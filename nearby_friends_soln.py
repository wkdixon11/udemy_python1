#!/usr/bin/env python

nearby_people = {"Rolf", "Jen", "Anna"}
user_friends = set()  # This is an empty set, like {}
 
friend = input("Enter your friend name to see if he is nearby: ")
 
# Add the friend to the user_friends set
user_friends.add(friend)
 
# Print out the friends that are nearby... those which are in both sets!
print(user_friends.intersection(nearby_people))
