from expyriment import design, control, stimuli

# Create a new experiment called "timing puzzle".
exp = design.Experiment(name="timing puzzle")
control.set_develop_mode()

# Initialize the experiment and open the display window.
control.initialize(exp)

# Create a fixation cross stimulus.
fixation = stimuli.FixCross()

# Create a text stimulus that will replace the fixation cross.
text = stimuli.TextLine("Fixation removed")

# Show the fixation cross on screen.
fixation.present()

# Record the time immediately after the fixation appears.
t0 = exp.clock.time

# Wait for 1000 milliseconds (1 second).
exp.clock.wait(1000)

# Replace the fixation cross with the text message.
text.present()

# Record the time immediately after the text appears.
t1 = exp.clock.time

# Compute how long the fixation stayed visible, in seconds.
fix_duration = (t1 - t0)/1000

# Keep the replacement text on screen for another second.
exp.clock.wait(1000)

# Choose the correct singular or plural word for the output.
units = "second" if fix_duration == 1.0 else "seconds"

# Build the result message showing the measured fixation duration.
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

# Create a new text stimulus containing the result message.
text2 = stimuli.TextLine(duration_text)

# Show the result message on screen.
text2.present()

# Keep the result message visible for 2 seconds.
exp.clock.wait(2000)

# End the experiment cleanly.
control.end()
