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

class conversation2Ru(conversation.conversation):

    __lang = cuty_communication_types.beast_language.ru
    __conv_type = (cuty_communication_types.beast_answer_type_flags.text &
                   cuty_communication_types.beast_answer_type_flags.text_to_speech)

    __dialogs = [
        [
            [],
            [
                "бла-бла-бла",
                "ты мне уже надоел",
                "отстань",
                "в советские времена тагого безобразия не было",
                "ох, была я молодая",
                "брысь, коты",
                "Иди отсюда"
            ]
        ],
        [
            [
                "привет",
                "здравствуй",
                "добрый день"
            ],
            [
                "Ну привет, лапусик",
                "чё надо?"
            ]
        ],
        [
            [
                "милашка"
            ],
            [
                "да, я милашка, чего тебе?",
                "а ты кто? вообще нет, мне не интересно"
            ]
        ],
        [
            [
                "рокси"
            ],
            [
                "рокси шмокси колбаса, на веревочке оса",
                "эта рокси всегда ворует мою еду!"
            ]
        ],
        [
            [
                "твикс"
            ],
            [
                "найдите уже у него кнопку выключения",
                "ААААААА! Уберите его!"
            ]
        ]
    ]

    __ready_to_listen_messages = [
        "Слушаю",
        "Ну говори уже",
        "Ой"
    ]

    def get_dialogs(self):
        return self.__dialogs

    def get_ready_to_listen_messages(self):
        return self.__ready_to_listen_messages

    def get_language(self):
        return self.__lang

    def get_answer_type_flags(self):
        return self.__conv_type
