from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_WHITE, C_BLACK

# ---------- INITIALIZE EXPYRIMENT ------------ #

exp = design.Experiment(name = "Kanizsa square", background_colour = C_GREY)

# control.set_develop_mode()

control.initialize(exp)
control.start()

# --------- STIMULI ------------------- #

# Screen sizes
screen_w, screen_h = exp.screen.size
side = int(0.25*screen_w)      # square side relative to screen size
radius = int(0.05*screen_w)    # circle radius relative to screen size  

half = side // 2

# CIRCLES
corners = [(-half, - half), (half, -half), (-half, half), (half, half)]
colors = [C_BLACK, C_BLACK, C_WHITE, C_WHITE]

circles = []
for pos, color in zip(corners, colors):
    circles.append(
        stimuli.Circle(
            radius=radius,
            position=pos,
            colour=color,
            anti_aliasing=10
        )
    )

# SQUARE
square = stimuli.Rectangle(
    size=(side, side),
    colour=C_GREY,
    corner_anti_aliasing=10
)

#------RUN EXPERIMENT-------

# DRAW
exp.screen.clear()
for stim in circles + [square]:
    stim.present(False, False)
exp.screen.update()

# WAIT
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()

