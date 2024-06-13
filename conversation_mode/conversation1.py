from conversation_mode import conversation
import cuty_communication_types

'''
[   [   [inputs ], [outputs] ], [   [inputs ], [outputs] ], ...]
[dialogs                                                       ]
[   [dialog 1                ], [dialog 2                ], ...]

dialogs                         [[[ ], [ ]], [[ ], [ ]], ...]
|
|___dialog 1                    [[   *    ], [[ ], [ ]], ...]
|   |
|   |___inputs for dialog 1     [[[*], [ ]], [[ ], [ ]], ...]
|   |   |___input 1
|   |   |___input 2
|   |   |___...
|   |
|   |___outputs for dialog 1    [[[ ], [*]], [[ ], [ ]], ...]
|       |___output 1
|       |___output 2
|       |___...
|
|___dialog 2                    [[[ ], [ ]], [   *    ], ...]
|   |
|   |___...
|
|___...       
'''

class conversation1(conversation.conversation):

    __lang = cuty_communication_types.beast_language.nl
    __conv_type = (cuty_communication_types.beast_answer_type_flags.text &
                   cuty_communication_types.beast_answer_type_flags.text_to_speech)

    __dialogs = [
        [
            [],
            [
                "bla-bla-bla",
                "Hou je mond"
            ]
        ],
        [
            [
                "hi",
                "hello",
                "hoi"
            ],
            [
                "Hello, schatje",
                "ga weg!"
            ]
        ],
        [
            [
                "cuty"
            ],
            [
                "Ja, ik ben Cuty, wat wil je?",
                "Wie ben je? Nee, het is niet interessant"
            ]
        ]
    ]

    __ready_to_listen_messages = [
        "Zeg, schaatje",
        "Oh"
    ]

    def get_dialogs(self):
        return self.__dialogs

    def get_ready_to_listen_messages(self):
        return self.__ready_to_listen_messages

    def get_language(self):
        return self.__lang

    def get_answer_type_flags(self):
        return self.__conv_type
