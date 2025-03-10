from psychopy import visual, core, event, data, sound
import random

# Initialize the window
win = visual.Window(fullscr=True, color='white',allowStencil=True,units = "norm")

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


def show_text(text, duration=0, image_path=None,x=0.5,y=0.6,height=0.3,text_height=0.07):
    """Displays a text message either until a key is pressed or for a specified duration (Default unlimited duration)"""
    stim = visual.TextStim(win, text=text, color='black', height=text_height, pos=(0, height), wrapWidth=1.5)
    stim.draw()

    if image_path:
        stim_image = visual.ImageStim(win, image=image_path, size=(x, y), pos=(0, -0.3))  # Adjust size as needed
        stim_image.draw()

    win.flip()

    if duration > 0:
        core.wait(duration)
    else:
        event.waitKeys(keyList=["space","a","l"])

def show_button_text(text,height=0.3,text_height=0.07):
    """Displays a text message either until a button is pressed or for a specified duration (Default unlimited duration)"""
    stim = visual.TextStim(win, text=text, color='black', height=text_height, pos=(0, height), wrapWidth=1.5)

    button1 = visual.Rect(win, width=0.3, height=0.1, pos=(-0.3, -0.1), fillColor='gray')
    button2 = visual.Rect(win, width=0.3, height=0.1, pos=(0.3, -0.1), fillColor='gray')

    label1 = visual.TextStim(win, text="Practice game again", pos=(-0.3, -0.1), color='black', height=0.04)
    label2 = visual.TextStim(win, text="Move on to the real game", pos=(0.3, -0.1), color='black', height=0.04)

    # Create mouse object
    mouse = event.Mouse()

    # Display everything
    while True:
        button1.draw()
        button2.draw()
        label1.draw()
        label2.draw()
        stim.draw()
        win.flip()
        # Check for clicks
        if mouse.isPressedIn(button1):
            dig_instruction()
            show_button_text("Now that you know how to dig for space treasure and travel to new planets, you can start exploring the universe!\n\nDo you want to play the practice game again or get started with the real game?")
            break
        elif mouse.isPressedIn(button2):
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

dig_sequence = [image_prefix+"dig.jpg", image_prefix+"land.jpg", image_prefix+"dig.jpg"]
index = 0
def show_animation(images, frame_time=0.667,test=False,gems=hundred_img):
    global index
    """Displays an animation sequence by flipping through images."""
    for img in images:
        stim = visual.ImageStim(win, image=img, size=(1.2,1.2))
        stim.draw()
        win.flip()
        core.wait(frame_time)
    if isinstance(gems,list):
        gem_img = gems[index]
    else: gem_img = gems
    stim = visual.ImageStim(win, image=gem_img, size=(1.2,1.2))
    stim.draw()
    if test == False:
        stim = visual.TextStim(win, text="Dig here or travel to a new planet?", color='black', height=0.07, pos=(0, 0.7), wrapWidth=1.5)
        stim.draw()
        win.flip()
        keys = event.waitKeys(maxWait=2,keyList= ['a','l'])
        if keys:
            if 'a' in keys:
                dig_instruction(gems=gem_img)
                index += 1
            if 'l' in keys:
                travel_trial()
                index =0
        else:
            too_slow()
            dig_instruction(gems=gem_img)
    else:
        win.flip()
        core.wait(1)

def too_slow():
    show_image(timeout_img,duration=2)


def dig_instruction(practice=False,gems=hundred_img):
    show_animation(dig_sequence, frame_time=0.667,test=practice,gems=gems)

def dig_trial():
    """Simulates the digging trial"""
    show_image(dig_img, 1)
    return random.randint(1, 135)  # Simulating reward collection

def travel_trial():
    """Simulates travel sequence"""
    for img in travel_sequence:
        stim = visual.ImageStim(win, image=img, size=(1.2,1.2))
        stim.draw()
        win.flip()
        core.wait(0.5)
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
        return run_quiz(questions, choices, correct_answers) 

    # Show feedback
    feedback = visual.TextStim(win, text=feedback_text, color='black', height=0.07)
    feedback.draw()
    win.flip()
    win.units = "norm"
    event.waitKeys(keyList=['space'])
    


def save_data(participant_id, trials):
    """Save collected data to a CSV file"""
    filename = f"participant_{participant_id}.csv"
    with open(filename, "w") as f:
        f.write("trial,choice,reward\n")
        for i, (choice, reward) in enumerate(trials):
            f.write(f"{i+1},{choice},{reward}\n")

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

show_text("After digging and traveling for a while, you’ll be able to take a break at home base.\n\nYou can spend at most 1 minute at home base — there are still a lot of gems left to collect!\n\nYou will spend 30 minutes mining gems and traveling to new planets no matter what.\n\nYou will visit home base every 6 minutes, so, you will visit home base four times during the game.\n\n[Press the space bar to continue]",image_path=home_base,height=0.6,x=0.8,y=0.8,text_height=0.04)
get_keyboard_response(["space"])

run_quiz(questions=questions,choices=choices,correct_answers=correct_answers)

show_text("Now, you'll play a practice game, so you can practice mining space treasure and traveling to new planets.\n\nIn the practice game, you'll be digging up barrels of gems. But, in the real game, you'll be digging up the gems themselves.\n\nPress the space bar to begin practice!")
get_keyboard_response(["space"])

show_image(img_path=practice_alien)
dig_instruction(gems=barrel_img)

show_button_text(text="Now that you know how to dig for space treasure and travel to new planets, you can start exploring the universe!\n\nDo you want to play the practice game again or get started with the real game?")

show_text("end")

win.close()
core.quit()

# Run practice trials
for _ in range(2):
    practice_trial()

# Run quiz


# Main experiment loop
trials = []
participant_id = random.randint(1000, 9999)
for _ in range(5):  # 5 trials for now
    choice = decision_trial()
    if choice == "dig":
        reward = dig_trial()
        trials.append(("dig", reward))
    elif choice == "travel":
        travel_trial()
        trials.append(("travel", 0))
    else:
        trials.append(("timeout", 0))

# Save data
# save_data(participant_id, trials)

show_text("Thank you for participating! Press SPACE to exit.")
get_keyboard_response(["space"])

win.close()
core.quit()
