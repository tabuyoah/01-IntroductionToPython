"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Alex Tabuyo.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.tracer(50)

pentagon = rg.SimpleTurtle()
pentagon.pen = rg.Pen('pink',5)
pentagon.speed = 5
size = 100

for k in range (50):
    pentagon.draw_regular_polygon(5,size)
    pentagon.pen_up()
    pentagon.left(90)
    pentagon.forward(10)
    pentagon.right(90)
    pentagon.pen_down()
    size = size - 5


circle = rg.SimpleTurtle()
circle.pen = rg.Pen('purple',2)
circle.speed = 10
radius = 150

for k in range (50):
    circle.draw_circle(radius)
    circle.pen_up()
    circle.right(90)
    circle.pen_down()
    radius = radius/1.1


window.close_on_mouse_click()