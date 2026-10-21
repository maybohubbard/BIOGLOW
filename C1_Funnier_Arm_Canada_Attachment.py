from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#New Robot Tuesday Route Funny Arm Heavy Lifting

#Robot Info

#front left motor wheel - port B
#front attachment motor - port A
#back attachment motor - port E
#front right motor wheel - port F
#color sensor - port D
#color sensor - port C

#standard technic small blue/black wheel_diameter = 56
#old robot axle_track = 95.504
#upgraded wheel diameter wheel_diameter=62.4
#new robot axle_track = 108.204

# ---- DRIVE MOTORS ----
# Set the positive direction for each motor based on how they're mounted
front_left_wheel = Motor(Port.B, Direction.COUNTERCLOCKWISE)
front_right_wheel = Motor(Port.F, Direction.CLOCKWISE)

# ---- ATTACHMENT MOTORS ----
front_attachment = Motor(Port.A)
back_attachment = Motor(Port.E)

# ---- DRIVE BASE ----
robot = DriveBase(front_left_wheel, front_right_wheel,
                       wheel_diameter=62.4, axle_track=108.204)

#Turn on Gyro
robot.use_gyro(True)

# Reset the front attachment to make sure it starts
# in the correct position before the run begins
front_attachment.run_angle(50, -5)

# ---- DRIVE TO FORGE ----
# Drive forward 720mm (about 28 inches) toward the forge
robot.settings(straight_speed=1000)
robot.straight(690)  #620 1st. 650 second time
robot.stop()

# Turn 45 degrees right to line up with the forge
robot.settings(turn_rate=50)
robot.turn(45)

# Drop the front arm down to get under the heavy lifter (millstone)

front_attachment.run_angle(500, -450)

# Drive forward 64mm (about 2.5 inches) to engage with the millstone
robot.straight(64)

# Lift the arm back up, bringing the millstone with it
try:
    front_attachment.run_angle(500, 500, wait=False)
except:
    pass    
# Drop smashy down to get silo points

try:
    back_attachment.run_angle(987, -50)
except:
    pass
# Go back up
back_attachment.run_angle(987, 90)

# Drop smashy down to get silo points
back_attachment.run_angle(987, -95)
# Go back up
back_attachment.run_angle(987, 100)
back_attachment.run_angle(987, -100)
back_attachment.run_angle(987, 100)


# Turn another 45 degrees to line up to release the ore blocks (boulders)
robot.settings(turn_rate=55) 
robot.turn(45)

# Drive backwards 185mm to pull the millstone away from the forge
robot.straight(-185)

# Turn 20 degrees right to aim at the forge boulders
robot.turn(20)

# Drive forward slowly 254mm (10 inches) to push the ore blocks off the forge
robot.settings(straight_speed=100)
robot.straight(260)

# Turn 15 degrees left to aim back toward home base
robot.turn(-15)

# Drive forward 400mm (about 16 inches) back toward the right home base
robot.settings(straight_speed=200)
robot.straight(400)