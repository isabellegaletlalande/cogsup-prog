# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_RED

# ---1. Global settings---

exp = design.Experiment(name = "Display Edges")
control.set_develop_mode()
control.initialize(exp)

# 2.---Stimuli---

width, height = exp.screen.size

square_w = int(0.05*width)
square_h = int(0.05*height)

half_square_w = square_w // 2
half_square_h = square_h // 2

half_screen_w = width // 2
half_screen_h = height // 2

# Positions

# Positions (offset so squares stay fully on screen)

top_left_pos = (-half_screen_w + half_square_w,  half_screen_h - half_square_h)
top_right_pos = ( half_screen_w - half_square_w,  half_screen_h - half_square_h)
bottom_left_pos = (-half_screen_w + half_square_w, -half_screen_h + half_square_h)
bottom_right_pos = (half_screen_w - half_square_w, -half_screen_h + half_square_h)

square_top_left = stimuli.Rectangle((square_w, square_h), C_RED, position=top_left_pos, line_width=1)
square_top_right = stimuli.Rectangle((square_w, square_h), C_RED, position=top_right_pos, line_width=1)
square_bottom_left = stimuli.Rectangle((square_w, square_h), C_RED, position=bottom_left_pos, line_width=1)
square_bottom_right = stimuli.Rectangle((square_w, square_h), C_RED, position=bottom_right_pos, line_width=1)

#---3. Run experiment---

control.start(subject_id=1)

# Plot all squares
square_top_left.present(clear = True, update = False)
square_top_right.present(clear = False, update = False)
square_bottom_left.present(clear = False, update = False)
square_bottom_right.present(clear = False, update = True)

exp.keyboard.wait()

control.end()