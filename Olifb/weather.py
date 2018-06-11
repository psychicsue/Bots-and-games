import pyowm

class Weather:
    def __init__(self, gpe=None, cord=None):
        self.__api_key = '61eaa93d4afd86d636c1fee95daa2110'
        self.__owm = pyowm.OWM(self.__api_key)
        if cord is None:
            reg = self.__owm.city_id_registry()
            if reg.ids_for(gpe):
                self.__observation = self.__owm.weather_at_place(gpe)
        elif gpe is None:
            obser_lst = self.__owm.weather_around_coords(cord[0], cord[1])
            self.__observation = obser_lst[0]

        self.__w = self.__observation.get_weather()
        self.__city = gpe

    def get_humidity(self):
        return self.__w.get_humidity()

    def get_max_temp(self):
        temp_max = self.__w.get_temperature('celsius')
        return temp_max['temp_max']

    def get_min_temp(self):
        temp_min = self.__w.get_temperature('celsius')
        return temp_min['temp_min']

    def get_temp(self):
        temp = self.__w.get_temperature('celsius')
        return temp['temp']

    def get_wind_speed(self):
        return self.__w.get_wind()["speed"]

    def get_city(self):
        return self.__city

    def get_status(self):
        return self.__w.get_status()