class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f'There are {cls.active_users} active users'
    
    @classmethod
    def from_string(cls, data):
        first, last, age = data.split(',')
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.name = first
        self.last = last
        self.age = age
        User.active_users+=1
    
    def __repr__(self):
        return f'{self.name} is {self.age}'

    def logout(self):
        User.active_users-=1
        return f'{self.name} has logged out'

    def full_name(self):
        return f'{self.name} {self.last}'
    
    def initials(self):
        return f'{self.name[0]}.{self.last[0]}.'
    
    def likes(self, thing):
        return f'{self.name} likes {thing}'
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age+=1
        return f'Happy {self.age}th, {self.name}'
    
Tom = User.from_string('Tom,Hay,23')
j = User('judy','steele', 20)
print(j)