class Person:

    def __init__(self, age):
        self._age = age
        self._id_number = '931212-1234567'

    @property
    def age(self):
        return self._age
    
    @property
    def id_number(self):
        return self._id_number[:8] + '*' * 5
    
    @age.setter
    def age(self, new_age):
        if new_age <= 10:
            raise ValueError('Too young')

        
        self._age = new_age

p1 = Person(10)
print(p1.age)
print(p1.id_number)