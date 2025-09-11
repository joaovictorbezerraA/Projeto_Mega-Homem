from camera import Camera


class Object(Camera):
    def __init__(self, x, y, width=0, height=0, camera_x=0, camera_y=0):
        super().__init__(camera_x, camera_y)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
