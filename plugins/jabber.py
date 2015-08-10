import xmpp

class JabberClientNotFoundException(Exception):
    pass

class JabberAuthException(Exception):
    pass

class JabberClient:

    client = None
    channel = None

    def __init__(self, username, password, server, channel, port=5222, debug=[]):
        self.username = username
        self.password = password
        self.channel = channel
        self.client = xmpp.Client(server=server, port=port, debug=debug)

    def send(self, message):
        message = xmpp.Message(self.channel, message)
        self.client.send(message)

    def __enter__(self):
        if not self.client:
            raise JabberClientNotFoundException()
        self.client.connect()
        try:
            self.client.auth(self.username, self.password)
        except:
            raise JabberAuthException()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
