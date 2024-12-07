class Guitar:
  def __init__(self, name):
    self.name = name

  def sum(self, guitar, option, pick):
    return guitar + option + pick
  
a01 = Guitar("PRS")
print(a01.name)
print(a01.sum(110000, 10000, 100))