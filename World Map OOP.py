class Room(object):
    def __init__(self, name, description, north=None, south=None, east=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = descripiton
        self.characters = []




class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []

    def move(self, new_location):
        """This moves the player to a new room

        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location


def find_next_room(direction):
    """ This method searches the current room so see if a room exists in that direction.

    :param direction: The direction that you want to move to
    :return: The room object if it exists, or None if it does not exist
    """
    return getattr(self.current_location, direction)
    return globals()[name_of_room]


R19A = Room("Mr. Wiebe's Room", 'Parking_lot')
parking_lot = Room("Parking lot", )



