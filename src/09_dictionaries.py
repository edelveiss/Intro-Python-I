# """
# Dictionaries are Python's implementation of associative arrays.
# There's not much different with Python's version compared to what
# you'll find in other languages (though you can also initialize and
# populate dictionaries using comprehensions just like you can with
# lists!).

# The docs can be found here:
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# For this exercise, you have a list of dictionaries. Each dictionary
# has the following keys:
#  - lat: a signed integer representing a latitude value
#  - lon: a signed integer representing a longitude value
#  - name: a name string for this location
# """

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({
        "lat": 44,
        "lon": -124,
        "name": "a forth place"})
print(waypoints)

# # Modify the dictionary with name "a place" such that its longitude
# # value is -130 and change its name to "not a real place"
# # Note: It's okay to access the dictionary using bracket notation on the
# # waypoints list.

# # YOUR CODE HERE

for k in range(len(waypoints)):
    if waypoints[k]["name"] == "a place":
        waypoints[k]["name"] = "not a real place"
        waypoints[k]["lon"]= -130

print(waypoints)

# # Write a loop that prints out all the field values for all the waypoints
# # YOUR CODE HERE
print("----enumerate-----")
for key, values in enumerate(waypoints):
    print(values)
print("----[print(v) for k,v in i.items()]-----")
for  i in waypoints:
    [print(v) for k,v in i.items()]
    
print("----print(i.values())-----")
for i in waypoints:
    print(i.values())
    
print("----print(', '.join(f'' for k, v in way.items()))-----")
for way in waypoints:
    print(', '.join(f'{k}: {v}' for k, v in way.items()))



