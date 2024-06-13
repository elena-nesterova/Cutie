import random
from playsound import playsound
import give_reaction

class _give_reaction_audio(give_reaction.give_reaction):

    def give_reaction(self, source):
        try:
            playsound(source)
        except Exception as ex:
            print("Error playsound (" + source + ")")


def give_reaction_random(reactions):
    try:
        playsound(random.choice(reactions))
    except Exception as ex:
        print("Error playsound")

def give_reaction_f(reactions, index):
    try:
        if index < len(reactions):
            playsound(reactions[index])
        else:
            playsound(random.choice(reactions))
    except:
        print("Error playsound")

