
import turtle as t
from Drawing_functions import change_position, red, blue, star

t.speed(50000000000)
print(t.window_height())
y_cordinate =-335
for i in range(7):
    change_position(-650, y_cordinate)
    red()
    y_cordinate+=105

change_position(-650,-20)
blue()
y_coordinate=5
for i in range(5):
    x_cordinate = -30
    for i in range(6):
        change_position(x_cordinate,y_coordinate)
        star()
        x_cordinate-=120
    y_coordinate+=75
y_coordinate = 40
for i in range(5):
    x_cordinate = -85
    for i in range(5):
        change_position(x_cordinate, y_coordinate)
        star()
        x_cordinate-=120
    y_coordinate+=75

# -85,40
t.done()

# import turtle as t
# from Drawing_functions import change_position, red, blue, star
#
# t.speed(500)
# print(t.window_height())
# y_coordinate = -335
# for i in range(7):
#     change_position(-650, y_coordinate)
#     red()
#     y_coordinate += 105
#
# change_position(-650, -20)
# blue()
# y_coordinate = 5
# for i in range(5):
#     x_coordinate = -30
#     for j in range(6):
#         change_position(x_coordinate, y_coordinate)
#         star()
#         x_coordinate -= 120
#     y_coordinate += 75
#
#     change_position(-450, y_coordinate - 40)
#     for j in range(5):
#         change_position(x_coordinate, y_coordinate)
#         star()
#
# t.done()