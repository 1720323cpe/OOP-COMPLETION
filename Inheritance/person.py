class Person: 
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
       
    def introduce (self): 
        return f"Hello Everyone. My name is {self.full_name} and I'm {self.age} Of age." 
              
    @property
    def age(self): 
        return self.__age 
               
    @age.setter 
    def age (self, value): 
        if value <= 0: 
            raise ValueError('Age of existence is INVALID!')
         
        self.__age = value 
         
    @property
    def full_name(self): 
        return f" {self.first_name} {self.last_name}"