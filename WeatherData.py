from Observer import *


class PressureListener(AbstractListener):
    _pressure = 0   # static variable

    def notify(self, event):
        val = event.split(',')[0]
        if val != PressureListener._pressure:
            print(self.name, "Current Barometric Pressure is", val, "atms.")
            PressureListener._pressure = val
# end class PressureListener(AbstractListener):


class TemperatureListener(AbstractListener):
    _temperature = 0    # static variable

    def notify(self, event):
        val = event.split(',')[1]
        if val != TemperatureListener._temperature:
            print(self.name, "Current Temperature is ", val, " degrees F.")
            TemperatureListener._temperature = val
# end class TemperatureListener(AbstractListener):


class WindListener(AbstractListener):
    _wind = None   # static variable

    def notify(self, event):
        val = event.split(',')[2]
        if val != WindListener._wind:
            print(self.name, "Current Wind Direction is from the", val.capitalize())
            WindListener._wind = val
# end class WindListener(AbstractListener):
