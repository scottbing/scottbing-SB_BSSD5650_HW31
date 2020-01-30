from Observer import *
import pickle

# NOT MY CODE
# takenfrom:
# https://stackoverflow.com/questions/26835477/pickle-load-variable-if-exists-or-create-and-save-it
# Wednesday, 01/29/2020
# Scott Bing
#
# prime the pickle file first time
def read_or_new_pickle(path, default):
    try:
        with open(path, "rb") as f:
            foo = pickle.load(f)
    except Exception:
        foo = default
        with open(path, "wb") as f:
            pickle.dump(foo, f)
    return foo

# prime the three sensor files
#read_or_new_pickle(path="pressure.dat", default=0)
#read_or_new_pickle(path="temperature.dat", default=0)
#read_or_new_pickle(path="wind.dat", default=0)


class PressureListener(AbstractListener):
    _pressure = 0    # static variable
    #read_or_new_pickle(path="pressure.dat", default=0)

    def notify(self, event):
        val = event.split(',')[0]
        PressureListener._pressure = pickle.load(open("pressure.dat", "rb"))
        # print("PressureListener._pressure = ", PressureListener._pressure)
        # print("val = ", val)
        if val != PressureListener._pressure:
            print(self.name, "Current Barometric Pressure is", val, "atms.")
            pickle.dump(val, open("pressure.dat", "wb"))


# end class PressureListener(AbstractListener):


class TemperatureListener(AbstractListener):
    _temperature = 0  # static variable
    #read_or_new_pickle(path="temperature.dat", default=0)

    def notify(self, event):
        val = event.split(',')[1]
        TemperatureListener._temperature = pickle.load(open("temperature.dat", "rb"))
        # print("TemperatureListener._temperature = ", TemperatureListener._temperature)
        # print("val = ", val)
        if val != TemperatureListener._temperature:
            print(self.name, "Current Temperature is ", val, " degrees F.")
            pickle.dump(val, open("temperature.dat", "wb"))


# end class TemperatureListener(AbstractListener):


class WindListener(AbstractListener):
    _wind = 0  # static variable
    #read_or_new_pickle(path="wind.dat", default=0)

    def notify(self, event):
        val = event.split(',')[2]
        WindListener._wind = pickle.load(open("wind.dat", "rb"))
        # print("WindListener._wind = ", WindListener._wind)
        # print("val = ", val)
        if val != WindListener._wind:
            print(self.name, "Current Wind Direction is from the", val.capitalize())
            pickle.dump(val, open("wind.dat", "wb"))


# end class WindListener(AbstractListener):
