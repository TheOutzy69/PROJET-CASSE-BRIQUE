class Paddle:
    def __init__(self, canvas, x, y):
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__width = 100
        self.__height = 20
        self.__color = 'blue'
        self.__id = None

    def création(self):
        self.__id = self.__canvas.create_rectangle(self.__x, self.__y, self.__x + self.__width, self.__y + self.__height, fill=self.__color)

    def move_left(self, event):
        if event.keysym == 'Left':
            if self.__x - self.__width/2 > 0 - self.__width/2:
                self.__canvas.move(self.__id, -20, 0)
                self.__x -= 20
            
    def move_right(self, event):
        if event.keysym == 'Right':
            if self.__x + self.__width/2 < int(self.__canvas['width'])-self.__width/2:
                self.__canvas.move(self.__id, 20, 0)
                self.__x += 20

    def move(self, dx):
        new_x = self.__x + dx
        canvas_width = int(self.__canvas['width'])
        if 0 <= new_x <= canvas_width - self.__width:
            self.__canvas.move(self.__id, dx, 0)
            self.__x = new_x


    def getPos(self):
        return self.__canvas.coords(self.__id) 