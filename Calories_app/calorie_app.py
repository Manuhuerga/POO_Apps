from scrapping import Temperature
from calorie_calculator import Calorie


if __name__ == '__main__':

    weight = int(input('Please input your weigth: '))
    height = int(input('Input your height: '))
    age = int(input('Your age is: '))

    country = str(input('What is your country?: '))
    city = str(input('and your city?: '))

    t = Temperature(country,city)
    c = Calorie(weight,height,age,33)

    print(f"your body need {c.calculate()} calories")
