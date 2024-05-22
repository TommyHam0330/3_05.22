from rabbit import Rabbit

class MountainRabbit(Rabbit):
  shape= "mountain"

  def __init__(self,x,y):
    self.goto(x,y)

  def eat_glass(self):
    print("토끼가 풀을 뜯습니다")

a = MountainRabbit(1,2)
a.eat_glass()