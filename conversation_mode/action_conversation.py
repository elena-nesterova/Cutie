import random

import action

class action_conversation(action.action):

    def __init__(self, conversation):
        self.__conversation = conversation

    def get_language(self):
        return self.__conversation.get_language()

    def get_answer_type_flags(self):
        return self.__conversation.get_answer_type_flags()

    def process_action(self, request):

        # go through dialogs
        for dialog in self.__conversation.get_dialogs():

            # dialog - requests
            dialog_requests = dialog[0]

            # check only dialog with request
            if len(dialog_requests) != 0:

                # go through dialog - requests
                for dialog_request in dialog_requests:

                    # search our request in dialog-requests
                    if dialog_request in request:
                        return random.choice(dialog[1])

        dialog = self.__conversation.get_dialogs()[0]
        # if didn't find request, give any reaction from 0 dialog
        return random.choice(dialog[1])

    def restart(self):
        pass

    def is_finished(self):
        return True

    def say_smth(self):
        dialog = self.__conversation.get_dialogs()[0]
        # give any reaction from 0 dialog
        return random.choice(dialog[1])

    # return ready_to_listen answer
    def ready_to_listen(self):
        return random.choice(self.__conversation.get_ready_to_listen_messages())
