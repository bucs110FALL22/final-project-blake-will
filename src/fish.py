import random

class Fish:
  
  def __init__(self, x,y):
    self.x = x
    self.y = y
    self.value = 0
    self.speed = random.randrange(5, 10)
    if self.x == 400:
      self.speed * -1
    self.image = self.chooseFish()
    

  def chooseFish(self):
    type = random.randrange(101)
    if type > 0 and type <= 50:
      self.value = 10
    if type > 50 and type <= 70:
      self.value = 20
    if type > 70 and type <= 85:
      self.value = 35
    if type > 85 and type <= 95:
      self.value = 50
    if type > 95 and type <= 100:
      self.value = 100

  def reportValue(self):
    print(self.value)

def main():
  mirae = Fish(10, 10)
  #mirae.chooseFish()
  mirae.reportValue()

main()
