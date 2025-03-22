from psychopy import visual, core, event, data, sound
import random
import numpy as np
import csv
import sys 

# Initialize the window
debug = True

win = visual.Window(fullscr=True, color='white',allowStencil=True,units = "norm")
experiment_clock = core.Clock()
if debug:
    block_length = 30
else:
    block_length = 360
# Define stimuli images
image_prefix = "../run_exp/static/images/task_images/"
land_img = image_prefix + "land.jpg"
dig_img = image_prefix + "dig.jpg"
space_treasure_img = image_prefix + "gems/100.jpg"
example_gem_sequence = [image_prefix + "gems/100.jpg",image_prefix + "gems/84.jpg",image_prefix + "gems/73.jpg",image_prefix + "gems/63.jpg",image_prefix + "gems/41.jpg",image_prefix + "gems/12.jpg"]
travel_sequence = []
for i in range(1,10):
    travel_sequence.append(image_prefix+f"rocket-0{i}.jpg")
intro_gem_img = image_prefix + "pink_gem.jpg"
intro_ast = image_prefix + "opening_img-01.jpg"
barrel_img = image_prefix + "barrel_text.jpg"
hundred_img = image_prefix + "gems/100.jpg"
intro_travel = image_prefix + "rocket-01.jpg"
intro_alien = image_prefix + "aliens/alien_planet-125.jpg"
practice_alien = image_prefix + "aliens/alien_planet-124.jpg"
timeout_img = image_prefix + "time_out.jpg"
home_base = image_prefix + "home_base.jpg"
planets = []
planet_prefix = np.random.choice(np.arange(1,121),120,replace=False)
for planet in planet_prefix:
    planets.append(image_prefix + f"aliens/alien_planet-{planet}.jpg")
gem = 0
decay = None
alien_index = 0
prt_clock = core.Clock()

if len(sys.argv) < 2:
    print("Error: No participant ID provided.")
    print("Usage: python3 experiment.py <participant_id>")
    sys.exit(1)  # Exit with error code 1

# Get participant ID from command-line argument
participant_id = sys.argv[1]

study = []

study.append({
    "ID": participant_id,
    "TrialType":f"InitializeStudy",
    "AlienOrder": planet_prefix,
    "TimeElapsed": experiment_clock.getTime(),
    "RT": "",
    "PRT": "",
    "Galaxy": "",
    "DecayRate": "",
    "AlienIndex": "",
    "GemValue": ""
})

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

def rbeta(alpha, beta):
    """Generates a random number from a Beta distribution."""
    return np.random.beta(alpha, beta)

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
        
text_index = 0

def show_text(text, duration=0, image_path=None,x=0.5,y=0.6,height=0.3,text_height=0.07,home=False):
    """Displays a text message either until a key is pressed or for a specified duration (Default unlimited duration)"""
    global text_index,study,experiment_clock
    text_index += 1

    stim = visual.TextStim(win, text=text, color='black', height=text_height, pos=(0, height), wrapWidth=1.5)
    stim.draw()

    if image_path:
        stim_image = visual.ImageStim(win, image=image_path, size=(x, y), pos=(0, -0.3))  # Adjust size as needed
        stim_image.draw()

    win.flip()
    if home:
        timer = core.Clock()
        while timer.getTime() < duration:
            keys = event.getKeys(keyList=["space"])
            if "space" in keys:
                break 
    else:
        if duration > 0:
            core.wait(duration)
            study.append({
                "ID": "",
                "TrialType":f"too_slow",
                "AlienOrder": "",
                "TimeElapsed": experiment_clock.getTime(),
                "RT": "",
                "PRT": "",
                "Galaxy": "",
                "DecayRate": "",
                "AlienIndex": "",
                "GemValue": ""
            })
           
        else:
            event.waitKeys(keyList=["space","a","l"])
            if text_index < 10:
                study.append({
                    "ID": "",
                    "TrialType":f"Instruction_{text_index}",
                    "AlienOrder": "",
                    "TimeElapsed": experiment_clock.getTime(),
                    "RT": "",
                    "PRT": "",
                    "Galaxy": "",
                    "DecayRate": "",
                    "AlienIndex": "",
                    "GemValue": ""
                })
            else:
                study.append({
                    "ID": "",
                    "TrialType":f"Home_Base",
                    "AlienOrder": "",
                    "TimeElapsed": experiment_clock.getTime(),
                    "RT": "",
                    "PRT": "",
                    "Galaxy": "",
                    "DecayRate": "",
                    "AlienIndex": "",
                    "GemValue": ""
                })

def show_button_text(text,height=0.3,text_height=0.07):
    """Displays a text message either until a button is pressed or for a specified duration (Default unlimited duration)"""
    global text_index,experiment_clock,study
    text_index += 1
    
    stim = visual.TextStim(win, text=text, color='black', height=text_height, pos=(0, height), wrapWidth=1.5)

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
        if mouse.isPressedIn(button1):
            study.append({
                "ID": "",
                "TrialType":f"Instruction_{text_index}",
                "AlienOrder": "",
                "TimeElapsed": experiment_clock.getTime(),
                "RT": "",
                "PRT": "",
                "Galaxy": "",
                "DecayRate": "",
                "AlienIndex": "",
                "GemValue": ""
            })
            dig_instruction(gems=barrel_img)
            show_button_text("Now that you know how to dig for space treasure and travel to new planets, you can start exploring the universe!\n\nDo you want to play the practice game again or get started with the real game?")
            break
        elif mouse.isPressedIn(button2):
            study.append({
                "ID": "",
                "TrialType":f"Instruction_{text_index}",
                "AlienOrder": "",
                "TimeElapsed": experiment_clock.getTime(),
                "RT": "",
                "PRT": "",
                "Galaxy": "",
                "DecayRate": "",
                "AlienIndex": "",
                "GemValue": ""
            })
            break

def get_keyboard_response(valid_keys, timeout=2):
    """Waits for a keyboard response within a given time"""
    timer = core.Clock()
    keys = event.waitKeys(maxWait=timeout, keyList=valid_keys, timeStamped=timer)
    return keys

def show_image(img_path, duration=1.5):
    """Displays an image for a given duration"""
    stim = visual.ImageStim(win, image=img_path,size=(1.2,1.2))
    stim.draw()
    win.flip()
    core.wait(duration)

dig_index = 0
dig_sequence = [image_prefix+"dig.jpg", image_prefix+"land.jpg", image_prefix+"dig.jpg"]
index = 0
first_planet = True
def show_animation(images, frame_time=0.667,test=False,gem_img=hundred_img):
    global decay,gem,galaxy,study,experiment_clock,dig_index,first_planet,prt_clock
    """Displays an animation sequence by flipping through images."""
    for img in images:
        stim = visual.ImageStim(win, image=img, size=(1.2,1.2))
        stim.draw()
        win.flip()
        core.wait(frame_time)
    stim = visual.ImageStim(win, image=gem_img, size=(1.2,1.2))
    stim.draw()
    if test == False:
        response_clock = core.Clock()
        if first_planet:
            prt_clock = core.Clock()
        stim = visual.TextStim(win, text="Dig here or travel to a new planet?", color='black', height=0.07, pos=(0, 0.7), wrapWidth=1.5)
        stim.draw()
        win.flip()
        keys = event.waitKeys(maxWait=2,keyList= ['a','l'],timeStamped = response_clock)
        if keys:
            key,RT = keys[0]
            if 'a' in key:
                if decay:
                    first_planet= False
                    dig_index +=1
                    study.append({
                        "ID": "",
                        "TrialType":f"Dig_Trial_{dig_index}",
                        "AlienOrder": "",
                        "TimeElapsed": experiment_clock.getTime(),
                        "RT": RT,
                        "PRT": "",
                        "Galaxy": "",
                        "DecayRate": "",
                        "AlienIndex": "",
                        "GemValue": gem
                    })
                    gem = round(decay*gem)
                    gem_path = image_prefix + f"gems/{gem}.jpg"
                    dig_instruction(gems=gem_path)
                else:
                    dig_instruction(gems=gem_img)
            if 'l' in key:
                    study.append({
                        "ID": "",
                        "TrialType":f"Travel_Trial",
                        "AlienOrder": "",
                        "TimeElapsed": experiment_clock.getTime(),
                        "RT": RT,
                        "PRT": prt_clock.getTime(),
                        "Galaxy": "",
                        "DecayRate": "",
                        "AlienIndex": "",
                        "GemValue": gem
                    })
                    travel_trial()
        else:
            too_slow()
            # dig_instruction(gems=gem_img)
            study.append({
                "ID": "",
                "TrialType":f"Too_slow",
                "AlienOrder": "",
                "TimeElapsed": experiment_clock.getTime(),
                "RT": "NA",
                "PRT": "",
                "Galaxy": "",
                "DecayRate": "",
                "AlienIndex": "",
                "GemValue": gem
            })
            if decay:
                gem = round(decay*gem)
                gem_path = image_prefix + f"gems/{gem}.jpg"
                dig_instruction(gems=gem_path)  
            else:
                dig_instruction(gems=gem_img)
    else:
        prt_clock = core.Clock()
        study.append({
            "ID": "",
            "TrialType":f"Dig_Instruct",
            "AlienOrder": "",
            "TimeElapsed": experiment_clock.getTime(),
            "RT": "",
            "PRT": "",
            "Galaxy": "",
            "DecayRate": "",
            "AlienIndex": "",
            "GemValue": ""
        })
        win.flip()
        core.wait(1)

def too_slow():
    show_image(timeout_img,duration=2)


def dig_instruction(practice=False,gems=hundred_img):
    show_animation(dig_sequence, frame_time=0.667,test=practice,gem_img=gems)

def travel_trial():
    """Simulates travel sequence"""
    global study
    for img in travel_sequence:
        stim = visual.ImageStim(win, image=img, size=(1.2,1.2))
        stim.draw()
        win.flip()
        core.wait(1)
    core.wait(1)
    study.append({
        "ID": "",
        "TrialType":f"Travel_Planet",
        "AlienOrder": "",
        "TimeElapsed": experiment_clock.getTime(),
        "RT": "",
        "PRT": "",
        "Galaxy": "",
        "DecayRate": "",
        "AlienIndex": "",
        "GemValue": ""
    })
    win.flip()


def decision_trial():
    """Allows participants to choose whether to dig or travel"""
    show_image(land_img, 1)
    response = get_keyboard_response(["a", "l"], timeout=2)
    if response:
        key = response[0][0]
        if key == "a":
            return "dig"
        elif key == "l":
            return "travel"
    return "timeout"

def practice_trial():
    """Practice version of the decision trial"""
    show_text("Practice Trial: Press A to dig or L to travel.")
    return decision_trial()

def run_quiz(questions,choices,correct_answers):
    """Displays a multiple-choice quiz and checks answers."""
    form_items = []
    win.units = "height"
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

    # Provide feedback based on correctness
    if correct==True:
        feedback_text = "Correct! Press SPACE to continue."
    else:
        feedback_text = "Incorrect. Try again."
        return repeat_inst()

    # Show feedback
    feedback = visual.TextStim(win, text=feedback_text, color='black', height=0.07)
    feedback.draw()
    win.flip()
    win.units = "norm"
    event.waitKeys(keyList=['space'])
    
def repeat_inst():
    show_text("Howdy! In this experiment, you’ll be an explorer traveling through space to collect space treasure. Your mission is to collect as much treasure as possible. Press the space bar to begin reading the instructions!",image_path=intro_ast,y=0.7,x=0.4)
    show_text("As a space explorer, you’ll visit different planets to dig for space treasure, these pink gems. The more space treasure you mine, the more bonus payment you’ll win! \n\n[Press the space bar to continue]",image_path=intro_gem_img)
    show_text("When you’ve arrived at a new planet, you will dig once.\n\nThen, you get to decide if you want to stay on the planet and dig again or travel to a new planet and dig there. \n\nTo stay and dig, press the letter ‘A’ on the keyboard. Try pressing it now!",image_path=land_img,height=0.6,x=1,y=1)
    dig_instruction(practice=True)
    show_text("The longer you mine a planet the fewer gems you’ll get with each dig.\n\nWhen gems are running low, you may want to travel to a new planet that hasn’t been overmined.\n\nPlanets are very far apart in this galaxy, so it will take some time to travel between them.\n\nThere are lots and lots of planets for you to visit, so you won’t be able to return to any planets you’ve already visited.\n\nTo leave this planet and travel to a new one, press the letter ‘L’ on the keyboard. Try pressing it now!",image_path=intro_travel,height=0.6,x=0.8,y=0.8,text_height=0.05)
    travel_trial()
    show_text("When you arrive at a new planet, an alien from that planet will greet you!\n\n[Press the space bar to continue]",image_path=intro_alien,height=0.6,y=1,x=1)
    show_text("If you’re not fast enough in making a choice, you’ll have to wait a few seconds before you can make another one.\n\nYou can’t dig for more gems or travel to new planets. You just have to sit and wait.\n\n[Press the space bar to continue]",image_path=timeout_img,height=0.5,x=1,y=1)
    show_text("After digging and traveling for a while, you’ll be able to take a break at home base.\n\nYou can spend at most 1 minute at home base — there are still a lot of gems left to collect!\n\nYou will spend 30 minutes mining gems and traveling to new planets no matter what.\n\nYou will visit home base every 6 minutes, so, you will visit home base four times during the game.\n\n[Press the space bar to continue]",image_path=home_base,height=0.5,x=1,y=1,text_height=0.04)
    run_quiz(questions=questions,choices=choices,correct_answers=correct_answers)

def rest_homebase():
    """When participants need to rest at homebase"""
    global study,experiment_clock
    show_text(text="You have been traveling for a while. Time to take a rest at home base!\n\nWhen you are ready to move one, press the space bar. You have up to a minute of rest.",height=0.5,image_path=home_base,x=1,y=1,duration=60,home=True)
    show_text("The task is continuing now",height=0,duration=1.5)
    study.append({
        "ID": "",
        "TrialType":f"block_end",
        "AlienOrder": "",
        "TimeElapsed": experiment_clock.getTime(),
        "RT": "",
        "PRT": "",
        "Galaxy":"",
        "DecayRate": "",
        "AlienIndex": "",
        "GemValue": ""
    })

def block_loop(blockNum):
    """Main task loop divided into blocks"""
    global gem,decay,alien_index,study,first_planet
    first_trial = True
    timer = core.Clock()
    while timer.getTime() < block_length: 
        first_planet = True
        if alien_index >= len(planets):
            alien_index = 0
        if first_trial:
            get_galaxy(first=True)
        else:
            get_galaxy()
        first_trial = False
        decay = get_decay_rate(galaxy=galaxy)
        gem = round(np.max([np.min([np.random.normal(100,5),135]),0]))
        gem_path = image_prefix + f"gems/{gem}.jpg"
        show_image(img_path=planets[alien_index],duration=5)
        dig_instruction(gems=gem_path)
        alien_index += 1
        study.append({
            "ID": "",
            "TrialType":f"start_loop",
            "AlienOrder": "",
            "TimeElapsed": experiment_clock.getTime(),
            "RT": "",
            "PRT": "",
            "Galaxy": galaxy,
            "DecayRate": decay,
            "AlienIndex": alien_index,
            "GemValue": ""
        })
    win.flip()
    core.wait(1)


def save_data(participant_id, trials):
    """Save collected data to a CSV file, automatically detecting headers."""
    filename = f"participant_{participant_id}.csv"

    if not trials:
        print("No trial data to save.")
        return  # Prevents writing an empty file

    # Extract headers dynamically from the first trial's keys
    headers = trials[0].keys()  

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()  # Write column names
        
        for trial in trials:
            writer.writerow(trial)  # Write each trial's data as a row

    print(f"Data saved to {filename}")

# Experiment flow

show_text("Howdy! In this experiment, you’ll be an explorer traveling through space to collect space treasure. Your mission is to collect as much treasure as possible. Press the space bar to begin reading the instructions!",image_path=intro_ast,y=0.7,x=0.4)
get_keyboard_response(["space"])

show_text("As a space explorer, you’ll visit different planets to dig for space treasure, these pink gems. The more space treasure you mine, the more bonus payment you’ll win! \n\n[Press the space bar to continue]",image_path=intro_gem_img)
get_keyboard_response(["space"])

show_text("When you’ve arrived at a new planet, you will dig once.\n\nThen, you get to decide if you want to stay on the planet and dig again or travel to a new planet and dig there. \n\nTo stay and dig, press the letter ‘A’ on the keyboard. Try pressing it now!",image_path=land_img,height=0.6,x=1,y=1)
get_keyboard_response(["a"])

dig_instruction(practice=True)

show_text("The longer you mine a planet the fewer gems you’ll get with each dig.\n\nWhen gems are running low, you may want to travel to a new planet that hasn’t been overmined.\n\nPlanets are very far apart in this galaxy, so it will take some time to travel between them.\n\nThere are lots and lots of planets for you to visit, so you won’t be able to return to any planets you’ve already visited.\n\nTo leave this planet and travel to a new one, press the letter ‘L’ on the keyboard. Try pressing it now!",image_path=intro_travel,height=0.6,x=0.8,y=0.8,text_height=0.05)
get_keyboard_response(["l"])

travel_trial()

show_text("When you arrive at a new planet, an alien from that planet will greet you!\n\n[Press the space bar to continue]",image_path=intro_alien,height=0.6,y=1,x=1)
get_keyboard_response(["space"])

show_text("If you’re not fast enough in making a choice, you’ll have to wait a few seconds before you can make another one.\n\nYou can’t dig for more gems or travel to new planets. You just have to sit and wait.\n\n[Press the space bar to continue]",image_path=timeout_img,height=0.5,x=1,y=1)
get_keyboard_response(["space"])

show_text("After digging and traveling for a while, you’ll be able to take a break at home base.\n\nYou can spend at most 1 minute at home base — there are still a lot of gems left to collect!\n\nYou will spend 30 minutes mining gems and traveling to new planets no matter what.\n\nYou will visit home base every 6 minutes, so, you will visit home base four times during the game.\n\n[Press the space bar to continue]",image_path=home_base,height=0.5,x=1,y=1,text_height=0.04)
get_keyboard_response(["space"])

run_quiz(questions=questions,choices=choices,correct_answers=correct_answers)

show_text("Now, you'll play a practice game, so you can practice mining space treasure and traveling to new planets.\n\nIn the practice game, you'll be digging up barrels of gems. But, in the real game, you'll be digging up the gems themselves.\n\nPress the space bar to begin practice!")
get_keyboard_response(["space"])

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
rest_homebase()

block_loop(6)
rest_homebase()




#Save data
save_data(participant_id, study)

show_text("Thank you for participating! Press SPACE to exit.")
get_keyboard_response(["space"])

win.close()
core.quit()
