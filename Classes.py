
class Road:
    
    def __init__(self, lenght : int, max_speed : int, id : int, id_crossroads : tuple[int, int], traffic_light : TrafficLight) -> None:
        self._lenght = lenght
        self._max_speed = max_speed
        self._id = id
        self._id_crossroads = id_crossroads
        self._traffic_lights = traffic_light
        self.space = [None for _ in range(lenght)]
        self._can_join = True
    
    def GetId(self):
        return self._id

    def GetMaxSpeed(self):
        return self._max_speed

    def GetCrossroads(self):
        return self._id_crossroads

    def GetTrafficLight(self):
        return self._traffic_lights._able_to_pass
    
    def UpdateTrafficLight(self):
        self._traffic_lights = self._traffic_lights.Update()
    
    def CanJoin(self):
        return self._can_join

    def Move(self):
        self.UpdateTrafficLight()
        if self.GetTrafficLight():
            wichle = self.space[-1]
            self.space = [None] + self.space[:-1]
            return wichle
        else:
            for i in range(self._lenght - 1, 0, -1):
                if self.space[i] == None:
                    self.space[:i] = [None] + self.space[:i - 1]
    
    def AddWichle(self, wichle : Wichle):
        self.space[:wichle.GetLenght()] = wichle


class Wichle:

    def __init__(self, type : str, id : int) -> None:
        self._type = type
        self._id = id
        self._lenght = None
        self._speed = None
        if type == 'car':
            self._speed = 5
            self._lenght = 2
        else:
            raise Exception("Undefined wichle type!")
    
    def GetLenght(self):
        return self._lenght
    
    def GetId(self):
        return self._id
    
    def GetSpeed(self):
        return self._speed
    
    def GetType(self):
        return self._type