# I want to create a game where a person travels through rooms
# dealing with others, their past, their future, and finally acceptance.
# acceptence of themselves and others is how they win
# the rooms are "scenes" and behind every scene is a game "engine"
# that takes the user to various rooms
# the death scene will tell different jokes

from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("Will this be included in all the subclasses?")
        exit(1)
        

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # when play initially runs, the current scne is the first scene
        current_scene = self.scene_map.opening_scene()
        # why is 'finished' here? What does it do?
        # so it's the last scene, so the next_scene would
        # finish the game
        last_scene = self.scene_map.next_scene('finished')

        # this while loop is going to loop back on itself
        # until the game is over 
        # the game is over when current_scene = last_scene
        # but it starts and continues as long as the current_scene
        # != last_scene or when in Death, the exit() function
        while current_scene != last_scene:
            # so current scene needs to have some function
            # that is enter()
            next_scene_name = current_scene.enter()
            # so self, as defined above has an attribute scene_map
            # so, the function next_scene is called on self.scene_map
            current_scene = self.scene_map.next_scene(next_scene_name)
        # I think we're calling enter() on the variable current_scene
        current_scene.enter()

class Death(Scene):
    # when the player dies, random jokes will appear
    death_jokes = [
        """Let's cheer up your death with a joke: 
        The Man Who Created Autocorrect Has Died. Resturant In Peace.""",
        """Let's cheer up your death with a joke: 
        I hope when I inevitably choke to death on gummy bears
        people just say I was killed by bears and leave it at that.""",
        """Let's cheer up your death with a joke: 
        How is it that I always seem to buy the plants 
        without the will to live?""",
        """Let's cheer up your death with a joke: 
        I always feel better when my doctor says something is normal for my age 
        but then think dying will also be normal for my age at some point.""",
        """Let's cheer up your death with a joke: 
        I would request a last meal of soda and pop rocks 
        so I could die on my own terms."""
    ]
    
    # so, I think this will print a random joke from the list above
    # whenever a play enters into death? I'm not sure
    def enter(self):
        print(Death.death_jokes[randint(0, len(self.death_jokes))])
        exit(1)


class Others(Scene):

 def enter(self):

    print(dedent(f""" 
    Welcome, {name}. You have fallen asleep and now you find youself
    in a large room full of beautiful people. It might be located in LA
    but you never know. Anyways, it makes you nervous but you don't 
    know how to respond. The responses come to mind:
    - get in a cat fight
    - mess up a beautiful girl's makeup
    - give a hug to every person there
    What do you choose?
    """))

    action = input("> ")

    if 'fight' in action:
        print(dedent("""
        You were too weak for a cat fight. You die out of embarassment
        """))
        return 'death'
    elif 'mess' in action or 'makeup' in action:
        print("That girl messes up your makeup. You die of embarassment")
        return 'death'
    elif 'hug' in action:
        print(dedent("""
        Through the hug, you show you accept others.
        even if you are intimidated of them.
        """))
        return 'glass_ball'
    else:
        print("That's not an option. Let's try this again.\n")
        return 'others'

class GlassBall(Scene):

    def enter(self):
        print(dedent(""" 
        You find yourself in a room that is completely empty and dark except
        for a lit glass ball in the center of the room. You have heard about
        this glass ball in the past. Whatever it tells you is your future
        becomes true. You have 5 guesses to speak the right number for it to
        tell you a favorable future. If you guess wrong, well, let's just say
        don't find out. Type any number 1-9. 
        """))

        code = randint(1, 9)
        print(code)
        guess = int(input("> "))
        guesses = 0
        # there was a bug because guesses starts at 0, not at 1
        while guess != code and guesses < 4:
            print("That's not the right number!")
            guesses += 1
            guess = input("> ")

        if guess == code:
            print(dedent("""
            That was the right number! The glass ball says something mysterious.
            It says, "accept". You brush it off, the glass ball doesn't really 
            determine your future...or does it?
            """))
            return 'memory_weapons'
        else:
            print(dedent("""
            Your five guesses ran out.
            The glass ball tells you 'watch out'. Then you see it! A giant glass ball 
            comes rolling and crushes you.
            """))
            return 'death'

class MemoryWeapons(Scene):
    
    def enter(self):
        print(dedent("""
        Poof! You find yourself in a road lane. Along the lane you see a road sign
        that reads "Go down and down you'll realize you're along memory lane. This
        memory lane brings up every embarassing memory you've ever had. How do you
        want to get rid of these memories?" Below the sign is a bomb, a gun, and 
        a photo album. Which 'weapon' do you pick up?
        """))
        # I want weapon to apply to the Memory class
        global weapon
        weapon = input("> ")
        # the user has a choice of weapon
        if 'bomb' in weapon or 'gun' in weapon or 'photo album' in weapon:
            print(dedent("""
            *ripple ripple*
            """))
            return 'memory'
        else:
            print(dedent(f"""
            Unacceptable!!! No, don't you dare move forward with {weapon}
            Try another weapon
            """))
            return 'memory_weapons'
# I don't know if this is going to work
# but I want the variable weapon from Memory Weapons to apply here
# does a class inherit a higher class's variables?
# let's see...
class Memory(MemoryWeapons):

    def enter(self):
        print(dedent("""
        Poof again! You in a long hallway with pictures, upon pictures, upon pictures
        of embarassing memories. Do you want to change your weapon of choice?
        """))
        # do you want to change weapons to keep them?
        change = input("> ")

        if 'no' in change:

            if 'bomb' in weapon or 'gun' in weapon:
                print(dedent(f"""
                Gasp! The pictures of embarrasing memories were contained in an explosive
                proof glass. The {weapon} kills you instead.
                """))
                return 'death'

            elif 'photo album' in weapon:
                photo_reaction = randint(0, 10)
                print(">>>> photo_reaction = ", photo_reaction)

                if photo_reaction > 5: 
                    print(dedent("""
                    Oh no! The photos continue to laugh at you as you put them inside the
                    photo album. How do you shut them up?
                    """))

                    shut_up = input("> ")

                    if "yell" in shut_up:
                        photo_reaction = randint(0, 10)
                        print(">>>> photo_reaction = ", photo_reaction)

                        if photo_reaction <= 5:
                            print(dedent("""
                            You've shown that you accept your embarassing memories by placing them in
                            a photo album that will never be opened again because who looks at hand-held
                            photo albums anymore?
                            """))
                            return 'acceptence'

                        elif photo_reaction > 5:
                            print(dedent("""
                            The photos continue to laugh at you. You die of embarassment. 
                            """))
                            return 'death'

                    else:
                        print(dedent("""
                        The photos continue to laugh at you. You die of embarassment. 
                        """))
                        return 'death'

                
                elif photo_reaction <= 5: 
                    print(dedent("""
                    You've shown that you accept your embarassing memories by placing them in
                    a photo album that will never be opened again because who looks at hand-held
                    photo albums anymore?
                    """))
                    return 'acceptence'

            else:
                print(dedent("""
                Oops, that's not possible. Let's try this again...
                *ripple ripple*
                """)) 
                return 'memory'

        elif 'yes' in change:
            print(dedent("""
            *ripple ripple*
            """))
            return 'memory_weapons'

        else:
            print(dedent("""
            Oops, that's not possible. Let's try this again...
            *ripple ripple*
            """)) 
            return 'memory'

class Acceptence(Scene):
    
    def enter(self):
        # mirror 1-5
        # which is the correct mirror?
        # one of them shows your true self

        print(dedent("""
        Woooooooshhhhhh!
        After you catch your breath and balance, you find yourself face to face in a house
        of mirrors. Four of the five mirrors disotort your apperance to something fataly 
        ugly. You have one guess...
        """))

        good_mirror = randint(1, 5)
        print(good_mirror)
        guess = input("[mirror #]> ")

        try: 
            if int(guess) != good_mirror:
                print(dedent(f"""
                You catch of glisp of yourself in mirror {guess} and die of horror.
                """))
                return 'death'
            else:
                print(dedent("""
                Well done. 
                """))
                return 'finished'
        except:
            print("\nThat wasn't a mirror choice. Let's try this again.\n")
            return 'acceptence'

class Finished(Scene):

    def enter(self):
        print(dedent("""
        You have shown that you accept others, the past, and the future.
        """))
        return 'finished'

class Map(object):

    scenes = {
        'others': Others(), 
        'glass_ball': GlassBall(), 
        'memory_weapons': MemoryWeapons(), 
        'memory': Memory(), 
        'acceptence': Acceptence(), 
        'finished': Finished(), 
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('others')
a_game = Engine(a_map)
print("Hi, what is your name?")
global name
name = input("> ")
a_game.play()