import turtle
import random

class Polygon:
    def __init__(self):
        self.num_sides = None
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.border_size = random.randint(1, 10)

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def reduction_ratio(self):
        reduction_ratio = 0.618
        turtle.penup()
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= reduction_ratio


class Triangle(Polygon):
    def __init__(self):
        super().__init__()
        self.num_sides = 3

class Square(Polygon):
    def __init__(self):
        super().__init__()
        self.num_sides = 4

class Pentagon(Polygon):
    def __init__(self):
        super().__init__()
        self.num_sides = 5

class Draw:
    def __init__(self):
        self.user_choice = int(input('Which art do you want to generate? Enter a number between 1 to 9 inclusive: '))
    
    def draw(self):
        if self.user_choice == 1:
            for i in range(30):
                shape_poly = Triangle()
                shape_poly.draw_polygon()
        elif self.user_choice == 2:
            for i in range(30):
                shape_poly = Square()
                shape_poly.draw_polygon()
        elif self.user_choice == 3:
            for i in range(30):
                shape_poly = Pentagon()
                shape_poly.draw_polygon()
        elif self.user_choice == 4:
            for i in range(30):
                if i % 2 == 0:
                    shape_poly = Pentagon()
                elif i % 3 == 0:
                    shape_poly = Square()
                else:
                    shape_poly = Triangle()
                shape_poly.draw_polygon()
        elif self.user_choice == 5:
            for i in range(30):
                shape_poly = Triangle()
                for j in range(3):
                    shape_poly.draw_polygon()
                    shape_poly.reduction_ratio()
        elif self.user_choice == 6:
            for i in range(30):
                shape_poly = Square()
                for j in range(3):
                    shape_poly.draw_polygon()
                    shape_poly.reduction_ratio()
        elif self.user_choice == 7:
            for i in range(30):
                shape_poly = Pentagon()
                for j in range(3):
                    shape_poly.draw_polygon()
                    shape_poly.reduction_ratio()
        elif self.user_choice == 8:
            for i in range(30):
                if i % 2 == 0:
                    shape_poly = Pentagon()
                elif i % 3 == 0:
                    shape_poly = Square()
                else:
                    shape_poly = Triangle()
                for j in range(3):
                    shape_poly.draw_polygon()
                    shape_poly.reduction_ratio()
        elif self.user_choice == 9:
            for i in range(30):
                if i % 2 == 0:
                    shape_poly = Pentagon()
                elif i % 3 == 0:
                    shape_poly = Square()
                else:
                    shape_poly = Triangle()
                get_smaller_or_not = random.choice([True, False])
                if get_smaller_or_not == True:
                    for j in range(3):
                        shape_poly.draw_polygon()
                        shape_poly.reduction_ratio()
                else:
                    shape_poly.draw_polygon()


draw = Draw()
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
draw.draw()
turtle.done()
