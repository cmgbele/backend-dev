import time 
class food():


    company = "THE_CHRISTOPHERS_"


    def __init__(self, score, age, treat ):
        self.score = score
        self.age = age
        self.treat = treat

    def __str__(self):
        return f'{self.score} {self.age} {self.treat}' 


    def __add__(self, other): 
        if isinstance(other ,food):

             return self.score + other.score

        raise TypeError(f'Expected type {type(self)} but got {type(other)}')  

    def __to_know_(self):
        """THis is a private method used to know the age  
        Returns:
                [int]: [age of individual]"""

    def compete(self):
        """This is a competition in which the winners above or equals  the score 90 wins a special treat
        Returns:
                [int]: [the special treat]
        """ 
        Age = 2021
        return Age - self.age  
        
        scores = 90 
        if self.score >= scores:
            print("Winner")
            print("A TEN THOUSAND NAIRA GIFT CARD AT KRISPY KREME") 
        else:
            return 0 
        
 

food1 = food(79,"21","icecream")
food2 = food(92,"34","pizza") 

# print(food1+food2) 
# print(food1.company) 
# print(food2.company)

# print(food1.compete())
# print(food2.compete()) 

class store(food):

    def __init__(self,score, age, treat, awards):

        self.awards = awards 
        super().__init__(score,age,treat) 
    
@property




store1 = store(45,19,"CHICKEN","Trophy")
store2 = store(68,39,"Lotte","Derby") 



