from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "You died.  I hope this was an intereting story about myself.",
        "You died. Unfortunately this is where the story ends, boring right?",
        "You died. Such a luser. Talking about me, durr! Wait...Huh.",
        "You died. Please give me the job :) !!"
        "You died. If you wish to contact me please email me, which was provided to you in my CV. Just note that you should rerun the game to find out more about me. I also posted the code for this on my github at https://github.com/hect1c/mystory. Thank you."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class HartleyStory(Scene):

    def enter(self):
        print "The story of what makes Hartley Jean-Aimee unique, written on June 15 2016 at 6:23 pm while watching the Romania vs Switzerland Euro game in Python.\n"
        print "Well, where to begin, let's start with the fact that he is an American, born in French Guiana, residing currently in London. I know not really that interesting. Then we tie into the fact, that he has 3 first names. You don't see it, let me show:\n"
        print "Hartley - Actually a common English last name but obviously my first name, oh the irony.\n"
        print "Jean - Very common first name Jean of Arc, Jean-Claude Van Damme, ok either way it's technically a first name.\n"
        print "Aimee - Well in french it means to love, but again common first name.\n"
        print "OK how about maybe when Gears 2 game out (yes I am a HUGE Gears of War fan) my brother, and best friend joined a Lan Tournament and came in 3rd place. I am a sniper pro, headshot galore. Oh the good times.\n"
        print "Do you want to know more? (options: yes, no, joke)"

        action = raw_input("> ")

        if action == "yes":
            print "Wow I can't believe you said yes. What a sorry sap, feel bad for you."
            print "Who forced you to have to learn more about me."
            print "Let's see, I am very good at reading people with only a breif meeting."
            print "Futhermore I can use this skill to understand where and how to support people even when they don't see it. Friends, Family, Coworkers."
            print "Huge Anime fan, probably my favorite one is currently One Piece. Amazing. I love to draw, and I've probably seen every TV show out there within my favorite Genres of course. I don't know how but I manage to find time to watch TONS of tv shows. Thanks for trying to find out more about me, hope you enjoyed it."
            return 'finished'

        elif action == "no":
            print "\nWell you said no, which frankly hurts a bit. But I'm going to forgive you and assume that's a good thing"
            print "I hope the story the intro was good some useful basic information about me. Can't give everything away a bit of mystery is good."
            print "I had some fun quickly writing this script. Thanks for that."
            print "But since you said no, but I'm sorry but you must die !!!!"
            return 'death'

        elif action == "joke":
            print "You want to hear a joke eh:"
            print "Well I'm not very funny but here goes"
            print "A plane full of crazy people is in the air. One guy goes in to the cockpit and asks the pilot to teach him how to fly. The pilot says if you can get everyone back there quiet I will teach you. A few minutes later the guy comes back and said they are quite now. The pilot asked how did you get them quiet, the guy says, I just told them all to go play outside."
            print "Since you didn't say yes you still must die !!"
            return 'death'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

class Finished(Scene):

    def enter(self):
        print "You know a lot about me! Good job."
        print "If you wish to contact me please email me, which was provided to you in my CV. Thank you."
        print "I also posted the code for this on my github at https://github.com/hect1c/mystory"
        return 'finished'

class Map(object):

    scenes = {
        'hartley_story': HartleyStory(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('hartley_story')
a_game = Engine(a_map)
a_game.play()
