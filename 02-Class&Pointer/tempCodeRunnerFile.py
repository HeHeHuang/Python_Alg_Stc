class Cookies:
    def __init__(self,color):
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color = color
        
cookie_one = Cookies('Green')
cookie_one.get_color
print('Color:',cookie_one.get_color())

