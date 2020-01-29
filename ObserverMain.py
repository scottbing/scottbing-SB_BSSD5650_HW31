from WeatherData import *


class WeatherTower(Subject):
    # overriding Subject method
    def getUserAction(self):
        prompt = "Enter Pressure, Temperature, and Wind Direction separated by commas:"
        self.data = input(prompt)
        return self.data
# end of class WeatherTower(Subject):


if __name__ == "__main__":
    subject = WeatherTower()

    listenerP = PressureListener("<Press>", subject)
    listenerT = TemperatureListener("<Temp>", subject)
    ListenerW = WindListener("<Wind>", subject)

    action = subject.getUserAction()
    subject.notify_listeners(action)