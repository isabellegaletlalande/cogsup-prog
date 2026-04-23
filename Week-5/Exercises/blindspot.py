from expyriment import design, control, stimuli

from expyriment.misc.constants import (C_WHITE, C_BLACK, K_SPACE, K_1, K_2, K_DOWN, K_UP, K_LEFT, K_RIGHT)

# List the keys the participant is allowed to use
KEYS = [K_1, K_2, K_UP, K_DOWN, K_RIGHT, K_LEFT, K_SPACE]

# Set how much the circle radius changes each time
ADJUST_RADIUS = 5

# Set how far the circle moves with each arrow key press
STEP_SIZE = 5

# Match each key to:
# 1. a readable name
# 2. the type of change
# 3. the amount of change
KEYMAP = {
    K_1: ("1", "radius", -ADJUST_RADIUS),
    K_2: ("2", "radius", +ADJUST_RADIUS),
    K_DOWN: ("down", "move", (0, -STEP_SIZE)),
    K_UP: ("up", "move", (0, +STEP_SIZE)),
    K_LEFT: ("left", "move", (-STEP_SIZE, 0)),
    K_RIGHT: ("right", "move", (+STEP_SIZE, 0)),
}

# Create the instructions shown at the start of each trial
INSTRUCTION_TEMPLATE = """
While looking at the cross with your {eye_closed} eye closed, adjust the circle's
position (arrow keys) and size (1 smaller, 2 bigger) until you can no longer see it.

When the circle becomes invisible, press SPACE.
Press any key to begin.
"""

# Create the experiment and set the screen colours
exp = design.Experiment(
    name="Blindspot",
    background_colour=C_WHITE,
    foreground_colour=C_BLACK
)

# Define the column names for the data file
exp.add_data_variable_names(["eye", "keypress", "radius", "x_coord", "y_coord"])

# Use develop mode for easier testing
control.set_develop_mode()

# Initialize the experiment and open the screen
control.initialize(exp)

# Create a function that makes the instruction screen
def make_instructions(eye):
    # Decide which eye should be closed
    eye_closed = "left" if eye == "right" else "right"

    # Build the text screen with the correct instructions
    screen = stimuli.TextScreen(
        heading="Instructions",
        text=INSTRUCTION_TEMPLATE.format(eye_closed=eye_closed),
        text_justification=0
    )

    # Preload the instruction screen to make presentation smoother
    screen.preload()

    # Return the finished instruction screen
    return screen

# Create a function that makes a circle stimulus
def make_circle(radius, pos=(0, 0)):
    # Create a circle with a given size and position
    circle = stimuli.Circle(radius, position=pos, anti_aliasing=10)

    # Preload the circle before showing it
    circle.preload()

    # Return the finished circle
    return circle

# Create a function that runs one trial
def run_trial(eye, radius=75):
    # Show the instructions for this eye
    make_instructions(eye).present()

    # Wait for the participant to press a key to start
    exp.keyboard.wait()

    # Put the fixation cross on the correct side of the screen
    fixation_pos = (300, 0) if eye == "left" else (-300, 0)

    # Create the fixation cross
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=fixation_pos)

    # Preload the fixation cross
    fixation.preload()

    # Create the starting circle
    circle = make_circle(radius)

    # Keep running until the participant presses SPACE
    while True:
        # Draw the fixation cross first
        fixation.present(clear=True, update=False)

        # Draw the circle on top and update the screen
        circle.present(clear=False, update=True)

        # Wait for one of the allowed keys
        key, _ = exp.keyboard.wait(KEYS)

        # If SPACE is pressed, end the trial
        if key == K_SPACE:
            break

        # Look up what the pressed key should do
        keypress, action, change = KEYMAP[key]

        # If the key is an arrow key, move the circle
        if action == "move":
            circle.move(change)

        # If the key is 1 or 2, change the circle size
        else:
            radius = max(1, radius + change)
            circle = make_circle(radius, circle.position)

        # Get the circle's current x and y position
        x, y = circle.position

        # Save the current trial data after this key press
        exp.data.add([eye, keypress, radius, x, y])

# Start the experiment session
control.start(subject_id=1)

# Run one trial for the right eye and one for the left eye
for eye in ["right", "left"]:
    run_trial(eye)

# End the experiment cleanly
control.end()
