class Subject:

    def __init__(self):
        self._observers=set()

    def add_observer(self,observer):
        self._observers.add(observer)
    
    def remove_observer(self,observer):
        self._observers.remove(observer)

    def sync_notify(self,message=""):
        x.notify(message) for x in self._observers
    


