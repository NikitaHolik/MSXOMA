import random
import time
#job, car, home, name, gladness
class Human:
    def __init__(self, name="Human", job = None, home = None, car = None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car

        self.gladness = 15
        self.money = 100
        self.satiety = 50

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
        self.job = Job(job_list)


    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
            self.satiety += 5
            self.home.food -= 5

    def shopping(self, manage):
        if not self.car.drive:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
        if manage == 'fuel':
            print("I bought fuel!")
            self.car.fuel += 100
            self.money -= 100
        elif manage == 'food':
            print('I bought food!')
            self.home.food += 50
            self.money -= 50
        elif manage == 'delicacies':
            print('Hooray! Delicious')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15




    def work(self):
        if not self.car.drive():
            if self.car.fuel < 20:
                self.shopping('fuel')

            else:
                self.to_repair()
        self.money += self.job.salary
        self.gladness -= self.job.glandess_less
        self.satiety -= 4



    def chill(self):
        self.gladness += 10
        self.home.mess += 5


    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0


    def to_repair(self):
        self.car.strength += 10
        self.money -= 50


    def days_indexes(self, day):
        day = f"Today the {day} of {self.name} life!"
        print(f"day:=^50")
        print('')


    def is_alive(self):


    def live(self):


class Auto():
    def __init__(self, brand_list):
        self.brand = random.choice(brand_list)
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']


    def drive(self):
        if self.strength > 0 and self.fuel > self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("This car cannot move")
            return False



brands_of_car = {
    "BMW":{
        'fuel': 100, 'consumption': 6, 'strength': 100
    },
    "Mitsubishi ":{
        'fuel': 40, 'consumption': 2.5, 'strength': 100
    },
    "Audi":{
        'fuel': 58, 'consumption': 3.5, 'strength': 100
    },
    'Peugeot':{
        'fuel': 150, 'consumption':  8.8, 'strength': 100
    }

}

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.glandess = job_list[self.job]['gladness_less']


job_list = {
    'Java developer':
        {
            'salary': 50,
            'gladness_less': 10
        },

    'Python developer':
        {
            'salary': 60,
            'gladness_less': 5
        },

    'C++ developer':
        {
            'salary': 70,
            'gladness_less': 15
        }


}


