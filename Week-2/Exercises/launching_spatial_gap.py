# Import the main modules of expyriment
from expyriment import design, control, stimuli, misc

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Launching")

# Enable developer mode 
control.set_develop_mode()

# Initialize the experiment
control.initialize(exp)

# Create red square starting 400px left from centre
square_1 = stimuli.Rectangle(
    size=(50,50), 
    colour=(255, 0, 0), 
    position = (-400, 0)
)

# Create green square starting at centre
square_2 = stimuli.Rectangle(
    size=(50,50), 
    colour=(0, 255, 0), 
    position = (0, 0)
)

# Start running the experiment
control.start(subject_id=1)

#-----------------------------------------
# 1. Show both squares on screen
#-----------------------------------------

square_1.present(clear=True, update=False)
square_2.present(clear=False, update=True)

# Show for 1 second
misc.Clock().wait(1000)

#-----------------------------------------
# 2. Move red square towards green
#-----------------------------------------

speed = 5 # pixels per frame
gap = 20 # add a gap
collision_point = -50 - gap


# Point of collision where red square centered on x =-50
while square_1.position[0] < collision_point:
    # Move red square right
    square_1.move((speed, 0))

    # Redraw both squares
    square_1.present(clear=True, update=False)
    square_2.present(clear=False, update=True)

    exp.clock.wait(10)

#-----------------------------------------
# 3. Move green square right
#-----------------------------------------

# Calculate number of frames moved by red
distance  = 350 # from -400 to -50
frames = distance // speed

for i in range(frames):
    square_2.move((speed,0))

    square_1.present(clear=True, update=False)
    square_2.present(clear=False, update=True)

    exp.clock.wait(10)

# Leave it on-screen for 1s
exp.clock.wait(1000)

# End experiment
control.end()