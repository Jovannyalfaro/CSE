world_map = {
    'R19A': {
        'NAME': "Mr. Wiebe's Room",
        'DESCRIPTION': "This is the classroom you are in right now. "
                       "NOW, there are two doors on the north wall.",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "The North Parking Lot",
        'DESCRIPTION': "There are couple cars parked here.",
        'PATHS': {
            'SOUTH': 'R19A'
        }
    }
}

# controller
playing = True
current_node = world_map['R19A']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit' , 'exit']:
        playing = False
    elif command.upper() in directions:
        try:




# Other Notes
states["AR"] = "Arizona?" # It isn't Arizona

states['AR'] = "Arkansas" # Fixed it.
print(states['AR'])
