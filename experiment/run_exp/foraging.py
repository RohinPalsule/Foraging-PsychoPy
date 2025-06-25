from psychopy import visual, core, event, data, sound,monitors
import random
import numpy as np
import csv
import sys 
import os
import yaml

# Load config
with open("study.yaml", "r") as f:
    config = yaml.safe_load(f)



# Initialize the window
# For scanner
monitor = monitors.Monitor("expMonitor", width=config['params']['SCREENWIDTH'])
monitor.setSizePix((config['params']['HRES'], config['params']['VRES']))
monitor.saveMon()

# win = visual.Window([config['params']['HRES'], config['params']['VRES']], allowGUI=True, monitor=monitor, units="norm", color="white", fullscr=True, screen=0)
win = visual.Window(fullscr=True, color='white',allowStencil=True,units = "norm")
experiment_clock = core.Clock()


# Debug and block length
debug = config.get("debug", False)
block_length = config["block_length_debug"] if debug else config["block_length"]

# Image prefix
image_prefix = config["image_prefix"]

# Define individual images
land_img = image_prefix + config["images"]["land"]
dig_img = image_prefix + config["images"]["dig"]
space_treasure_img = image_prefix + config["images"]["space_treasure"]
intro_gem_img = image_prefix + config["images"]["pink_gem"]
intro_ast = image_prefix + config["images"]["opening_img"]
barrel_img = image_prefix + config["images"]["barrel_text"]
hundred_img = image_prefix + config["images"]["gem_value"]
intro_travel = image_prefix + config["images"]["rocket_first"]
intro_alien = image_prefix + config["images"]["alien_intro"]
practice_alien = image_prefix + config["images"]["alien_practice"]
timeout_img = image_prefix + config["images"]["timeout"]
home_base = image_prefix + config["images"]["home_base"]

# Sequences
travel_sequence = [image_prefix + r for r in config["rocket_sequence"]]

# Randomized planets
planet_prefix = np.random.choice(np.arange(1,121), 120, replace=False)
planets = [image_prefix + f"aliens/alien_planet-{planet}.jpg" for planet in planet_prefix]
gem = 0
decay = None
alien_index = 0
prt_clock = core.Clock() # Initialized prt timer
block_time = 0
text_index = 0
failedNum = 0
dig_index = 0
dig_sequence = [image_prefix+"dig.jpg", image_prefix+"land.jpg", image_prefix+"dig.jpg"]
index = 0
first_planet = True

keyList = [config['params']['BUTTON_1'],config['params']['BUTTON_2']]

if len(sys.argv) < 2: # Call participant ID in terminal
    print("Error: No participant ID provided.")
    print("Usage: python3 experiment.py <participant_id>")
    sys.exit(1)  # Exit with error code 1

# Get participant ID from command-line argument
participant_id = sys.argv[1]

study = []

# For study.yaml output
def study_filename(subject_id_str):
    extension = ".yaml"
    if not subject_id_str:
        return 'study' + extension
    return 'study' + "." + str(subject_id_str) + extension

def write_study():
    if not participant_id:
        raise Exception("Shouldn't write to original study file! Please provide a valid subject ID.")
    with open(study_filename(participant_id), 'w') as file:
        for row in study:
            if isinstance(row.get("AlienOrder"), np.ndarray):
                row["AlienOrder"] = row["AlienOrder"].tolist()
        yaml.dump(study, file)

# Initial data format -- What the csv reader takes as column names
study.append({
    "ID": participant_id,
    "TrialType":f"InitializeStudy",
    "BlockNum": "",
    "AlienOrder": planet_prefix,
    "QuizResp": "",
    "QuizFailedNum": "",
    "TimeElapsed": experiment_clock.getTime(),
    "RT": "",
    "PRT": "",
    "Galaxy": "",
    "DecayRate": "",
    "AlienIndex": "",
    "GemValue": "",
    "TimeInBlock": ""
})
# init in case exp breaks
write_study()
# For practice quiz
questions = [
    "What affects the amount of bonus money you will earn?",
    "The length of this experiment",
    "You get to stay at home base as long as you like."
]

choices = [
    ["The number of planets you visit", "How long you stay at home base", "The number of gems you collect"],
    ["Depends on how many planets you've visited", "Is fixed", "Depends on how many gems you've collected"],
    ["True", "False"]
]

correct_answers = ["The number of gems you collect", "Is fixed", "False"]

# For decay rate
def rbeta(alpha, beta):
    """Generates a random number from a Beta distribution."""
    return np.random.beta(alpha, beta)

# Takes galaxy type to know which distribution to create (poor, neutral, rich)
def get_decay_rate(galaxy):
    """Returns a decay rate sampled from a Beta distribution based on the galaxy type."""
    galaxy_distributions = {
        0: (13, 51),  # Rich planet
        1: (50, 50),  # Neutral planet
        2: (50, 12)   # Poor planet
    }
    
    if galaxy in galaxy_distributions:
        alpha, beta = galaxy_distributions[galaxy]
        return rbeta(alpha, beta)
    else:
        raise ValueError("Galaxy index out of range. Must be 0, 1, or 2.")


galaxy = None # Galaxy is initialized later and can randomly start between planet types

# If first is true it randomly chooses a planet type but if not it uses the 80% stay 20% switch
def get_galaxy(first=False):
    global galaxy
    if first is True:
        galaxy = np.random.randint(0,3)
    else:
        percentNum = np.random.randint(1,11)
        if percentNum > 8:
            newGalaxy = galaxy
            while newGalaxy == galaxy:
                newGalaxy = np.random.randint(0,3)
            galaxy = newGalaxy
        

def show_text(text, duration=0, image_path=None,x=0.5,y=0.6,height=0.3,text_height=config['params']['FONT_SIZE'],home=False):
    """Displays a text message either until a key is pressed or for a specified duration (Default unlimited duration)"""
    global text_index,study,experiment_clock
    text_index += 1 # Used for trial data descriptions

    stim = visual.TextStim(win, text=text, color='black', height=text_height, pos=(0, height), wrapWidth=config['params']['TEXTBOX_WIDTH']) # Adds whatever text is called
    stim.draw() # Pushes it to screen

    # If there is an image (specified by image_path) it will show it on the screen
    if image_path:
        stim_image = visual.ImageStim(win, image=image_path, size=(x, y), pos=(0, -0.3))  # Adjust size as needed
        stim_image.draw()

    win.flip() # Resets screen
    if home: # Code for when they are at homebase, as there is a 1 minute timer that can be ended early with a keypress
        timer = core.Clock()
        while timer.getTime() < duration:
            keys = event.getKeys(keyList=["space"])
            if "space" in keys:
                break 
    else:
        if duration > 0: # Only timed instruction is for the too slow img
            core.wait(duration)
            study.append({
                "ID": "",
                "TrialType":f"too_slow",
                "BlockNum": "",
                "AlienOrder": "",
                "QuizResp": "",
                "QuizFailedNum": "",
                "TimeElapsed": experiment_clock.getTime(),
                "RT": "",
                "PRT": "",
                "Galaxy": "",
                "DecayRate": "",
                "AlienIndex": "",
                "GemValue": "",
                "TimeInBlock": ""
            }) 
        else:
            # Only keys taken in exp (need to change to specify which key to use)
            event.waitKeys(keyList=["space","a","l"])
            if home == False:
                study.append({
                    "ID": "",
                    "TrialType":f"Instruction_{text_index}",
                    "BlockNum": "",
                    "AlienOrder": "",
                    "QuizResp": "",
                    "QuizFailedNum": "",
                    "TimeElapsed": experiment_clock.getTime(),
                    "RT": "",
                    "PRT": "",
                    "Galaxy": "",
                    "DecayRate": "",
                    "AlienIndex": "",
                    "GemValue": "",
                    "TimeInBlock": ""
                })
            
# Function below is for moving on to real game or continuing practice
def show_button_text(text,height=0.3,text_height=config['params']['FONT_SIZE']):
    """Displays a text message either until a button is pressed or for a specified duration (Default unlimited duration)"""
    global text_index,experiment_clock,study
    text_index += 1
    
    stim = visual.TextStim(win, text=text, color='black', height=text_height, pos=(0, height), wrapWidth=config['params']['TEXTBOX_WIDTH'])

    button1 = visual.Rect(win, width=0.3, height=0.1, pos=(-0.3, -0.1), fillColor='gray')
    button2 = visual.Rect(win, width=0.3, height=0.1, pos=(0.3, -0.1), fillColor='gray')

    label1 = visual.TextStim(win, text="Practice game again", pos=(-0.3, -0.1), color='black', height=0.04)
    label2 = visual.TextStim(win, text="Move on to the real game", pos=(0.3, -0.1), color='black', height=0.04)

    mouse = event.Mouse()

    while True:
        button1.draw()
        button2.draw()
        label1.draw()
        label2.draw()
        stim.draw()
        win.flip()
        if mouse.isPressedIn(button1): # When practice is chosen again
            study.append({
                "ID": "",
                "TrialType":f"Instruction_{text_index}",
                "BlockNum": "",
                "AlienOrder": "",
                "QuizResp": "",
                "QuizFailedNum": "",
                "TimeElapsed": experiment_clock.getTime(),
                "RT": "",
                "PRT": "",
                "Galaxy": "",
                "DecayRate": "",
                "AlienIndex": "",
                "GemValue": "",
                "TimeInBlock": ""
            })
            # Show the practice sequence again and then when they travel show this same button text
            dig_instruction(gems=barrel_img)
            show_button_text("Now that you know how to dig for space treasure and travel to new planets, you can start exploring the universe!\n\nDo you want to play the practice game again or get started with the real game?")
            break
        elif mouse.isPressedIn(button2): # When moving to the main game
            study.append({
                "ID": "",
                "TrialType":f"Instruction_{text_index}",
                "BlockNum": "",
                "AlienOrder": "",
                "QuizResp": "",
                "QuizFailedNum": "",
                "TimeElapsed": experiment_clock.getTime(),
                "RT": "",
                "PRT": "",
                "Galaxy": "",
                "DecayRate": "",
                "AlienIndex": "",
                "GemValue": "",
                "TimeInBlock": ""
            })
            break # Continue to next function

# Shows an image for some duration
def show_image(img_path, duration=1.5):
    """Displays an image for a given duration"""
    stim = visual.ImageStim(win, image=img_path,size=(1.2,1.2))
    stim.draw()
    win.flip()
    core.wait(duration)

# Function for digging gems and the subseqent trials
def show_animation(images, frame_time=0.667,test=False,gem_img=hundred_img):
    """Displays an animation sequence by flipping through images."""
    global decay,gem,galaxy,study,experiment_clock,dig_index,first_planet,prt_clock

    for img in images: # Flips through img in images at speed frame_time
        stim = visual.ImageStim(win, image=img, size=(1.2,1.2))
        stim.draw()
        win.flip()
        core.wait(frame_time)
    stim = visual.ImageStim(win, image=gem_img, size=(1.2,1.2)) # After animation shows image with gems with img path gem_img
    stim.draw()
    win.flip()
    core.wait(1.5)
    if test == False: # Test is for the instruction digging trial, not practice nor main phase
        stim = visual.ImageStim(win, image=land_img, size=(1.2,1.2)) # After animation shows image with gems with img path gem_img
        stim.draw()
        response_clock = core.Clock() # for rt data collection
        if first_planet:
            prt_clock = core.Clock() # Turns on prt timer when the first visit to the planet occurs
        stim = visual.TextStim(win, text="Dig here or travel to a new planet?", color='black', height=0.07, pos=(0, 0.7), wrapWidth=config['params']['TEXTBOX_WIDTH'])
        stim.draw()
        win.flip()
        keys = event.waitKeys(maxWait=2,keyList= keyList,timeStamped = response_clock) # can only take a or l
        if keys:
            key,RT = keys[0] # RT used for data collection
            if keyList[0] in key: # Dig more
                if decay: # practice trials do not have decay
                    first_planet= False # Switch first planet off for next trials
                    dig_index +=1
                    study.append({
                        "ID": "",
                        "TrialType":f"Dig_Trial_{dig_index}",
                        "BlockNum": "",
                        "AlienOrder": "",
                        "QuizResp": "",
                        "QuizFailedNum": "",
                        "TimeElapsed": experiment_clock.getTime(),
                        "RT": RT,
                        "PRT": "",
                        "Galaxy": "",
                        "DecayRate": "",
                        "AlienIndex": "",
                        "GemValue": gem, # Initial gem value set in block_loop
                        "TimeInBlock": ""
                    })
                    gem = round(decay*gem) # Adds decay to next gem value for following trial
                    gem_path = image_prefix + f"gems/{gem}.jpg"
                    dig_instruction(gems=gem_path) # Loops to new trial
                else:
                    dig_instruction(gems=gem_img) # This is for practice trials since only shows barrel img
            if keyList[1] in key: # If they travel
                    if decay:
                        study.append({
                            "ID": "",
                            "TrialType":f"Travel_Trial",
                            "BlockNum": "",
                            "AlienOrder": "",
                            "QuizResp": "",
                            "QuizFailedNum": "",
                            "TimeElapsed": experiment_clock.getTime(),
                            "RT": RT,
                            "PRT": prt_clock.getTime(),
                            "Galaxy": "",
                            "DecayRate": "",
                            "AlienIndex": "",
                            "GemValue": gem,
                            "TimeInBlock": ""
                        })
                    else:
                        study.append({
                            "ID": "",
                            "TrialType":f"Practice_Trial",
                            "BlockNum": "",
                            "AlienOrder": "",
                            "QuizResp": "",
                            "QuizFailedNum": "",
                            "TimeElapsed": experiment_clock.getTime(),
                            "RT": RT,
                            "PRT": "",
                            "Galaxy": "",
                            "DecayRate": "",
                            "AlienIndex": "",
                            "GemValue": "",
                            "TimeInBlock": ""
                        })
                    travel_trial() # Travel animation function
        else:
            too_slow() # Run out of time
            study.append({
                "ID": "",
                "TrialType":f"Too_slow",
                "BlockNum": "",
                "AlienOrder": "",
                "QuizResp": "",
                "QuizFailedNum": "",
                "TimeElapsed": experiment_clock.getTime(),
                "RT": "NA",
                "PRT": "",
                "Galaxy": "",
                "DecayRate": "",
                "AlienIndex": "",
                "GemValue": gem,
                "TimeInBlock": ""
            })
            if decay: # If there is decay show the next gem value
                gem = round(decay*gem)
                gem_path = image_prefix + f"gems/{gem}.jpg"
                dig_instruction(gems=gem_path)  
            else: # If not just show the barrel again
                dig_instruction(gems=gem_img)
    else:
        prt_clock = core.Clock() # Meant to intiialize 
        study.append({
            "ID": "",
            "TrialType":f"Dig_Instruct",
            "BlockNum": "",
            "AlienOrder": "",
            "QuizResp": "",
            "QuizFailedNum": "",
            "TimeElapsed": experiment_clock.getTime(),
            "RT": "",
            "PRT": "",
            "Galaxy": "",
            "DecayRate": "",
            "AlienIndex": "",
            "GemValue": "",
            "TimeInBlock": ""
        })
        win.flip()
        core.wait(1)

# Timeout image for 2 seconds
def too_slow():
    show_image(timeout_img,duration=2)

# Function where show animation is nested -- added for earlier versions but can look into removing
def dig_instruction(practice=False,gems=hundred_img):
    show_animation(dig_sequence, frame_time=0.667,test=practice,gem_img=gems)

# Rocket travel trials
def travel_trial():
    """Simulates travel sequence"""
    global study
    for img in travel_sequence: # Animates through all images and then waits 1 sec after for 10 sec total
        stim = visual.ImageStim(win, image=img, size=(1.2,1.2))
        stim.draw()
        win.flip()
        core.wait(1)
    core.wait(1)
    study.append({
        "ID": "",
        "TrialType":f"Travel_Planet",
        "BlockNum": "",
        "AlienOrder": "",
        "QuizResp": "",
        "QuizFailedNum": "",
        "TimeElapsed": experiment_clock.getTime(),
        "RT": "",
        "PRT": "",
        "Galaxy": "",
        "DecayRate": "",
        "AlienIndex": "",
        "GemValue": "",
        "TimeInBlock": ""
    })
    win.flip()

# For the practice quiz
def run_quiz(questions,choices,correct_answers):
    """Displays a multiple-choice quiz and checks answers."""
    global failedNum
    form_items = []
    win.units = "height" # Quizzes in psychopy need to have units of height, but this is changed at end of quiz
    for i in range(len(questions)):
        form_items.append(
            {"itemText": questions[i], "type": "radio", "options": choices[i]}
        )
    form = visual.Form(win, items=form_items, size=(1.1, 0.8), pos=(0, 0), itemPadding=0.1,units="height")

    # Display quiz and wait for responses
    while not form.complete:
        form.draw()
        win.flip()
        keys = event.getKeys(keyList=['return', 'escape'])

    # Get responses
    answers = form.getData()
    responses = [answers[i]['response'] for i in range(len(questions))]
    # Check correctness
    correct = True
    for i in range(len(responses)):
        if responses[i] != correct_answers[i]:
            correct = False
            break  # Stop checking once an incorrect answer is found
    study.append({
        "ID": "",
        "TrialType":f"practice_quiz",
        "BlockNum": "",
        "AlienOrder": "",
        "QuizResp": responses,
        "QuizFailedNum": failedNum,
        "TimeElapsed": experiment_clock.getTime(),
        "RT": "",
        "PRT": "",
        "Galaxy":"",
        "DecayRate": "",
        "AlienIndex": "",
        "GemValue": "",
        "TimeInBlock": ""
    })
    # Provide feedback based on correctness
    if correct==True:
        feedback_text = "Correct! Press SPACE to continue."
        # Show feedback
        feedback = visual.TextStim(win, text=feedback_text, color='black', height=0.07) # Show correct or incorrect
        feedback.draw()
        win.flip()
        win.units = "norm" # Change units back
        event.waitKeys(keyList=config['params']['BUTTON_NEXTPHASE'])
    else:
        feedback_text = "Incorrect. Press SPACE to reread the instructions and ry again."
        failedNum +=1 # log how many times they fail the quiz
        feedback = visual.TextStim(win, text=feedback_text, color='black', height=0.07)
        feedback.draw()
        win.flip()
        win.units = "norm" # Change units back
        event.waitKeys(config['params']['BUTTON_3'])
        repeat_inst() # Repeat initial instructions along with quiz



# Repeat instructions if they fail the quiz
def repeat_inst():
    show_text("Howdy! In this experiment, you’ll be an explorer traveling through space to collect space treasure. Your mission is to collect as much treasure as possible. Press the space bar to begin reading the instructions!",image_path=intro_ast,y=0.7,x=0.4)
    show_text("As a space explorer, you’ll visit different planets to dig for space treasure, these pink gems. The more space treasure you mine, the more bonus payment you’ll win! \n\n[Press the space bar to continue]",image_path=intro_gem_img)
    show_text("When you’ve arrived at a new planet, you will dig once.\n\nThen, you get to decide if you want to stay on the planet and dig again or travel to a new planet and dig there. \n\nTo stay and dig, press the letter ‘A’ on the keyboard. Try pressing it now!",image_path=land_img,height=0.6,x=1,y=1)
    dig_instruction(practice=True)
    show_text("The longer you mine a planet the fewer gems you’ll get with each dig.\n\nWhen gems are running low, you may want to travel to a new planet that hasn’t been overmined.\n\nPlanets are very far apart in this galaxy, so it will take some time to travel between them.\n\nThere are lots and lots of planets for you to visit, so you won’t be able to return to any planets you’ve already visited.\n\nTo leave this planet and travel to a new one, press the letter ‘L’ on the keyboard. Try pressing it now!",image_path=intro_travel,height=0.6,x=0.8,y=0.8,text_height=0.05)
    travel_trial()
    show_text("When you arrive at a new planet, an alien from that planet will greet you!\n\n[Press the space bar to continue]",image_path=intro_alien,height=0.6,y=1,x=1)
    show_text("If you’re not fast enough in making a choice, you’ll have to wait a few seconds before you can make another one.\n\nYou can’t dig for more gems or travel to new planets. You just have to sit and wait.\n\n[Press the space bar to continue]",image_path=timeout_img,height=0.5,x=1,y=1)
    show_text("After digging and traveling for a while, you’ll be able to take a break at home base.\n\nYou can spend at most 1 minute at home base — there are still a lot of gems left to collect!\n\nYou will spend 30 minutes mining gems and traveling to new planets no matter what.\n\nYou will visit home base every 6 minutes, so, you will visit home base four times during the game.\n\n[Press the space bar to continue]",image_path=home_base,height=0.5,x=1,y=1,text_height=0.05)
    run_quiz(questions=questions,choices=choices,correct_answers=correct_answers)

# 1 minute rest at homebase for breaks
def rest_homebase():
    """When participants need to rest at homebase"""
    global study,experiment_clock,block_time
    show_text(text="You have been traveling for a while. Time to take a rest at home base!\n\nWhen you are ready to move one, press the space bar. You have up to a minute of rest.",height=0.5,image_path=home_base,x=1,y=1,duration=60,home=True)
    show_text("The task is continuing now",height=0,duration=1.5)
    study.append({
        "ID": "",
        "TrialType":f"home_base",
        "BlockNum": "",
        "AlienOrder": "",
        "QuizResp": "",
        "QuizFailedNum": "",
        "TimeElapsed": experiment_clock.getTime(),
        "RT": "",
        "PRT": "",
        "Galaxy":"",
        "DecayRate": "",
        "AlienIndex": "",
        "GemValue": "",
        "TimeInBlock": block_time # Block time is fixed from block_loop
    })

# Where the main task is run
def block_loop(blockNum):
    """Main task loop divided into blocks"""
    global gem,decay,alien_index,study,first_planet,block_time
    first_trial = True # Initial switch for first_trial
    timer = core.Clock() # Timer for each block
    while timer.getTime() < block_length: # Loop runs for as long as the timer is under block_length
        first_planet = True
        if alien_index >= len(planets): # If they get through all the aliens it restarts
            alien_index = 0
        if first_trial:
            get_galaxy(first=True) # Get first galaxy type
        else:
            get_galaxy() # Get galaxy types with 80/20 distribution
        first_trial = False
        # Initial decay rate and gem selection
        decay = get_decay_rate(galaxy=galaxy)
        gem = round(np.max([np.min([np.random.normal(100,5),135]),0]))
        gem_path = image_prefix + f"gems/{gem}.jpg"
        study.append({
            "ID": "",
            "TrialType":f"start_loop",
            "BlockNum": blockNum,
            "AlienOrder": "",
            "QuizResp": "",
            "QuizFailedNum": "",
            "TimeElapsed": experiment_clock.getTime(),
            "RT": "",
            "PRT": "",
            "Galaxy": galaxy,
            "DecayRate": decay,
            "AlienIndex": alien_index,
            "GemValue": "",
            "TimeInBlock": ""
        })
        show_image(img_path=planets[alien_index],duration=5) # Show the first alien welcome
        dig_instruction(gems=gem_path) # And first digging trial done automatically
        alien_index += 1
        
    block_time = timer.getTime() # when timer goes above block_length it logs the time
    write_study()
    win.flip()
    core.wait(1)

# How data is saved to CSV
def save_data(participant_id, trials):
    """Save collected data to a CSV file, automatically detecting headers."""
    folder_name = "data"
    os.makedirs(folder_name, exist_ok=True)  # Uses data directory and checks if it exists before adding

    filename = os.path.join(folder_name, f"participant_{participant_id}.csv") # Data is saved under the id

    if not trials: # checks if it is empty
        print("No trial data to save.")
        return 

    headers = trials[0].keys()  # Header is first study keys (should be consistent accross study calls)

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        
        for trial in trials: # Every row is a trial
            writer.writerow(trial) 

    print(f"Data saved to {filename}") # Confirmation that data saved



# Main experiment flow

show_text("Howdy! In this experiment, you’ll be an explorer traveling through space to collect space treasure. Your mission is to collect as much treasure as possible. Press the space bar to begin reading the instructions!",image_path=intro_ast,y=0.7,x=0.4)

show_text("As a space explorer, you’ll visit different planets to dig for space treasure, these pink gems. The more space treasure you mine, the more bonus payment you’ll win! \n\n[Press the space bar to continue]",image_path=intro_gem_img)

show_text("When you’ve arrived at a new planet, you will dig once.\n\nThen, you get to decide if you want to stay on the planet and dig again or travel to a new planet and dig there. \n\nTo stay and dig, press the letter ‘A’ on the keyboard. Try pressing it now!",image_path=land_img,height=0.6,x=1,y=1)

dig_instruction(practice=True)

show_text("The longer you mine a planet the fewer gems you’ll get with each dig.\n\nWhen gems are running low, you may want to travel to a new planet that hasn’t been overmined.\n\nPlanets are very far apart in this galaxy, so it will take some time to travel between them.\n\nThere are lots and lots of planets for you to visit, so you won’t be able to return to any planets you’ve already visited.\n\nTo leave this planet and travel to a new one, press the letter ‘L’ on the keyboard. Try pressing it now!",image_path=intro_travel,height=0.6,x=0.8,y=0.8,text_height=0.05)

travel_trial()

show_text("When you arrive at a new planet, an alien from that planet will greet you!\n\n[Press the space bar to continue]",image_path=intro_alien,height=0.6,y=1,x=1)

show_text("If you’re not fast enough in making a choice, you’ll have to wait a few seconds before you can make another one.\n\nYou can’t dig for more gems or travel to new planets. You just have to sit and wait.\n\n[Press the space bar to continue]",image_path=timeout_img,height=0.5,x=1,y=1)

show_text("After digging and traveling for a while, you’ll be able to take a break at home base.\n\nYou can spend at most 1 minute at home base — there are still a lot of gems left to collect!\n\nYou will spend 30 minutes mining gems and traveling to new planets no matter what.\n\nYou will visit home base every 6 minutes, so, you will visit home base four times during the game.\n\n[Press the space bar to continue]",image_path=home_base,height=0.5,x=1,y=1,text_height=0.05)

run_quiz(questions=questions,choices=choices,correct_answers=correct_answers)

show_text("Now, you'll play a practice game, so you can practice mining space treasure and traveling to new planets.\n\nIn the practice game, you'll be digging up barrels of gems. But, in the real game, you'll be digging up the gems themselves.\n\nPress the space bar to begin practice!", height=0)

show_image(img_path=practice_alien,duration=5)
dig_instruction(gems=barrel_img)

show_button_text(text="Now that you know how to dig for space treasure and travel to new planets, you can start exploring the universe!\n\nDo you want to play the practice game again or get started with the real game?")

block_loop(1)
rest_homebase()

block_loop(2)
rest_homebase()

block_loop(3)
rest_homebase()

block_loop(4)
rest_homebase()

block_loop(5)

#Save data
save_data(participant_id, study)

show_text("Thank you for participating! Press SPACE to exit.")

win.close()
core.quit()
