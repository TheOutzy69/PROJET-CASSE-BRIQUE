class Paddle:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = 100
        self.height = 20
        self.color = 'blue'
        self.id = None

    def création(self):
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)

    def move_left(self, event):
        if event.keysym == 'Left':
            if self.x > 0:
                self.x -= 20
                self.canvas.move(self.id, -20, 0)
            
    def move_right(self, event):
        if event.keysym == 'Right':
            if self.x + self.width < int(self.canvas['width']):
                self.x += 20
                self.canvas.move(self.id, 20, 0)