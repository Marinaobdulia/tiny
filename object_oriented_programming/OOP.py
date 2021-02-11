class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Miliki', 16)
cat2 = Cat('Fofo', 2)
cat3 = Cat('Fofito', 7)

# 2 Create a function that finds the oldest cat
def Oldest(cats):
    age = 0
    for cat in cats:
        if cat.age > age:
            age = cat.age
            oldest = cat
    return oldest


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
oldest = Oldest([cat1, cat2, cat3])
print(f'The oldest cat is {oldest.age} years old.')