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
        print(f"{day:=^50}")
        print(f'{self.name} indexses:')
        print(f"Money - {self.money}")
        print(f"Gladness - {self.gladness}")
        print(f"Food - {self.home.food}")
        print(f"Mess - {self.home.mess}")
        print(f"Car fuel - {self.car.fuel}")
        print(f"Car strength - {self.car.strength}")


    def is_alive(self):
        if self.gladness < 0:
            print('Depression')
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt")
            return False


    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home == None:
            print("Settled in the house")
            self.get_home()
        if self.car == None:
            print("I bought new car!")
            self.get_car()
        if self.job == None:
            self.job = self.get_job()
            print(f"I dont have a job, Im going to get {self.job}")
        self.days_indexes()

        dice = random.randint(1,4)
        if self.satiety < 20:
            print("I ll go to eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess...")
            else:
                print('Lets chill')
                self.chill()
        elif self.money < 0:
            print("Lets work")
            self.work()
        elif self.car.strength < 15:
            print('I need to repair my car')
            self.to_repair()
        if dice == 1:
            print("Lets chill!")
            self.chill()
        elif dice == 2:
            print("Lets work")
            self.work()
        elif dice == 3:
            print("cleaning time")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage='delicacies')




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

nick = Human(name = "Nick")

for day in range(1, 8):
    if nick.live(day) == False:
        print("game over")
        break

