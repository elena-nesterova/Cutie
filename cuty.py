from threading import Thread, Lock
from time import sleep
from py122u import nfc

class cuty:

    def __init__(self, action, get_request, give_reaction, interval_sec=20):

        self.__started = False
        self.__stop_requested = False
        self.__thread_work = False

        self.__lock_busy = Lock()

        self.__action = action
        #self.__lang = action.get_language()
        self.__get_request = get_request
        self.__give_reaction = give_reaction

        self.__interval_sec = interval_sec

    def started(self):
        return self.__started

    def __say_smth_periodically(self, name):

        self.__thread_work = True

        while not self.__stop_requested:

            if not self.__lock_busy.locked():
                # perform the task
                with self.__lock_busy:
                    self.say_smth()

            # block for the interval
            sleep(self.__interval_sec)

        self.__thread_work = False
        self.__started = False

    def __listen_by_timer(self, name):

        while not self.__stop_requested:

            print('Listening!')
            with self.__lock_busy:
                self.__say(self.__action.process_action(self.__listen().lower()))

            sleep(self.__interval_sec)

    def __nfc_waiter(self, name):

        reader = nfc.Reader()

        card_exists = False

        while not self.__stop_requested:

            try:
                reader.connect()
                reader.mute_buzzer()

                if not card_exists:
                    card_exists = True
                    #  print('Card connected!')
                    card_id = reader.get_uid()
                    # print(reader.get_uid())
                    if card_id == [201, 230, 84, 124]:
                        print('Restart!')
                        self.__action.restart()
                    elif card_id == [217, 85, 250, 124]:
                        print('Off!')
                        self.__stop_requested = True
                    else:
                        print('Listening!')
                        with self.__lock_busy:
                            self.__say(self.__action.process_action(self.__listen().lower()))

            except:
                if card_exists:
                    card_exists = False
                #            print('Card disconnected!')

            sleep(0.2)
    @property
    def __check_nfc(self):
        return True
        try:

            reader = nfc.Reader()
            reader.connect()
        except:
            return False

        return True

    def start(self):
        self.__started = True
        daemon = Thread(target=self.__say_smth_periodically, args=(self,), daemon=True, name='Background')
        daemon.start()

        if self.__check_nfc:
            print("Found nfc-reader")
            daemon_listen = Thread(target=self.__nfc_waiter, args=(self,), daemon=True, name='BackgroundNFC')

        else:
            print("No Nfc")
            daemon_listen = Thread(target=self.__listen_by_timer, args=(self,), daemon=True, name='BackgroundListen')

        daemon_listen.start()

    def stop(self):
        self.__stop_requested = True

    def say_smth(self):
        self.__say(self.__action.say_smth())

    def __say(self, source):
        self.__give_reaction.give_reaction(source)

    def __listen(self):
        self.__say(self.__action.ready_to_listen())
        return self.__get_request.get_request()
