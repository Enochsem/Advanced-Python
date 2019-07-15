# def is_even(n):
#     if n % 2 == 0:
#     	return n
# numbers = [1,56,234,87,4,76,24,69,90,135]
# print(list(map(is_even,numbers)))

# using lambda in-line to print out even numbers in a list
numbers = [1,56,234,87,4,76,24,69,90,135]
answer=list(filter( lambda x: x % 2 == 0,numbers))
print(answer)

# usinig lambda for odd numbers in a list
numbers = [1,56,234,87,4,76,24,69,90,135]
answer=list(filter(lambda x: x % 2 == 1,numbers))
print(answer)

#using the "not" function
numbers = [1,56,234,87,4,76,24,69,90,135]
def is_even(n):
    if not n % 2 == 0:
     	return n
answer=list(filter(is_even,numbers))
print(answer)
print(not(False))

#list comprehensions (printing out the lenght of the words > 3)
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
lst = [len(word) for word in words if len(word) > 3]
print(lst)

#printing out the positive nuumbbers in the list
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print([n for n in numbers if n > 0])

#classes
class Person():
    
    def __init__(self, name = "Enoch", age = 0):
        self.age = age
        self.name = name
        
    def is_adult(self):
        return self.age > 18
    
bob = Person("Bob", 15)
enoch = Person("Enoch", 23)

print(list(map(lambda person: person.is_adult(), [bob, enoch])))

