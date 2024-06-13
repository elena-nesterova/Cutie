from time import sleep

import cutie
from conversation_mode.action_conversation import action_conversation
from conversation_mode.conversation2Ru import conversation2Ru
from get_request_text import get_request_text
from give_reaction_text import give_reaction_text

# conversation ru text
action = action_conversation(conversation2Ru())
get_request = get_request_text()
give_reaction = give_reaction_text()

'''
# conversation nl text to speech
action = action_conversation(conversation2Ru())
get_request = get_request_speech_to_text(action.get_language())
give_reaction = give_reaction_text_to_speech(action.get_language())
'''

bibi = cutie.cutie(action, get_request, give_reaction, 10)

bibi.start()

while True:
    sleep(10)

    if not bibi.started():
        break
