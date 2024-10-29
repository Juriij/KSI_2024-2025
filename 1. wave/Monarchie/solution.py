#!/usr/bin/python3

from Pinguin import Gender, Pingu

TARGET_PENGUIN = "Karlík Veliký"

def killPenguins(king: Pingu):
   if king.getName() == TARGET_PENGUIN:
      return True

   else:
      king.kill()
      children = king.getChildren()

      male_children = [p for p in children if p.getGender() == Gender.MALE]
      male_children.sort(key=lambda p: p.getAge(), reverse=True)

      for child in male_children:
        Karlik_coronated = killPenguins(child)
        if Karlik_coronated:
            return True    
        