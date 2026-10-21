# ==========================================
# MISSION 2: MARKY MARK - Canada - 4002
# ==========================================
# This mission scores 2 things in one route:
#   - What's on Sale? (Mission 09) : Raise roof and market wares  = 30 pts
#   - Tip the Scales  (Mission 10) : Tip scale, remove scale pan  = 30 pts
#                                              TOTAL = 60 pts!
#
# ROBOT INFO
# Left wheel motor          : Port B (COUNTERCLOCKWISE)
# Right wheel motor         : Port F (CLOCKWISE)
# Front attachment motor    : Port A
# Back attachment motor     : Port E
# Color sensor (bottom)     : Port D - line following
# Color sensor (top)        : Port C - mission select by lego color (coming soon!)
#
# GEAR SETUP: 12t → 20t → 12t → 20t (two reduction stages!)
# Each stage: 20 ÷ 12 = 1.67
# Total ratio: 1.67 × 1.67 = 2.78:1
# Formula: motor degrees ÷ 2.78 = arm degrees
# Example: 350° on motor ÷ 2.78 = ~126° of actual arm movement
# The double reduction means EVEN MORE power - great for lifting!
# ==========================================

from pybricks.tools import wait, hub_menu, StopWatch
from pybricks.parameters import Stop

def run(robot, front_attachment, back_attachment):
    # Create the stopwatch
    timer = StopWatch()

    # Start/reset it
    timer.reset()

    #Turn off gyro for this route
    robot.use_gyro(False)

    # Set current arm position as zero / home before starting
    # This makes sure all the angles below are measured from the same spot every time
    front_attachment.reset_angle(0)

    # ---- DRIVE TO MARKET STALL ----
    # Drive forward 500mm toward the market stall
    robot.settings(straight_speed=500)
    robot.straight(500)

    # Drop the front arm down to knock down bucket
    # run_angle(speed, degrees)
    #   speed  : how fast the motor spins (max 1000)
    #   degrees: how far the motor rotates
    # 350° motor ÷ 2.78 = ~126° of actual arm movement
    front_attachment.run_angle(850, -350)   # speed=850 (fast), degrees=-350 (drop down)

    # Small turn right to fine tune alignment with the stall
    robot.turn(5)

    #Drop down ~11 more degrees to fully hook under the roof
    # 30 motor degrees ÷ 2.78 = ~11 degrees of actual arm movement
    front_attachment.run_angle(200, -30)   # slow speed for precision
    wait(200)                              # let the arm fully settle before moving

    # Nudge back slightly to get into position under the stall
    robot.settings(straight_speed=475)
    robot.straight(-40)

    # ---- RAISE THE MARKET STALL ----
    # Drive back slowly - this motion raises the market stall roof and wares
    robot.settings(straight_speed=225)
    robot.straight(-150)

    # Nudge forward slightly to release the latch on the stall
    robot.settings(straight_speed=475)
    robot.straight(50)

    # Raise the arm back up, releasing the market stall #this clicks a bit
    # 530° motor ÷ 2.78 = ~191° of actual arm movement
    front_attachment.run_angle(450, 500) #change from 500 for first number

    # ---- TIP THE SCALES ----
    # Drive back to reposition in front of the scales
    robot.settings(straight_speed=500)
    robot.straight(-105)

    #turn to garuntee table hit
    robot.turn(-15)

    # Drop arm down to engage with the scale mechanism
    # 650° motor ÷ 2.78 = ~234° of actual arm movement
    front_attachment.run_angle(1000, -650)

    # Swing arm back to pull off the scale pan
    # 400° motor ÷ 2.78 = ~144° of actual arm movement
    front_attachment.run_angle(-1000, -450)

    # ---- RETURN HOME ----
    # Turn left to aim back toward home base
    robot.turn(-25) #-40

    # Drive back to home base at full speed
    robot.settings(straight_speed=750)
    robot.straight(-640, Stop.COAST)

    #Turn Gyro Back On for Next Route
    robot.use_gyro(True)

    # Check how much time has passed (in milliseconds)
    #print(timer.time())  # prints milliseconds e.g. 1500 = 1.5 seconds
