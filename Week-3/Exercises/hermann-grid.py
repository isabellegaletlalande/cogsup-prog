from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_YELLOW

# ---------- INITIALIZE EXPYRIMENT ------------ #

exp = design.Experiment(name = "Hermann grid")

control.set_develop_mode()

control.initialize(exp)
control.start()

#----------STIMULI------------

# PARAMETERS

rows = 10
cols = 12
sq_size = 50
gap = 10
sq_color = C_BLACK
bg_color = C_YELLOW

screen_w, screen_h = exp.screen.size

# GRID SIZE
grid_w = cols * sq_size + (cols -1) * gap
grid_h = rows * sq_size + (rows - 1) * gap

if grid_w > screen_w or grid_h > screen_h:
    raise ValueError("Grid does not fit on screen with current dimensions")

#--------CREATE STIMULI-------- 

# START POSITION (middle of screen)
start_x = -grid_w // 2 + sq_size // 2
start_y = -grid_h // 2 + sq_size // 2

# CREATE SQUARES
squares = []
for r in range(rows):
    for c in range(cols):
        x = start_x + c * (sq_size + gap)
        y = start_y + r * (sq_size + gap)
        squares.append(
            stimuli.Rectangle(size = (sq_size, sq_size),
                              position=(x, y),
                              colour=sq_color,
                              corner_anti_aliasing=10)
        )

# DRAW
exp.screen.colour = bg_color
exp.screen.clear()
for sq in squares:
   sq.present(False, False)
exp.screen.update()

# WAIT
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()