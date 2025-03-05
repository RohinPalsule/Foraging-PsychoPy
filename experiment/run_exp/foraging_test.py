from psychopy import visual, core, event, data, sound
import random

# Initialize the window
win = visual.Window(fullscr=True, color='white')

# Define stimuli images
image_prefix = "../run_exp/static/images/task_images/"
land_img = image_prefix + "land.jpg"
dig_img = image_prefix + "dig.jpg"
space_treasure_img = image_prefix + "gems/100.jpg"
travel_sequence = [image_prefix+"rocket-01.jpg", image_prefix+"rocket-02.jpg", image_prefix+"rocket-03.jpg"]
intro_gem_img = image_prefix + "pink_gem.jpg"
intro_ast = image_prefix + "opening_img-01.jpg"

def show_text(text, duration=0, image_path=None):
    """Displays a text message either until a key is pressed or for a specified duration (Default unlimited duration)"""
    stim = visual.TextStim(win, text=text, color='black', height=0.07, pos=(0, 0.3))
    stim.draw()

    if image_path:
        stim_image = visual.ImageStim(win, image=image_path, size=(0.5, 0.5), pos=(0, -0.3))  # Adjust size as needed
        stim_image.draw()

    win.flip()

    if duration > 0:
        core.wait(duration)
    else:
        event.waitKeys()

def get_keyboard_response(valid_keys, timeout=2):
    """Waits for a keyboard response within a given time"""
    timer = core.Clock()
    keys = event.waitKeys(maxWait=timeout, keyList=valid_keys, timeStamped=timer)
    return keys

def show_image(img_path, duration=1.5):
    """Displays an image for a given duration"""
    stim = visual.ImageStim(win, image=img_path)
    stim.draw()
    win.flip()
    core.wait(duration)

def dig_trial():
    """Simulates the digging trial"""
    show_image(dig_img, 1)
    return random.randint(1, 135)  # Simulating reward collection

def travel_trial():
    """Simulates travel sequence"""
    for img in travel_sequence:
        show_image(img, 0.5)

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

def run_quiz():
    """Basic quiz to check understanding"""
    show_text("Quiz: What key do you press to dig? A or L?")
    response = get_keyboard_response(["a", "l"], timeout=5)
    if response and response[0][0] == "a":
        show_text("Correct!")
    else:
        show_text("Incorrect. The correct answer is A.")

def save_data(participant_id, trials):
    """Save collected data to a CSV file"""
    filename = f"participant_{participant_id}.csv"
    with open(filename, "w") as f:
        f.write("trial,choice,reward\n")
        for i, (choice, reward) in enumerate(trials):
            f.write(f"{i+1},{choice},{reward}\n")

# Experiment flow

show_text("Howdy! In this experiment, you’ll be an explorer traveling through space to collect space treasure. Your mission is to collect as much treasure as possible. Press the space bar to begin reading the instructions!",image_path=intro_ast)
get_keyboard_response(["space"])

show_text("As a space explorer, you’ll visit different planets to dig for space treasure, these pink gems. The more space treasure you mine, the more bonus payment you’ll win! [Press the space bar to continue]",image_path=intro_gem_img)
get_keyboard_response(["space"])

win.close()
core.quit()

# Run practice trials
for _ in range(2):
    practice_trial()

# Run quiz
run_quiz()

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
