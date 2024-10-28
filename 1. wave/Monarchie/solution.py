#!/usr/bin/python3

from Pinguin import Gender, Pingu

TARGET_PENGUIN = "Karlík Veliký"




# # O( ch*log(ch) + ch )
# def killPenguins(king: Pingu):
#    if king.getName() == TARGET_PENGUIN:
#       return True

#    else:
#       king.kill()

#       children = king.getChildren()
#       children.sort(key=lambda p: p.getAge(), reverse=True)

#       for child in children:
#          if child.getGender() == Gender.MALE:
#             Karlik_coronated = killPenguins(child)
#             if Karlik_coronated:
#                return True




# # O( ch + s*log(s) + s )
# def killPenguins(king: Pingu):
#    if king.getName() == TARGET_PENGUIN:
#       return True

#    else:
#       king.kill()

#       children = king.getChildren()

#       children = [p for p in children if p.getGender() == Gender.MALE]
#       children.sort(key=lambda p: p.getAge(), reverse=True)
      

#       for child in children:
#          if child.getGender() == Gender.MALE:
#             Karlik_coronated = killPenguins(child)
#             if Karlik_coronated:
#                return True    








##### idea: 1. While iterating over the king's children save all the sons into a data structure
#####       2. In the data structure, sort the sons by the age
#####       3. Loop over the sons and input each of them into killPenguins()
#####
##### After killing a king without a heir, the code exits the function, picks a brother, if there
##### is no brother it exits the function and picks an uncle, if there is no uncle it exits 
##### the function and picks a grand-uncle ...  
##### after coronation, program delves into a function with a new king


##### idea: Before executing the king (king.kill()) check if he isn't Karlik Veliky.
#####       If the current king is Karlik Veliky, don't kill him and cease the genocide (end program).






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



# # O(s*ch + ch + slogs)
# def killPenguins(king: Pingu):
#    if king.getName() == TARGET_PENGUIN:
#       return True

#    else:
#       king.kill()
#       sons_ages = []   

#       for child in king.getChildren():
#          if child.getGender() == Gender.MALE:
#             sons_ages.append(child.getAge())       

#       sons_ages.sort(reverse=True)

#       for age in sons_ages:
#          for child in king.getChildren(): 
#             if child.getAge() == age:
#                Karlik_coronated = killPenguins(child)
#                if Karlik_coronated:
#                   return True



# O(s+2ch + slogs) 
# def killPenguins(king: Pingu):
#    if king.getName() == TARGET_PENGUIN:
#       return True

#    else:
#       king.kill()
#       sons_ages = []   

#       for child in king.getChildren():
#          if child.getGender() == Gender.MALE:
#             sons_ages.append(child.getAge())       

#       sons_ages.sort(reverse=True)

#       children = {node.getAge(): node for node in king.getChildren()}


#       for age in sons_ages:
#          child = children[age] 
#          Karlik_coronated = killPenguins(child)
#          if Karlik_coronated:
#             return True