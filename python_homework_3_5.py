import osa
import os


def convert_temp(temp):
    cl = osa.Client("http://www.webservicex.net/ConvertTemperature.asmx?WSDL")
    with open(temp, encoding="utf-8") as f:
        for fahrenheit in f:
            temp = fahrenheit.strip(" \nF")
            print("Температура по Фаренгейту: {}, температура по Цельсию: {}".format(temp, round(cl.service.ConvertTemp(
                Temperature=temp,
                FromUnit="degreeFahrenheit",
                ToUnit="degreeCelsius"
            ))))


def currency(currencies):
    cl = osa.Client("http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL")
    with open(currencies, encoding="utf-8") as f:
        for trip in f:
            destination = trip.split(" ")[0]
            cost = trip.split(" ")[1]
            curr = trip.split(" ")[2]
            print(destination, (cl.service.ConvertToStr(
                fromCurrency=curr,
                toCurrency="RUB",
                round=True,
                amount=cost
            )))


if __name__ == "__main__":
    # convert_temp("temps.txt")
    currency("currencies.txt")