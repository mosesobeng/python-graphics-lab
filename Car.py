
from graphics import *

class Wheel(object):

    def __init__(self, center, wheel_radius, tire_radius):
        self.tire_circle = Circle(center, tire_radius)
        self.wheel_circle = Circle(center, wheel_radius)

    def draw(self, win):
        self.tire_circle.draw(win)
        self.wheel_circle.draw(win)

    def move(self, dx, dy):
        self.tire_circle.move(dx, dy)
        self.wheel_circle.move(dx, dy)

    def set_color(self, wheel_color, tire_color):
        self.tire_circle.setFill(tire_color)
        self.wheel_circle.setFill(wheel_color)

    def undraw(self):
        self.tire_circle .undraw()
        self.wheel_circle .undraw()

    def get_size(self):
        return self.tire_circle.getRadius()

    def get_center(self):
        return self.tire_circle.getCenter()


#add any functions or classes you might define here

    def animate(self, win, dx, dy, n):
        if n > 0:
            self.move(dx, dy)
            win.after(100, self.animate, win, dx, dy, n-1)



class Car(object):

    def __init__(self,center1, wheel_radius1,center2, wheel_radius2,p):
        
        self.body = Rectangle(center2,center1)
        ##self.body.setWidth(p)
        self.first_wheel = Wheel(center1, wheel_radius1,wheel_radius1-10)
        self.second_wheel = Wheel(center2, wheel_radius2,wheel_radius1-10)
        


    def draw(self,win):
        self.first_wheel.draw(win)
        self.second_wheel.draw(win)
        self.body.draw(win)

    def set_color(self,wheel_color, tire_color,body_color):
        self.body.setOutline(body_color)
        self.first_wheel.set_color(wheel_color, tire_color)
        self.second_wheel.set_color(wheel_color, tire_color)

      
        

        
        





from graphics import *

def main():
    win = GraphWin('Car', 700, 300)
    

    car1 = Car(Point(50,50),15,Point(100,50),15,40)
    car1.draw(win)

    car1.set_color('black', 'grey', 'pink')


    win.mainloop()

main()






























