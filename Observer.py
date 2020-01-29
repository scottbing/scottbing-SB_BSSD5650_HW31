###################################################
# Boiler plate code taken from wikibooks
# https://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Observer
# on /01/28/2020
# available under the Creative Commons Attribution-ShareALike License
# https://creativecommons.org/licenses/by-sa/3.0/
# Modified by Scott Bing
#
# Changelog:
# - modified input command to Python3 version
# - modified print command to Python3 version
# - abstracted listener class and notify method
# - ISSUE: Listener call in main test no longer works
#


class AbstractSubject:
    def register(self, listener):
        raise NotImplementedError("Must subclass me")

    def unregister(self, listener):
        raise NotImplementedError("Must subclass me")

    def notify_listeners(self, event, temperature):
        raise NotImplementedError("Must subclass me")


class AbstractListener:
    # class Listener
    def __init__(self, name, subject):
        self.name = name
        subject.register(self)

    def notify(self, event):
        # print(self.name, "received event", event)
        raise NotImplementedError("Must subclass me")


class Subject(AbstractSubject):
    def __init__(self):
        self.listeners = []
        self.data = None

    def getUserAction(self):
        self.data = input('Enter something to do:')
        return self.data

    # Implement abstract Class AbstractSubject

    def register(self, listener):
        self.listeners.append(listener)

    def unregister(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self, event):
        for listener in self.listeners:
            listener.notify(event)


if __name__ == "__main__":
    # make a subject object to spy on
    subject = Subject()

    # register two listeners to monitor it.
    listenerA = Listener("<listener A>", subject)
    listenerB = Listener("<listener B>", subject)

    # simulated event
    subject.notify_listeners("<event 1>")
    # outputs:
    #     <listener A> received event <event 1>
    #     <listener B> received event <event 1>

    action = subject.getUserAction()
    subject.notify_listeners(action)
    # Enter something to do:hello
    # outputs:
    #     <listener A> received event hello
    #     <listener B> received event hello
