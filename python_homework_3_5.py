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
            curr = trip.split(" ")[2].strip()
            print(destination, round(cl.service.ConvertToNum(
                fromCurrency=curr,
                toCurrency="RUB",
                rounding=False,
                amount=cost
            )), "RUB")


def convert_distance(dist):
    cl = osa.Client("http://www.webservicex.net/length.asmx?WSDL")
    total_distance = 0
    with open(dist, encoding="utf-8") as f:
        for trip in f:
            destination = trip.split(" ")[0]
            distance = trip.split(" ")[1]
            measure = trip.split(" ")[2].strip()
            print(destination)
            print(type(destination))
            print(distance)
            print(type(distance))
            print(measure)
            print(type(measure))
            trip_distance = cl.service.ChangeLengthUnit(
                LengthValue=str(distance),
                fromLengthUnit="Miles",
                toLengthUnit="Kilometers",
            )
            print(trip_distance)
            total_distance += trip_distance
    print(total_distance)


if __name__ == "__main__":
    # convert_temp("temps.txt")
    # currency("currencies.txt")
    convert_distance("travel.txt")