from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Button, Direction
from pybricks.iodevices import XboxController
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the hub
hub = PrimeHub()
hub.display.text("INIT")

# ROBOT MOTOR SETUP:
# Port A - Left wheel (COUNTERCLOCKWISE)
# Port E - Right wheel (CLOCKWISE)
# Port B - Front attachment
# Port F - Back attachment
# Port D - Color sensor (bottom) - line following (not implemented)
# Port C - Color sensor (top) - mission select by lego color (not implemented)

# Initialize drive motors
left_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, positive_direction=Direction.CLOCKWISE)

# Initialize attachment motors
front_attach = Motor(Port.B)
back_attach = Motor(Port.F)

# Initialize Xbox controller
hub.display.text("CTRL")
controller = XboxController()
wait(1000)

# Drive base settings
wheel_diameter = 56  # mm (small spike prime wheels)
axle_track = 120     # mm (adjust if needed)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)
drive_base.use_gyro(True)

hub.display.text("READY")
wait(500)

# --- Main loop ---
while True:
    try:
        # Read controller input
        left_stick = controller.joystick_left()
        right_stick = controller.joystick_right()
        right_trigger, left_trigger = controller.triggers()
        buttons = controller.buttons.pressed()
        
        # Initialize speed and turn rate
        speed_forward = 0
        turn_rate = 0
        
        # Trigger control for straight movement
        if left_trigger > 0:
            speed_forward = -500  # Move straight backward
        elif right_trigger > 0:
            speed_forward = 500   # Move straight forward
        
        # Joystick control for turning and fine movement
        joystick_turn_rate = right_stick[0] * 2  # Scale joystick X-axis for turning
        joystick_speed_forward = left_stick[1] * 10 # Scale joystick Y-axis for forward/backward
        
        # If triggers are not pressed, use joystick for forward/backward speed
        if left_trigger == 0 and right_trigger == 0:
            speed_forward = joystick_speed_forward
        
        # Always apply joystick turn rate
        turn_rate = joystick_turn_rate
        
        # Ensure speed and turn rate are within limits
        turn_rate = max(-360, min(360, turn_rate))
        speed_forward = max(-1000, min(1000, speed_forward))
        
        # Apply drive base commands
        if abs(speed_forward) > 50 or abs(turn_rate) > 50:
            drive_base.drive(speed_forward, turn_rate)
        else:
            drive_base.stop()
        
        # FRONT ATTACHMENT CONTROLS (Port B)
        # A button = forward, B button = backward
        if Button.A in buttons:
            front_attach.run(800)
        elif Button.B in buttons:
            front_attach.run(-800)
        else:
            front_attach.stop()
        
        # BACK ATTACHMENT CONTROLS (Port F)
        # X button = forward, Y button = backward
        if Button.X in buttons:
            back_attach.run(800)
        elif Button.Y in buttons:
            back_attach.run(-800)
        else:
            back_attach.stop()
        
        # Display speed on hub
        hub.display.number(int(speed_forward / 100))
        
    except Exception as e:
        hub.display.text("ERR")
        wait(100)
    
    wait(20)