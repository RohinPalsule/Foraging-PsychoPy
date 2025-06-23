from psychopy import visual, core, event, data, sound
import random

# Initialize the window
win = visual.Window(fullscr=True, color='black')

# Define stimuli images
image_prefix = "/static/images/task_images/"
land_img = image_prefix + "land.jpg"
dig_img = image_prefix + "dig.jpg"
space_treasure_img = image_prefix + "gems/100.jpg"
travel_sequence = [image_prefix+"rocket-01.jpg", image_prefix+"rocket-02.jpg", image_prefix+"rocket-03.jpg"]

def show_image(img_path, duration=1.5):
    """Displays an image for a given duration"""
    stim = visual.ImageStim(win, image=img_path)
    stim.draw()
    win.flip()
    core.wait(duration)

def get_keyboard_response(valid_keys, timeout=2):
    """Waits for a keyboard response within a given time"""
    timer = core.Clock()
    keys = event.waitKeys(maxWait=timeout, keyList=valid_keys, timeStamped=timer)
    return keys

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

# Experiment flow
for _ in range(5):  # 5 trials for now
    choice = decision_trial()
    if choice == "dig":
        reward = dig_trial()
        print(f"Collected {reward} gems!")
    elif choice == "travel":
        travel_trial()
    else:
        print("No response. Timed out.")

win.close()
core.quit()
