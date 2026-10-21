# ==========================================
# MAIN PROGRAM - FLL BIOGLOW 2026
# ==========================================

# ---- IMPORTS ----
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, hub_menu, StopWatch, multitask, run_task

# ---- HUB ----
hub = PrimeHub()

# ==========================================
# ROBOT INFO
# ==========================================
# Left wheel motor          : Port A (COUNTERCLOCKWISE)
# Right wheel motor         : Port E (CLOCKWISE)
# Front attachment motor    : Port B
# Back attachment motor     : Port F
# Color sensor (bottom)     : Port D - line following (not implemented)
# Color sensor (top)        : Port C - mission select by lego color (not implemented)
#
# Wheel diameter  : 62.4 mm
# Axle track      : 108.204 mm
#
# COLOR TO MISSION MAP:
# Yellow -> Run 0 : Extra Katydid
# Black  -> Run 1 : Drone Survey (1), Exploding Seeds (2)
# Green  -> Run 2 : Flip the Rock (3), Lucky Leaves (4), Reaching Roots (5)
# My Red -> Run 3 : 
# Blue   -> Run 4 : 
# White  -> Run 5 : 
# Orange -> Run 6 : Seeds of Renewal (?)
# ==========================================

# ---- DRIVE MOTORS ----
front_left_wheel  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
front_right_wheel = Motor(Port.E, Direction.CLOCKWISE)

# ---- ATTACHMENT MOTORS ----
front_attachment = Motor(Port.B)
back_attachment  = Motor(Port.F)

# ---- COLOR SENSOR ----
# Top sensor on Port C - reads the color of a LEGO brick to pick the mission
color_sensor = ColorSensor(Port.C)

# Define our custom red based on what OUR sensor actually reads
# h=352 (red hue), s=92 (vivid), v=36 (our brightness in our lighting)
MY_RED = Color(h=352, s=92, v=36)
MY_BLACK = Color(h=0, s=0, v=0)
MY_GREEN = Color(h=155, s=76, v=57)
MY_GRAY = Color(h=195, s=22, v=73) or Color(h=194, s=24, v=76)
MY_YELLOW = Color(h=49, s=62, v=100) or Color(h=50, s=64, v=100)
MY_BLUE = Color(h=217, s=87, v=46) or Color(h=217, s=88, v=46)
MY_DARK_GRAY = Color(h=198, s=22, v=51) or Color(h=198, s=26, v=51)
MY_ORANGE = Color(h=9, s=75, v=100)

# Only look for these specific colors - much more accurate than detecting all colors!
# This prevents confusion between similar colors under different lighting.
color_sensor.detectable_colors([
    MY_GREEN,
    MY_RED,
    MY_GRAY,
    MY_YELLOW,
    MY_BLUE,
    MY_ORANGE,
    Color.WHITE,
])


# ---- DRIVE BASE ----
robot = DriveBase(front_left_wheel, front_right_wheel,
                  wheel_diameter=62.4, axle_track=108.204)
robot.use_gyro(True)

# ==========================================
# RESET ROBOT
# ==========================================
def reset_robot():
    # Stop all motors immediately
    robot.stop()
    front_attachment.stop()
    back_attachment.stop()

    # robot.reset() wipes the gyro heading back to zero.
    # Without this, if you stop a mission halfway through,
    # the gyro remembers the old angle and the next mission
    # drives crooked thinking it's already turned!
    robot.reset()

    # Reset all movement settings to safe defaults
    robot.settings(straight_speed=500, straight_acceleration=1000,
                   turn_rate=100,      turn_acceleration=1000)
    robot.use_gyro(True)

# ==========================================
# MISSIONS
# ==========================================

def mission_0():
    reset_robot()
    #Insert code for mission 0 here (Extra Katydid) if needed

def mission_1():
    reset_robot()
    import R1_Drone_Exploding
    R1_Drone_Exploding.run(robot, front_attachment, back_attachment)

def mission_2():
    reset_robot()
    #Insert code for mission 2 here (Flip the Rock, Lucky Leaves, Reaching Roots) if needed 

# ---- OLD SEASON MISSIONS (not used this year) ----
# def mission_3():
#     reset_robot()
#     import A3_Statue_Delivery_Canada
#     A3_Statue_Delivery_Canada.run(robot, front_attachment, back_attachment)
#
# def mission_4():
#     reset_robot()
#     import A4_Shipwreck
#     A4_Shipwreck.run(robot, front_attachment, back_attachment)
#
# def mission_5():
#     reset_robot()
#     import A5_Soil
#     A5_Soil.run(robot, front_attachment, back_attachment)

def mission_6():
    reset_robot()
    #Insert code for mission 6 here (Seeds of Renewal) if needed
    # import A6_Careful_Recovery_Mineshaft
    # A6_Careful_Recovery_Mineshaft.run(robot, front_attachment, back_attachment)

# def mission_7():
#     reset_robot()
#     import A7_Forum_Delivery
#     A7_Forum_Delivery.run(robot, front_attachment, back_attachment)
#
# def mission_8():
#     reset_robot()
#     import A3_Statue_Delivery_Alliance
#     A3_Statue_Delivery_Alliance.run(robot, front_attachment, back_attachment)
#
# #Smashy Code in Case Needed
# def mission_9():
#     reset_robot()
#     import A9_Smashy_Silo_Alliance_Backup
#     A9_Smashy_Silo_Alliance_Backup.run(robot, front_attachment, back_attachment)

# ==========================================
# COLOR TO MISSION LOOKUP
# ==========================================
# Hold a colored LEGO brick up to the top sensor.
# Scroll to "C" on the menu and press center to run that mission.
# If the color isn't recognised, the hub light flashes red.

def run_by_color():
    detected = color_sensor.color()
    print("Color detected:", detected)  # Prints to computer console instantly

    if detected == Color.BLACK:
        print("Running: Mission 0 - Heavy Lifting with Smashy")
        mission_0()
    elif detected == MY_GRAY:
        print("Running: Mission 1 - Marky Mark")
        mission_1()
    elif detected == MY_GREEN:
        print("Running: Mission 2 - Angler")
        mission_2()
    # ---- OLD SEASON COLORS (not used this year) ----
    # elif detected == MY_YELLOW:
    #     print("Running: Mission 4 - Statue")
    #     mission_3()
    # elif detected == MY_BLUE:
    #     print("Running: Mission 5 - Shipwrek")
    #     mission_4()
    # elif detected == MY_DARK_GRAY:
    #     print("Running: Mission 6 - Soil")
    #     mission_5()
    # elif detected == Color.WHITE:
    #     print("Running: Mission 7 - Careful Recovery / Mineshaft")
    #     mission_6()
    # elif detected == MY_ORANGE:
    #     print("Running: Mission 8 - Forum Delivery")
    #     mission_7()
    else:
        print("Color not recognised! Got:", detected, "- flashing red")
        hub.light.on(Color.RED)
        wait(500)
        hub.light.off()

# ==========================================
# MAIN LOOP
# ==========================================
# HOW TO USE:
#   STOP  -> Press the CENTER button on the hub during any run
#   GO    -> The menu comes back automatically after each mission.
#            Scroll to "C" and press center for color mode,
#            or scroll to a number and press center for manual mode.
#
# DOUBLE PRESS FIX: After every mission there is a 1 second pause
# before the menu appears. This stops accidental double presses
# from immediately launching the next mission!

selected = "C"  # Start on color mode by default

while True:

    # "C" = color sensor mode, numbers = manual fallback
    # all_options = ["C", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # old season
    all_options = ["C", "0", "1", "2", "6"]
    idx = all_options.index(selected)
    ordered = all_options[idx:] + all_options[:idx]

    # try/except catches the stop button press mid-run.
    # Instead of crashing the whole program, it stops cleanly
    # and brings you back to the menu on the SAME mission
    # so you can immediately rerun it from the beginning!
    try:
        selected = hub_menu(*ordered)

        if selected == "C":
            run_by_color()
        elif selected == "0":
            mission_0()
        elif selected == "1":
            mission_1()
        elif selected == "2":
            mission_2()
        # elif selected == "3":
        #     mission_3()
        # elif selected == "4":
        #     mission_4()
        # elif selected == "5":
        #     mission_5()
        elif selected == "6":
            mission_6()
        # elif selected == "7":
        #     mission_7()
        # elif selected == "8":
        #     mission_8()
        # elif selected == "9":
        #     mission_9()

        # Wait 1 second after mission finishes before showing menu again
        # This prevents accidental double presses from relaunching the mission!
        wait(1000)

    except SystemExit:
        # Center button was pressed mid-run!
        # Stop all motors and reset the gyro,
        # then fall back to the menu on the same mission.
        robot.stop()
        front_attachment.stop()
        back_attachment.stop()
        robot.reset()
        wait(1000)  # Same double press protection after a stop