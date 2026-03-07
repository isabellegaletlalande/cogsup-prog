import expyriment

# Use DEVELOP MODE while testing
# expyriment.control.set_develop_mode(True)

# -------- 1. INITIALIZE EXPERIMENT --------

exp = expyriment.design.Experiment(name="Left Right RT Task")
expyriment.control.initialize(exp)

exp.data_variable_names = ["Block", "Trial", "Key", "RT"]       # assign variable names

# -------- 2. CREATE THE EXPERIMENTAL DESIGN --------

# Create first block
block = expyriment.design.Block(name="Main Block")

# Create trials
words = ["LEFT", "RIGHT", "LEFT", "RIGHT"]

for word in words:
    trial = expyriment.design.Trial()
    stim = expyriment.stimuli.TextLine(text=word)
    stim.preload()
    trial.add_stimulus(stim)
    block.add_trial(trial)

exp.add_block(block)

# -------- 3. START THE EXPERIMENT --------

expyriment.control.start()

# -------- 4. RUN THE TRIALS --------

for block in exp.blocks:
    for trial in block.trials:
        trial.stimuli[0].present()              # displays stimulus
        
        key, rt = exp.keyboard.wait(            # wait for keypress and measure RT                    
            [expyriment.misc.constants.K_LEFT,
             expyriment.misc.constants.K_RIGHT]
        )
        
        exp.data.add([block.name, trial.id, key, rt]) # save the data

# -------- 5. END EXPERIMENT --------

expyriment.control.end()                        # saves data file and event log, closes experiment