# WT*? is duck typing? 
# this is *not* about class inheritance
# AUTHOR Sven Schrodt
# SINCE 2025-04-20

""" Examples for so called duck typing 

    “When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck”
        - This sentence is attributed to James Whitcomb Riley; SEE https://de.wikipedia.org/wiki/James_Whitcomb_Riley 
        
        
"""




class Duck:

    def walk(self):
        print("walking")
    
    def fly(self):
        print("flying")

    def swim(self):
        print("swimming")

class Albatross:

    def fly(self):
        print("flying")
        
    def walk(self):
        print("walking")

class Eagle:

    def fly(self):
        print("flying")
        
    def walk(self):
        print("walking")
        
    def swim(self):
        print('swimming -  probably it can only happen once')

birds = [Duck(), Eagle(), Albatross()]

# Foreach-Schleife mit Ducktyping
for bird in birds:
    try:
        print(type(bird))
        bird.fly()
        bird.walk()
        bird.swim()
    except AttributeError as e:
        print(repr(e))