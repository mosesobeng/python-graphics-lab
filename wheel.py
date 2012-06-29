
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




from graphics import *

def main():
    win = GraphWin('Wheel', 700, 500)

    wheel = Wheel(Point(100, 100), 50, 70)
    wheel.set_color('gray', 'black')
    wheel.draw(win)
    wheel.animate(win,10,1,100)

    myRec = Rectangle(1,40)
    myRec.clone()



    win.mainloop()
    

    


main()































