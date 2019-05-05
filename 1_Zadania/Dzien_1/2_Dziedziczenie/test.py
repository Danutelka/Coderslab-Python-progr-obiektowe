class Lightsaber:



   def __init__(self, color):
       self._c = ["niebieski", "zielony", "fioletowy", "czerwony"]
       self.color = color
   def __str__(self):
       if self.color == "niebieski":
           return "Lighstaber: niebieski, force: jasna"
       if self.color == "zielony":
           return "Lighstaber: zielony, force: jasna"
       if self.color == "fioletowy":
           return "Lighstaber: fioletowy, force: jasna"
       if self.color == "czerwony":
           return "Lighstaber: czerwony, force: ciemna"

   @property
   def color(self):
       return self._color

   @color.setter
   def color(self, miecz):
       if miecz in self._c:
           self._color = miecz
       else:
           raise ValueError("Bad lightsaber color!")


jedi = Lightsaber("niebieski")
print(jedi.color)
