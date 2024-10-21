#!/usr/bin/python3

from Pinguin import Gender, Pingu


TARGET_PENGUIN = "Karlík Veliký"

def killPenguins(king: Pingu):
   king.kill()
   oldestAge = -1
   new_king = None

   for child in king.getChildren():
      if child.getGender() == Gender.Male and child.getAge() > oldestAge:
         new_king = child
         oldestAge = child.getAge()

   if new_king is not None: 
      killPenguins(new_king)


##### idea: 1. While iterating over the king's children save all the sons into a data structure
#####       2. In the data structure, sort the sons by the age
#####       3. Loop over the sons and input each of them into killPenguins()
#####
##### After killing a king without a heir, the code exits the function, picks a brother, if there
##### is no brother it exits the function and picks an uncle, if there is no uncle it exits 
##### the function and picks a grand-uncle ...  
##### after coronation, program delves into a function with a new king





# Primitive example algorithm that kills only the king and his first son
# def killPenguins(king: Pingu):
#     king.kill()
#     oldestAge = -1
#     pingu = None
#     for p in king.getChildren():
#         if p.getGender() == Gender.MALE and p.getAge() > oldestAge:
#             pingu = p
#             oldestAge = p.getAge()
#     if pingu is not None:
#         pingu.kill()
