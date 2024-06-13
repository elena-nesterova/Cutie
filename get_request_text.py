import get_request

class get_request_text(get_request.get_request):

    def get_request(self):
        return input("Waiting for text: ")
