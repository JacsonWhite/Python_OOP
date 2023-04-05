
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card = 0
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card)

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card = 200

    def spend_points(self, amount):
        self.gold_card = self.gold_card - amount


jacson = User('Jacson', 'White', 'jwhite@gmail.com', 30)
jacson.display_info()
jacson.enroll()
jacson.display_info()
jacson.spend_points(50)
jacson.display_info()

spiderman = User('Spider', 'Man', 'SMan@webs.com', 21)
spiderman.display_info()
spiderman.enroll()
spiderman.display_info()
spiderman.spend_points(80)
spiderman.display_info()

ironman = User('Tony', 'Stark', 'Tstark@marvel.com', 50)

ironman.display_info()
ironman.enroll()




