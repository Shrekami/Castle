import turtle as t
t.speed(1000)
from Drawing_functions import triangle,change_position,tree,bird,sun,name, bottom, up
t.shape("turtle")
#first triangle
change_position(-650,-85)
up()

change_position(-650,-335)
bottom()

change_position(-15,0)
triangle(lenght=100,color='red')
change_position(145,0)
triangle(lenght=200,color='yellow')
change_position(225,0)
triangle(lenght=150,color='light green')


change_position(-350,-150)
tree()
change_position(-250,-250)
tree()
change_position(-150,-150)
tree()
change_position(-50,-250)
tree()
change_position(-450,-250)
tree()


change_position(315,240)
bird()
change_position(375,180)
bird()
change_position(455,220)
bird()


change_position(-495,200)
sun()


change_position(250,50)
name()



t.done()