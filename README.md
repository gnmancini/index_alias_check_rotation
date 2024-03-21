# index_alias_check_rotation
Python script to check if the index did not rotate within a specific time

# Scenario:
If you are using elasticsearch or opensearch and you use aliases as a virtual pointer, having several per index and rotating them every 24 hours for example, sometimes the rotation gets stuck increasing the size of the alias.
The script checks the alias rotation and shows you a popup if you are using a linux operating system.

# Important:
Use this script at your own risk. 