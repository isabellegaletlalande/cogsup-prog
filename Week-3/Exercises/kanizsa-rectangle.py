from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_WHITE, C_BLACK

# ---------- INITIALIZE EXPYRIMENT ------------ #

exp = design.Experiment(name = "Kanizsa rectangle", background_colour = C_GREY)

control.set_develop_mode()

control.initialize(exp)
control.start()

# --------- STIMULI ------------------- #

def kanizsa_rectangle(aspect_ratio, rect_scale, circle_scale):
    screen_w, _= exp.screen.size

    width = int(rect_scale * screen_w)
    height = int(width / aspect_ratio)

    half_w = width // 2
    half_h = height // 2

    radius = int(circle_scale * screen_w)
    
    corners = [(-half_w, -half_h), (half_w, -half_h), (-half_w, half_h), (half_w, half_h)]
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

    rectangle = stimuli.Rectangle(
        size=(width, height),
        colour=C_GREY,
        corner_anti_aliasing=10
    )    
    
    return circles + [rectangle]

stim_list = kanizsa_rectangle(aspect_ratio=1, rect_scale=0.30, circle_scale=0.08)

# DRAW
exp.screen.clear()
for stim in stim_list:
    stim.present(False, False)
exp.screen.update()

# WAIT
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()