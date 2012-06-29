from graphics import *


#add any functions or classes you might define here

class GraphWin(tk.Canvas):

    """A GraphWin is a toplevel window for displaying graphics."""

    def __init__(self, title="Graphics Window",
                 width=200, height=200, autoflush=True):
        master = tk.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master, width=width, height=height)
        self.master.title(title)
        self.title = title
        self.pack()
        master.resizable(0,0)
        self.foreground = "black"
        self.items = []
        self.mouseX = None
        self.mouseY = None
        self.key = None                     #MB: added
        self.bind("<Button-1>", self._onClick)
        master.bind("<Key>", self._onKeyPress) #MB: added
        self.height = height
        self.width = width
        self.autoflush = autoflush
        self._mouseCallback = None
        self._keyCallback = None #MB: added
        self.trans = None
        self.closed = False
        if autoflush: _root.update()

    def __repr__(self):
        return "GraphWin("+ '"' + self.title + '"' + "," + str(self.getWidth()) + "," + str(self.getHeight()) +","+ str(self.autoflush) + ")"

    # Including str explicitly overrides tk.Canvas's str method
    def __str__(self):
        return self.__repr__()

    def __checkOpen(self):
        if self.closed:
            raise GraphicsError("window is closed")

    def setBackground(self, color):
        """Set background color of the window"""
        self.__checkOpen()
        self.config(bg=color)
        self.__autoflush()
        
    def setCoords(self, x1, y1, x2, y2):
        """Set coordinates of window to run from (x1,y1) in the
        lower-left corner to (x2,y2) in the upper-right corner."""
        self.trans = Transform(self.width, self.height, x1, y1, x2, y2)

    def close(self):
        """Close the window"""

        if self.closed: return
        self.closed = True
        self.master.destroy()
        self.__autoflush()


    def isClosed(self):
        return self.closed

    def __autoflush(self):
        if self.autoflush:
            _root.update()

    
    def plot(self, x, y, color="black"):
        """Set pixel (x,y) to the given color"""
        self.__checkOpen()
        xs,ys = self.toScreen(x,y)
        self.create_line(xs,ys,xs+1,ys, fill=color)
        self.__autoflush()
        
    def plotPixel(self, x, y, color="black"):
        """Set pixel raw (independent of window coordinates) pixel
        (x,y) to color"""
        self.__checkOpen()
        self.create_line(x,y,x+1,y, fill=color)
        self.__autoflush()
    	
    def flush(self):
        """Update drawing to the window"""
        self.__checkOpen()
        self.update_idletasks()

        
    def getMouse(self):
        """Wait for mouse click and return Point object representing
        the click"""
        self.update()      # flush any prior clicks
        self.mouseX = None
        self.mouseY = None
        while self.mouseX == None or self.mouseY == None:
            self.update()
            if self.isClosed(): raise GraphicsError("getMouse in closed window")
            time.sleep(.1) # give up thread
        x,y = self.toWorld(self.mouseX, self.mouseY)
        self.mouseX = None
        self.mouseY = None
        return Point(x,y)

    def checkMouse(self):
        """Return mouse click last mouse click or None if mouse has
        not been clicked since last call"""
        if self.isClosed():
            raise GraphicsError("checkMouse in closed window")
        self.update()
        if self.mouseX != None and self.mouseY != None:
            x,y = self.toWorld(self.mouseX, self.mouseY)
            self.mouseX = None
            self.mouseY = None
            return Point(x,y)
        else:
            return None

# MB: added            
    def checkKey(self):
        """Return key or None if no key has
        been pressed since last call"""
        if self.isClosed():
            raise GraphicsError("checkKey in closed window")
        self.update()
        if self.key != None:
            keyToReturn = self.key
            self.key = None
            return keyToReturn
        else:
            return None
# MB: end
            
    def getHeight(self):
        """Return the height of the window"""
        return self.height
        
    def getWidth(self):
        """Return the width of the window"""
        return self.width
    
    def toScreen(self, x, y):
        trans = self.trans
        if trans:
            return self.trans.screen(x,y)
        else:
            return x,y
                      
    def toWorld(self, x, y):
        trans = self.trans
        if trans:
            return self.trans.world(x,y)
        else:
            return x,y
        
    def setMouseHandler(self, func):
        self._mouseCallback = func
        
    def _onClick(self, e):
        self.mouseX = e.x
        self.mouseY = e.y
        if self._mouseCallback:
            self._mouseCallback(Point(e.x, e.y)) 

    #MB: added
    def _onKeyPress(self, e):
        self.key = e.keysym
    #MB: end 



from graphics import *

def main():
    win = GraphWin('Program Name', 700, 500)
    win.mainloop()


main()

