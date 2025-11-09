class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'
    activity = 'walk'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'
    activity = 'lie'

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds} and their favorite activity is {dog.activity}")
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds} and their favorite activity is {cat.activity}")