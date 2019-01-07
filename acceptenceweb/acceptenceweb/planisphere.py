class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)
        
    def add_paths(self, paths):
        self.paths.update(paths)

others = Room("Room of Others",
""" 
Welcome. You have fallen asleep and now you find youself
in a large room full of beautiful people. It might be located in LA
but you never know. Anyways, it makes you nervous but you don't 
know how to respond. The responses come to mind:
    - get in a cat fight
    - mess up a beautiful girl's makeup
    - give a hug to every person there
What do you choose?
""")

glass_ball = Room("The Room with the Glass Ball",
""" 
You find yourself in a room that is completely empty and dark except
for a lit glass ball in the center of the room. You have heard about
this glass ball in the past. Whatever it tells you is your future
becomes true. You have 5 guesses to speak the right number for it to
tell you a favorable future. If you guess wrong, well, let's just say
don't find out. Type any number 1-9. 
""")

memory_weapons = Room("Room of Memory Weapons",
"""
Poof! You find yourself in a road lane. Along the lane you see a road sign
that reads "Go down and down you'll realize you're along memory lane. This
memory lane brings up every embarassing memory you've ever had. How do you
want to get rid of these memories?" Below the sign is a bomb, a gun, and 
a photo album. Which 'weapon' do you pick up?
""")

memory = Room("Room of Embarassing Memories",
# I had to get rid of the player's ability to change their
# weapons, I might need to go back
"""
Poof again! You in a long hallway with pictures, upon pictures, upon pictures
of embarassing memories. The photos are laughing at you. How do you get them
to shut up?
""")

mirror_room = Room("Room of Present Acceptence",
"""
Woooooooshhhhhh!
After you catch your breath and balance, you find yourself face to face in a house
of mirrors. Four of the five mirrors disotort your apperance to something fataly 
ugly. You have one guess...
""")

the_end_winner = Room("The End",
"""
You have shown that you accept others, the past, and the future.
""")

the_end_loser = Room("The End",
"""
You never learned to accept others, the past, present, and the
the future. You die of embarassment.
""")

mirror_room.add_paths({
    '3': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "You died.")

memory.add_paths({
    # I get rid of the combat system and the ability
    # to change your weapon here, I need to go back
    'yell': generic_death,
    'put them in photo album': mirror_room,
    '*': generic_death
})

memory_weapons.add_paths({
    'bomb': generic_death,
    'gun': generic_death,
    'photo album': memory,
    '*': generic_death
})

glass_ball.add_paths({
    '4': memory_weapons,
    '*': generic_death
})

others.add_paths({
    'fight': generic_death,
    'mess': generic_death,
    'hug': glass_ball,
    '*': generic_death
})

START = 'others'

# what are these for?
def load_room(name):
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key