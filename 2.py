class Transportation(object):
   """Abstract base class"""

   def __init__( self, start, end, distance ):
      if self.__class__ == Transportation:
         raise NotImplementedError
      self.start = start
      self.end = end
      self.distance = distance

   def find_cost( self ):
      """Abstract method; derived classes must override"""
      raise NotImplementedError


class Walk( Transportation ):

   def __init__( self, start, end, distance ):
      Transportation.__init__( self, start, end, distance)

   def find_cost( self ):
      return 0
   
class Taxi(Transportation):
    def __init__(self, start, end, distance):
      Transportation.__init__(self, start, end, distance)

    def find_cost(self):
      return self.distance * 40

class Train(Transportation):
   def __init__(self, start, end, distance, station):
      super().__init__(start, end, distance)
      self.station = station 

   def find_cost(self):
      return self.station * 5  


class Bus(Transportation):
   def __init__(self, start, end, distance, station):
      super().__init__(start, end, distance)
      self.station = station  

   def find_cost(self):
      return self.station * 2  

   

travel_cost = 0

trip = [ Walk("KMITL","KMITL SCB Bank",0.6),
         Taxi("KMITL SCB Bank","Ladkrabang Station",5),
         Train("Ladkrabang Station","Payathai Station",40,6),
         Taxi("Payathai Station","The British Council",3),
          Bus("Ladkrabang Station","Payathai Station",40,6) ]

for travel in trip:
   travel_cost += travel.find_cost()
print(travel_cost)