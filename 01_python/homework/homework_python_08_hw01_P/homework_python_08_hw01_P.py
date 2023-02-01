class Point:
    pass
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    pass
    def __init__(self, p1, p2):
        width = abs(p1.x - p2.x)
        height = abs(p1.y - p2.y)

        self.get_area = width * height
        self.get_perimeter = 2 * (width + height)
        self.is_square = width == height

# 입력 예시
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# 출력 예시
# 4
# 8
# True

# 9
# 12
# True