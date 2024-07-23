class UserRequest:

    def __init__(self, username=None, password=None, fl_REQ=None):
        self.username = username
        self.password = password
        self.flreq = fl_REQ
        if fl_REQ is not None:
            self.getJSONRequest()

    def getJSONRequest(self):
        data = self.flreq
        self.username = data["username"]
        self.password = data["password"]
