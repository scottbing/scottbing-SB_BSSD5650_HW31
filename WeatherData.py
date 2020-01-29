from Observer import *


class PressureListener(AbstractListener):


    def notify(self, event):
        val = event.split(',')[0]
        print(self.name, "Current Barometric Pressure is", val, "atms.")
# end class PressureListener(AbstractListener):


class TemperatureListener(AbstractListener):
    def __init__(self, temperature=0):
        self.temperature = temperature

    def notify(self, event):
        val = event.split(',')[1]
        # save old temperature value
        self.temperature = val
        if self.temperature == val:
            print(self.name, "Current Temperature is ", self.temperature, " degrees F.")
        else:
            print(self.name, "Current Temperature is ", val, " degrees F.")
# end class TemperatureListener(AbstractListener):


class WindListener(AbstractListener):
    def notify(self, event):
        val = event.split(',')[2]
        print(self.name, "Current Wind Direction is from the", val.capitalize())
# end class WindListener(AbstractListener):
