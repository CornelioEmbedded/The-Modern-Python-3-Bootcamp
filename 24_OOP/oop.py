class User:

    active_users = 0

    def __init__(self, first, last, age):
        self.name = first
        self.last = last
        self.age = age
        User.active_users+=1
    
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
    
user = User('Cornelio', 'Posadas', 20)
user2 = User('Oksana', 'Ramirez', 21)

# print(user.full_name())
# print(user.initials())
# print(user.likes('candy'))
# print(user.is_senior())
# print(user.birthday())
