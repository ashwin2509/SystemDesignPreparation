class Dog:
    species = "mammal"
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
rockey = Dog("Rocky", 8)
array = [5, 6, 8]

print("{} is {} and {} is {}. ".format(philo.name, philo.age, mikey.name, mikey.age))

if philo.species == 'mammal':
    print("{} is a {}!!".format(philo.name, philo.species))
    


# In[7]:


def get_biggest_number(nums):
    return max(nums)

print("the oldest dog is {} years old".format(get_biggest_number(array)))
    

        

