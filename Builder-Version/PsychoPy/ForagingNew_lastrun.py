#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.3),
    on Mon Jun 23 12:53:51 2025
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.3'
expName = 'ForagingNew'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '000',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1728, 1117]
_loggingLevel = logging.getLevel('warning')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s' % (expInfo['participant'], expName)
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/Users/rohinpalsule/Documents/GitHub/Foraging-PsychoPy/Builder-Version/PsychoPy/ForagingNew_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1.0000, 1.0000, 1.0000]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_instruct') is None:
        # initialise key_instruct
        key_instruct = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruct',
        )
    if deviceManager.getDevice('key_instruct_2') is None:
        # initialise key_instruct_2
        key_instruct_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruct_2',
        )
    if deviceManager.getDevice('key_instruct_3') is None:
        # initialise key_instruct_3
        key_instruct_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruct_3',
        )
    if deviceManager.getDevice('key_instruct_4') is None:
        # initialise key_instruct_4
        key_instruct_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruct_4',
        )
    if deviceManager.getDevice('key_instruct_5') is None:
        # initialise key_instruct_5
        key_instruct_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruct_5',
        )
    if deviceManager.getDevice('key_instruct_6') is None:
        # initialise key_instruct_6
        key_instruct_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruct_6',
        )
    if deviceManager.getDevice('key_instruct_7') is None:
        # initialise key_instruct_7
        key_instruct_7 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruct_7',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_instruct_8') is None:
        # initialise key_instruct_8
        key_instruct_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruct_8',
        )
    if deviceManager.getDevice('digChoices') is None:
        # initialise digChoices
        digChoices = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='digChoices',
        )
    if deviceManager.getDevice('digChoices_2') is None:
        # initialise digChoices_2
        digChoices_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='digChoices_2',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_instruct_9') is None:
        # initialise key_instruct_9
        key_instruct_9 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_instruct_9',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "Instruct1" ---
    text_norm = visual.TextStim(win=win, name='text_norm',
        text='Howdy! In this experiment, you’ll be an explorer traveling through space to collect space treasure.\nYour mission is to collect as much treasure as possible.\nPress the space bar to begin reading the instructions!',
        font='Arial',
        units='norm', pos=(0, 0.3), height=0.07, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct = keyboard.Keyboard(deviceName='key_instruct')
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='../images/task_images/opening_img-01.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.3), size=(0.4, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    # Run 'Begin Experiment' code from text_align
    import csv
    from psychopy import core
    study = []  # this will hold all your trial data
    participant_id = expInfo['participant']  # this uses PsychoPy's built-in ID field
    experiment_clock = core.Clock()
    t_loop = 0
    endStudy = False
    def save_data(participant_id, trials):
        filename = f"data/participant_{participant_id}.csv"
        
        if not trials:
            print("No trial data to save.")
            return
        
        headers = trials[0].keys()
    
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for trial in trials:
                writer.writerow(trial)
        
        print(f"Data saved to {filename}")
        
    text_norm.alignHoriz= 'center'
    import numpy as np
    mainPhase = False
    numBlocks = 0
    # Generate from Beta distribution
    def rbeta(alpha, beta):
        return np.random.beta(alpha, beta)
    
    # Get decay rate based on galaxy type
    def get_decay_rate(galaxy):
        galaxy_distributions = {
            0: (13, 51),  # Rich
            1: (50, 50),  # Neutral
            2: (50, 12)   # Poor
        }
        if galaxy in galaxy_distributions:
            alpha, beta = galaxy_distributions[galaxy]
            return rbeta(alpha, beta)
        else:
            raise ValueError("Galaxy index out of range. Must be 0, 1, or 2.")
    
    # Track current galaxy
    galaxy = None
    
    # Choose the next galaxy
    def get_galaxy(first=False):
        global galaxy
        if first:
            galaxy = np.random.randint(0, 3)
        else:
            percentNum = np.random.randint(1, 11)
            if percentNum > 8:
                newGalaxy = galaxy
                while newGalaxy == galaxy:
                    newGalaxy = np.random.randint(0, 3)
                galaxy = newGalaxy
    study = []
    experiment_clock = core.Clock()
    from psychopy import core
    import numpy as np
    image_prefix = '../images/task_images/'
    alien_index = 0
    planets = []
    planet_prefix = np.random.choice(np.arange(1,121),120,replace=False) # Randomize order of aliens, but made so they do not repeat
    for planet in planet_prefix:
        planets.append(image_prefix + f"aliens/alien_planet-{planet}.jpg")
        
    study.append({
        "ID": expInfo['participant'],
        "TrialType":"InitializeStudy",
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
    
    # --- Initialize components for Routine "Instruct2" ---
    text_norm_2 = visual.TextStim(win=win, name='text_norm_2',
        text='As a space explorer, you’ll visit different planets to dig for space treasure, these pink gems.\nThe more space treasure you mine, the more bonus payment you’ll win!\n[Press the space bar to continue]',
        font='Arial',
        units='norm', pos=(0, 0.4), height=0.07, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct_2 = keyboard.Keyboard(deviceName='key_instruct_2')
    # Run 'Begin Experiment' code from text_align_2
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm_2.alignHoriz= 'center'
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', 
        image='../images/task_images/pink_gem.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.2), size=(0.29, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "Instruct3" ---
    text_norm_3 = visual.TextStim(win=win, name='text_norm_3',
        text='When you’ve arrived at a new planet, you will dig once.\nThen, you get to decide if you want to stay on the planet and dig again or travel to a new planet and dig there.\nTo stay and dig, press the letter ‘A’ on the keyboard. Try pressing it now!',
        font='Arial',
        units='norm', pos=(0, 0.7), height=0.07, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct_3 = keyboard.Keyboard(deviceName='key_instruct_3')
    # Run 'Begin Experiment' code from text_align_3
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm_3.alignHoriz= 'center'
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', 
        image='../images/task_images/land.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "digLoop" ---
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "gemReward" ---
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', 
        image='../images/task_images/gems/100.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "Instruct4" ---
    text_norm_4 = visual.TextStim(win=win, name='text_norm_4',
        text='The longer you mine a planet the fewer gems you’ll get with each dig.\nWhen gems are running low, you may want to travel to a new planet that hasn’t been overmined.\nPlanets are very far apart in this galaxy, so it will take some time to travel between them.\nThere are lots and lots of planets for you to visit, so you won’t be able to return to any planets you’ve already visited.\nTo leave this planet and travel to a new one, press the letter ‘L’ on the keyboard. Try pressing it now!',
        font='Arial',
        units='norm', pos=(0, 0.7), height=0.05, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct_4 = keyboard.Keyboard(deviceName='key_instruct_4')
    # Run 'Begin Experiment' code from text_align_4
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm.alignHoriz= 'center'
    image_6 = visual.ImageStim(
        win=win,
        name='image_6', 
        image='../images/task_images/rocket-01.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "travelLoop" ---
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "Instruct5" ---
    text_norm_5 = visual.TextStim(win=win, name='text_norm_5',
        text='When you arrive at a new planet, an alien from that planet will greet you!\n[Press the space bar to continue]',
        font='Arial',
        units='norm', pos=(0, 0.6), height=0.07, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct_5 = keyboard.Keyboard(deviceName='key_instruct_5')
    # Run 'Begin Experiment' code from text_align_5
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm_5.alignHoriz= 'center'
    image_8 = visual.ImageStim(
        win=win,
        name='image_8', 
        image='../images/task_images/aliens/alien_planet-125.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "Instruct6" ---
    text_norm_6 = visual.TextStim(win=win, name='text_norm_6',
        text='If you’re not fast enough in making a choice, you’ll have to wait a few seconds before you can make another one.\nYou can’t dig for more gems or travel to new planets. You just have to sit and wait.\n[Press the space bar to continue]',
        font='Arial',
        units='norm', pos=(0, 0.6), height=0.05, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct_6 = keyboard.Keyboard(deviceName='key_instruct_6')
    # Run 'Begin Experiment' code from text_align_6
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm_6.alignHoriz= 'center'
    image_9 = visual.ImageStim(
        win=win,
        name='image_9', 
        image='../images/task_images/time_out.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "Instruct7" ---
    text_norm_7 = visual.TextStim(win=win, name='text_norm_7',
        text='After digging and traveling for a while, you’ll be able to take a break at home base.\nYou can spend at most 1 minute at home base — there are still a lot of gems left to collect!\nYou will spend 30 minutes mining gems and traveling to new planets no matter what.\nYou will visit home base every 6 minutes, so, you will visit home base four times during the game.\n[Press the space bar to continue]',
        font='Arial',
        units='norm', pos=(0, 0.6), height=0.05, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct_7 = keyboard.Keyboard(deviceName='key_instruct_7')
    # Run 'Begin Experiment' code from text_align_7
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm_7.alignHoriz= 'center'
    image_10 = visual.ImageStim(
        win=win,
        name='image_10', 
        image='../images/task_images/home_base.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "practiceQuiz" ---
    win.allowStencil = True
    form = visual.Form(win=win, name='form',
        items='practice_quiz_form.csv',
        textHeight=0.02,
        font='Open Sans',
        randomize=False,
        style='dark',
        fillColor=None, borderColor=None, itemColor='white', 
        responseColor='white', markerColor='red', colorSpace='rgb', 
        size=(1.1, 0.9),
        pos=(0, 0),
        itemPadding=0.07,
        depth=0
    )
    # Run 'Begin Experiment' code from code
    quizTries = 0
    
    # --- Initialize components for Routine "QuizFeedback" ---
    feedbackText = visual.TextStim(win=win, name='feedbackText',
        text='',
        font='Arial',
        units='norm', pos=(0, 0), height=0.07, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "Instruct8" ---
    text_norm_8 = visual.TextStim(win=win, name='text_norm_8',
        text="Now, you'll play a practice game, so you can practice mining space treasure and traveling to new planets.\n\nIn the practice game, you'll be digging up barrels of gems. But, in the real game, you'll be digging up the gems themselves.\n\nPress the space bar to begin practice!",
        font='Arial',
        units='norm', pos=(0, 0), height=0.07, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct_8 = keyboard.Keyboard(deviceName='key_instruct_8')
    # Run 'Begin Experiment' code from text_align_8
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm_8.alignHoriz= 'center'
    
    # --- Initialize components for Routine "practiceAlien" ---
    pracAlienIMG = visual.ImageStim(
        win=win,
        name='pracAlienIMG', 
        image='../images/task_images/aliens/alien_planet-124.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "digLoop" ---
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "practiceGem" ---
    practice_gem = visual.ImageStim(
        win=win,
        name='practice_gem', 
        image='../images/task_images/barrel_text.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "digOptions" ---
    text_norm_9 = visual.TextStim(win=win, name='text_norm_9',
        text='Dig here or travel to a new planet?',
        font='Arial',
        units='norm', pos=(0, 0.7), height=0.07, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    image_11 = visual.ImageStim(
        win=win,
        name='image_11', 
        image='../images/task_images/land.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    digChoices = keyboard.Keyboard(deviceName='digChoices')
    
    # --- Initialize components for Routine "tooSlow" ---
    too_slow_img = visual.ImageStim(
        win=win,
        name='too_slow_img', 
        image='../images/task_images/time_out.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "travelLoop" ---
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "travel_init" ---
    image_15 = visual.ImageStim(
        win=win,
        name='image_15', 
        image='../images/task_images/rocket-09.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "choiceScreen" ---
    text_norm_12 = visual.TextStim(win=win, name='text_norm_12',
        text='Now that you know how to dig for space treasure and travel to new planets, you can start exploring the universe!\n\nDo you want to play the practice game again or get started with the real game?',
        font='Arial',
        units='norm', pos=(0, 0.2), height=0.07, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    buttonPractice = visual.ButtonStim(win, 
        text='Practice game again', font='Arvo',
        pos=(-0.3, -0.3),
        letterHeight=0.03,
        size=(0.3, 0.1), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='buttonPractice',
        depth=-1
    )
    buttonPractice.buttonClock = core.Clock()
    buttonReal = visual.ButtonStim(win, 
        text='Move on to the real game', font='Arvo',
        pos=(0.3, -0.3),
        letterHeight=0.03,
        size=(0.3, 0.1), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='buttonReal',
        depth=-2
    )
    buttonReal.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "Instruct9" ---
    text_norm_10 = visual.TextStim(win=win, name='text_norm_10',
        text='Task starting!',
        font='Arial',
        units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from text_align_9
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm_10.alignHoriz= 'center'
    
    
    # --- Initialize components for Routine "alienVisit" ---
    image_12 = visual.ImageStim(
        win=win,
        name='image_12', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "digLoop" ---
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "digTrial" ---
    gemIMG = visual.ImageStim(
        win=win,
        name='gemIMG', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "stay_leave" ---
    text_norm_11 = visual.TextStim(win=win, name='text_norm_11',
        text='Dig here or travel to a new planet?',
        font='Arial',
        units='norm', pos=(0, 0.7), height=0.07, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    image_13 = visual.ImageStim(
        win=win,
        name='image_13', 
        image='../images/task_images/land.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    digChoices_2 = keyboard.Keyboard(deviceName='digChoices_2')
    # Run 'Begin Experiment' code from code_8
    dig_index = 0
    
    # --- Initialize components for Routine "tooSlow" ---
    too_slow_img = visual.ImageStim(
        win=win,
        name='too_slow_img', 
        image='../images/task_images/time_out.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "travelLoop" ---
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "travel_init" ---
    image_15 = visual.ImageStim(
        win=win,
        name='image_15', 
        image='../images/task_images/rocket-09.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "homeBase" ---
    text_norm_13 = visual.TextStim(win=win, name='text_norm_13',
        text='You have been traveling for a while. Time to take a rest at home base!\nWhen you are ready to move one, press the space bar. You have up to a minute of rest.',
        font='Arial',
        units='norm', pos=(0, 0.6), height=0.07, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    image_14 = visual.ImageStim(
        win=win,
        name='image_14', 
        image='../images/task_images/home_base.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), size=(0.8, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "thank_you" ---
    text_norm_14 = visual.TextStim(win=win, name='text_norm_14',
        text='Thank you for participating! Press SPACE to exit.',
        font='Arial',
        units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_instruct_9 = keyboard.Keyboard(deviceName='key_instruct_9')
    # Run 'Begin Experiment' code from text_align_10
    # Code components should usually appear at the top
    # of the routine. This one has to appear after the
    # text component it refers to.
    text_norm_14.alignHoriz= 'center'
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # set up handler to look after randomisation of conditions etc
    ifQuizWrong = data.TrialHandler(nReps=50.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='ifQuizWrong')
    thisExp.addLoop(ifQuizWrong)  # add the loop to the experiment
    thisIfQuizWrong = ifQuizWrong.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisIfQuizWrong.rgb)
    if thisIfQuizWrong != None:
        for paramName in thisIfQuizWrong:
            globals()[paramName] = thisIfQuizWrong[paramName]
    
    for thisIfQuizWrong in ifQuizWrong:
        currentLoop = ifQuizWrong
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisIfQuizWrong.rgb)
        if thisIfQuizWrong != None:
            for paramName in thisIfQuizWrong:
                globals()[paramName] = thisIfQuizWrong[paramName]
        
        # --- Prepare to start Routine "Instruct1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Instruct1.started', globalClock.getTime(format='float'))
        key_instruct.keys = []
        key_instruct.rt = []
        _key_instruct_allKeys = []
        # keep track of which components have finished
        Instruct1Components = [text_norm, key_instruct, image]
        for thisComponent in Instruct1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Instruct1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_norm* updates
            
            # if text_norm is starting this frame...
            if text_norm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_norm.frameNStart = frameN  # exact frame index
                text_norm.tStart = t  # local t and not account for scr refresh
                text_norm.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_norm, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_norm.status = STARTED
                text_norm.setAutoDraw(True)
            
            # if text_norm is active this frame...
            if text_norm.status == STARTED:
                # update params
                pass
            
            # *key_instruct* updates
            waitOnFlip = False
            
            # if key_instruct is starting this frame...
            if key_instruct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_instruct.frameNStart = frameN  # exact frame index
                key_instruct.tStart = t  # local t and not account for scr refresh
                key_instruct.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_instruct, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_instruct.started')
                # update status
                key_instruct.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_instruct.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_instruct.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_instruct.status == STARTED and not waitOnFlip:
                theseKeys = key_instruct.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_instruct_allKeys.extend(theseKeys)
                if len(_key_instruct_allKeys):
                    key_instruct.keys = _key_instruct_allKeys[0].name  # just the first key pressed
                    key_instruct.rt = _key_instruct_allKeys[0].rt
                    key_instruct.duration = _key_instruct_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instruct1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instruct1" ---
        for thisComponent in Instruct1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Instruct1.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_instruct.keys in ['', [], None]:  # No response was made
            key_instruct.keys = None
        ifQuizWrong.addData('key_instruct.keys',key_instruct.keys)
        if key_instruct.keys != None:  # we had a response
            ifQuizWrong.addData('key_instruct.rt', key_instruct.rt)
            ifQuizWrong.addData('key_instruct.duration', key_instruct.duration)
        # Run 'End Routine' code from text_align
        thisExp.addData('trial_type','instruct_1')
        thisExp.nextEntry()
        
        study.append({
            "ID": "",
            "TrialType":"Instruction_1",
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
        # the Routine "Instruct1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Instruct2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Instruct2.started', globalClock.getTime(format='float'))
        key_instruct_2.keys = []
        key_instruct_2.rt = []
        _key_instruct_2_allKeys = []
        # keep track of which components have finished
        Instruct2Components = [text_norm_2, key_instruct_2, image_2]
        for thisComponent in Instruct2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Instruct2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_norm_2* updates
            
            # if text_norm_2 is starting this frame...
            if text_norm_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_norm_2.frameNStart = frameN  # exact frame index
                text_norm_2.tStart = t  # local t and not account for scr refresh
                text_norm_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_norm_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_norm_2.status = STARTED
                text_norm_2.setAutoDraw(True)
            
            # if text_norm_2 is active this frame...
            if text_norm_2.status == STARTED:
                # update params
                pass
            
            # *key_instruct_2* updates
            waitOnFlip = False
            
            # if key_instruct_2 is starting this frame...
            if key_instruct_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_instruct_2.frameNStart = frameN  # exact frame index
                key_instruct_2.tStart = t  # local t and not account for scr refresh
                key_instruct_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_instruct_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_instruct_2.started')
                # update status
                key_instruct_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_instruct_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_instruct_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_instruct_2.status == STARTED and not waitOnFlip:
                theseKeys = key_instruct_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_instruct_2_allKeys.extend(theseKeys)
                if len(_key_instruct_2_allKeys):
                    key_instruct_2.keys = _key_instruct_2_allKeys[0].name  # just the first key pressed
                    key_instruct_2.rt = _key_instruct_2_allKeys[0].rt
                    key_instruct_2.duration = _key_instruct_2_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *image_2* updates
            
            # if image_2 is starting this frame...
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.started')
                # update status
                image_2.status = STARTED
                image_2.setAutoDraw(True)
            
            # if image_2 is active this frame...
            if image_2.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instruct2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instruct2" ---
        for thisComponent in Instruct2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Instruct2.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_instruct_2.keys in ['', [], None]:  # No response was made
            key_instruct_2.keys = None
        ifQuizWrong.addData('key_instruct_2.keys',key_instruct_2.keys)
        if key_instruct_2.keys != None:  # we had a response
            ifQuizWrong.addData('key_instruct_2.rt', key_instruct_2.rt)
            ifQuizWrong.addData('key_instruct_2.duration', key_instruct_2.duration)
        # Run 'End Routine' code from text_align_2
        thisExp.addData('trial_type','instruct_2')
        thisExp.nextEntry()
        
        
        study.append({
            "ID": "",
            "TrialType":"Instruction_2",
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
        # the Routine "Instruct2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Instruct3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Instruct3.started', globalClock.getTime(format='float'))
        key_instruct_3.keys = []
        key_instruct_3.rt = []
        _key_instruct_3_allKeys = []
        # keep track of which components have finished
        Instruct3Components = [text_norm_3, key_instruct_3, image_3]
        for thisComponent in Instruct3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Instruct3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_norm_3* updates
            
            # if text_norm_3 is starting this frame...
            if text_norm_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_norm_3.frameNStart = frameN  # exact frame index
                text_norm_3.tStart = t  # local t and not account for scr refresh
                text_norm_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_norm_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_norm_3.status = STARTED
                text_norm_3.setAutoDraw(True)
            
            # if text_norm_3 is active this frame...
            if text_norm_3.status == STARTED:
                # update params
                pass
            
            # *key_instruct_3* updates
            waitOnFlip = False
            
            # if key_instruct_3 is starting this frame...
            if key_instruct_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_instruct_3.frameNStart = frameN  # exact frame index
                key_instruct_3.tStart = t  # local t and not account for scr refresh
                key_instruct_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_instruct_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_instruct_3.started')
                # update status
                key_instruct_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_instruct_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_instruct_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_instruct_3.status == STARTED and not waitOnFlip:
                theseKeys = key_instruct_3.getKeys(keyList=['a'], ignoreKeys=["escape"], waitRelease=False)
                _key_instruct_3_allKeys.extend(theseKeys)
                if len(_key_instruct_3_allKeys):
                    key_instruct_3.keys = _key_instruct_3_allKeys[0].name  # just the first key pressed
                    key_instruct_3.rt = _key_instruct_3_allKeys[0].rt
                    key_instruct_3.duration = _key_instruct_3_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *image_3* updates
            
            # if image_3 is starting this frame...
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3.started')
                # update status
                image_3.status = STARTED
                image_3.setAutoDraw(True)
            
            # if image_3 is active this frame...
            if image_3.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instruct3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instruct3" ---
        for thisComponent in Instruct3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Instruct3.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_instruct_3.keys in ['', [], None]:  # No response was made
            key_instruct_3.keys = None
        ifQuizWrong.addData('key_instruct_3.keys',key_instruct_3.keys)
        if key_instruct_3.keys != None:  # we had a response
            ifQuizWrong.addData('key_instruct_3.rt', key_instruct_3.rt)
            ifQuizWrong.addData('key_instruct_3.duration', key_instruct_3.duration)
        # Run 'End Routine' code from text_align_3
        thisExp.addData('trial_type','instruct_3')
        thisExp.nextEntry()
        
        study.append({
            "ID": "",
            "TrialType":"Instruction_3",
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
        # the Routine "Instruct3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('psychopy-vars.xlsx', selection='0:3'),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        for thisTrial in trials:
            currentLoop = trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            # --- Prepare to start Routine "digLoop" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('digLoop.started', globalClock.getTime(format='float'))
            image_4.setImage(dig_image)
            # keep track of which components have finished
            digLoopComponents = [image_4]
            for thisComponent in digLoopComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "digLoop" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.666667:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_4* updates
                
                # if image_4 is starting this frame...
                if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_4.frameNStart = frameN  # exact frame index
                    image_4.tStart = t  # local t and not account for scr refresh
                    image_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_4.started')
                    # update status
                    image_4.status = STARTED
                    image_4.setAutoDraw(True)
                
                # if image_4 is active this frame...
                if image_4.status == STARTED:
                    # update params
                    pass
                
                # if image_4 is stopping this frame...
                if image_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_4.tStartRefresh + 0.666667-frameTolerance:
                        # keep track of stop time/frame for later
                        image_4.tStop = t  # not accounting for scr refresh
                        image_4.tStopRefresh = tThisFlipGlobal  # on global time
                        image_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_4.stopped')
                        # update status
                        image_4.status = FINISHED
                        image_4.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in digLoopComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "digLoop" ---
            for thisComponent in digLoopComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('digLoop.stopped', globalClock.getTime(format='float'))
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.666667)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trials'
        
        # get names of stimulus parameters
        if trials.trialList in ([], [None], None):
            params = []
        else:
            params = trials.trialList[0].keys()
        # save data for this loop
        trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "gemReward" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('gemReward.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        gemRewardComponents = [image_5]
        for thisComponent in gemRewardComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "gemReward" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_5* updates
            
            # if image_5 is starting this frame...
            if image_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                image_5.frameNStart = frameN  # exact frame index
                image_5.tStart = t  # local t and not account for scr refresh
                image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_5.started')
                # update status
                image_5.status = STARTED
                image_5.setAutoDraw(True)
            
            # if image_5 is active this frame...
            if image_5.status == STARTED:
                # update params
                pass
            
            # if image_5 is stopping this frame...
            if image_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_5.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    image_5.tStop = t  # not accounting for scr refresh
                    image_5.tStopRefresh = tThisFlipGlobal  # on global time
                    image_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_5.stopped')
                    # update status
                    image_5.status = FINISHED
                    image_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in gemRewardComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "gemReward" ---
        for thisComponent in gemRewardComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('gemReward.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "Instruct4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Instruct4.started', globalClock.getTime(format='float'))
        key_instruct_4.keys = []
        key_instruct_4.rt = []
        _key_instruct_4_allKeys = []
        # keep track of which components have finished
        Instruct4Components = [text_norm_4, key_instruct_4, image_6]
        for thisComponent in Instruct4Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Instruct4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_norm_4* updates
            
            # if text_norm_4 is starting this frame...
            if text_norm_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_norm_4.frameNStart = frameN  # exact frame index
                text_norm_4.tStart = t  # local t and not account for scr refresh
                text_norm_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_norm_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_norm_4.status = STARTED
                text_norm_4.setAutoDraw(True)
            
            # if text_norm_4 is active this frame...
            if text_norm_4.status == STARTED:
                # update params
                pass
            
            # *key_instruct_4* updates
            waitOnFlip = False
            
            # if key_instruct_4 is starting this frame...
            if key_instruct_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_instruct_4.frameNStart = frameN  # exact frame index
                key_instruct_4.tStart = t  # local t and not account for scr refresh
                key_instruct_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_instruct_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_instruct_4.started')
                # update status
                key_instruct_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_instruct_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_instruct_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_instruct_4.status == STARTED and not waitOnFlip:
                theseKeys = key_instruct_4.getKeys(keyList=['l'], ignoreKeys=["escape"], waitRelease=False)
                _key_instruct_4_allKeys.extend(theseKeys)
                if len(_key_instruct_4_allKeys):
                    key_instruct_4.keys = _key_instruct_4_allKeys[0].name  # just the first key pressed
                    key_instruct_4.rt = _key_instruct_4_allKeys[0].rt
                    key_instruct_4.duration = _key_instruct_4_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *image_6* updates
            
            # if image_6 is starting this frame...
            if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_6.frameNStart = frameN  # exact frame index
                image_6.tStart = t  # local t and not account for scr refresh
                image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_6.started')
                # update status
                image_6.status = STARTED
                image_6.setAutoDraw(True)
            
            # if image_6 is active this frame...
            if image_6.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instruct4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instruct4" ---
        for thisComponent in Instruct4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Instruct4.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_instruct_4.keys in ['', [], None]:  # No response was made
            key_instruct_4.keys = None
        ifQuizWrong.addData('key_instruct_4.keys',key_instruct_4.keys)
        if key_instruct_4.keys != None:  # we had a response
            ifQuizWrong.addData('key_instruct_4.rt', key_instruct_4.rt)
            ifQuizWrong.addData('key_instruct_4.duration', key_instruct_4.duration)
        # Run 'End Routine' code from text_align_4
        thisExp.addData('trial_type','instruct_4')
        thisExp.nextEntry()
        
        study.append({
            "ID": "",
            "TrialType":"Instruction_4",
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
        # the Routine "Instruct4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('psychopy-vars.xlsx'),
            seed=None, name='trials_2')
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    globals()[paramName] = thisTrial_2[paramName]
            
            # --- Prepare to start Routine "travelLoop" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('travelLoop.started', globalClock.getTime(format='float'))
            image_7.setImage(rocket_image)
            # Run 'Begin Routine' code from code_9
            t_loop +=1
            # keep track of which components have finished
            travelLoopComponents = [image_7]
            for thisComponent in travelLoopComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "travelLoop" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_7* updates
                
                # if image_7 is starting this frame...
                if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_7.frameNStart = frameN  # exact frame index
                    image_7.tStart = t  # local t and not account for scr refresh
                    image_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_7.started')
                    # update status
                    image_7.status = STARTED
                    image_7.setAutoDraw(True)
                
                # if image_7 is active this frame...
                if image_7.status == STARTED:
                    # update params
                    pass
                
                # if image_7 is stopping this frame...
                if image_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_7.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        image_7.tStop = t  # not accounting for scr refresh
                        image_7.tStopRefresh = tThisFlipGlobal  # on global time
                        image_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_7.stopped')
                        # update status
                        image_7.status = FINISHED
                        image_7.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in travelLoopComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "travelLoop" ---
            for thisComponent in travelLoopComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('travelLoop.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_9
            if mainPhase:
                
                if block_timer.getTime() >= block_duration:
                    timeLoop.finished = True
                    if numBlocks == 5:
                        endStudy = True
            if t_loop == 1:
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
                thisExp.addData('trial_type','travel_trial')
                thisExp.nextEntry()
            
            
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'trials_2'
        
        # get names of stimulus parameters
        if trials_2.trialList in ([], [None], None):
            params = []
        else:
            params = trials_2.trialList[0].keys()
        # save data for this loop
        trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "Instruct5" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Instruct5.started', globalClock.getTime(format='float'))
        key_instruct_5.keys = []
        key_instruct_5.rt = []
        _key_instruct_5_allKeys = []
        # keep track of which components have finished
        Instruct5Components = [text_norm_5, key_instruct_5, image_8]
        for thisComponent in Instruct5Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Instruct5" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_norm_5* updates
            
            # if text_norm_5 is starting this frame...
            if text_norm_5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                text_norm_5.frameNStart = frameN  # exact frame index
                text_norm_5.tStart = t  # local t and not account for scr refresh
                text_norm_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_norm_5, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_norm_5.status = STARTED
                text_norm_5.setAutoDraw(True)
            
            # if text_norm_5 is active this frame...
            if text_norm_5.status == STARTED:
                # update params
                pass
            
            # *key_instruct_5* updates
            waitOnFlip = False
            
            # if key_instruct_5 is starting this frame...
            if key_instruct_5.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                key_instruct_5.frameNStart = frameN  # exact frame index
                key_instruct_5.tStart = t  # local t and not account for scr refresh
                key_instruct_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_instruct_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_instruct_5.started')
                # update status
                key_instruct_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_instruct_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_instruct_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_instruct_5.status == STARTED and not waitOnFlip:
                theseKeys = key_instruct_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_instruct_5_allKeys.extend(theseKeys)
                if len(_key_instruct_5_allKeys):
                    key_instruct_5.keys = _key_instruct_5_allKeys[0].name  # just the first key pressed
                    key_instruct_5.rt = _key_instruct_5_allKeys[0].rt
                    key_instruct_5.duration = _key_instruct_5_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *image_8* updates
            
            # if image_8 is starting this frame...
            if image_8.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                image_8.frameNStart = frameN  # exact frame index
                image_8.tStart = t  # local t and not account for scr refresh
                image_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_8.started')
                # update status
                image_8.status = STARTED
                image_8.setAutoDraw(True)
            
            # if image_8 is active this frame...
            if image_8.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instruct5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instruct5" ---
        for thisComponent in Instruct5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Instruct5.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_instruct_5.keys in ['', [], None]:  # No response was made
            key_instruct_5.keys = None
        ifQuizWrong.addData('key_instruct_5.keys',key_instruct_5.keys)
        if key_instruct_5.keys != None:  # we had a response
            ifQuizWrong.addData('key_instruct_5.rt', key_instruct_5.rt)
            ifQuizWrong.addData('key_instruct_5.duration', key_instruct_5.duration)
        # Run 'End Routine' code from text_align_5
        thisExp.addData('trial_type','instruct_5')
        thisExp.nextEntry()
        
        study.append({
            "ID": "",
            "TrialType":"Instruction_5",
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
        # the Routine "Instruct5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Instruct6" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Instruct6.started', globalClock.getTime(format='float'))
        key_instruct_6.keys = []
        key_instruct_6.rt = []
        _key_instruct_6_allKeys = []
        # keep track of which components have finished
        Instruct6Components = [text_norm_6, key_instruct_6, image_9]
        for thisComponent in Instruct6Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Instruct6" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_norm_6* updates
            
            # if text_norm_6 is starting this frame...
            if text_norm_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_norm_6.frameNStart = frameN  # exact frame index
                text_norm_6.tStart = t  # local t and not account for scr refresh
                text_norm_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_norm_6, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_norm_6.status = STARTED
                text_norm_6.setAutoDraw(True)
            
            # if text_norm_6 is active this frame...
            if text_norm_6.status == STARTED:
                # update params
                pass
            
            # *key_instruct_6* updates
            waitOnFlip = False
            
            # if key_instruct_6 is starting this frame...
            if key_instruct_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_instruct_6.frameNStart = frameN  # exact frame index
                key_instruct_6.tStart = t  # local t and not account for scr refresh
                key_instruct_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_instruct_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_instruct_6.started')
                # update status
                key_instruct_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_instruct_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_instruct_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_instruct_6.status == STARTED and not waitOnFlip:
                theseKeys = key_instruct_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_instruct_6_allKeys.extend(theseKeys)
                if len(_key_instruct_6_allKeys):
                    key_instruct_6.keys = _key_instruct_6_allKeys[0].name  # just the first key pressed
                    key_instruct_6.rt = _key_instruct_6_allKeys[0].rt
                    key_instruct_6.duration = _key_instruct_6_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *image_9* updates
            
            # if image_9 is starting this frame...
            if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_9.frameNStart = frameN  # exact frame index
                image_9.tStart = t  # local t and not account for scr refresh
                image_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_9.started')
                # update status
                image_9.status = STARTED
                image_9.setAutoDraw(True)
            
            # if image_9 is active this frame...
            if image_9.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instruct6Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instruct6" ---
        for thisComponent in Instruct6Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Instruct6.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_instruct_6.keys in ['', [], None]:  # No response was made
            key_instruct_6.keys = None
        ifQuizWrong.addData('key_instruct_6.keys',key_instruct_6.keys)
        if key_instruct_6.keys != None:  # we had a response
            ifQuizWrong.addData('key_instruct_6.rt', key_instruct_6.rt)
            ifQuizWrong.addData('key_instruct_6.duration', key_instruct_6.duration)
        # Run 'End Routine' code from text_align_6
        thisExp.addData('trial_type','instruct_6')
        thisExp.nextEntry()
        
        study.append({
            "ID": "",
            "TrialType":"Instruction_6",
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
        # the Routine "Instruct6" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Instruct7" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Instruct7.started', globalClock.getTime(format='float'))
        key_instruct_7.keys = []
        key_instruct_7.rt = []
        _key_instruct_7_allKeys = []
        # keep track of which components have finished
        Instruct7Components = [text_norm_7, key_instruct_7, image_10]
        for thisComponent in Instruct7Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Instruct7" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_norm_7* updates
            
            # if text_norm_7 is starting this frame...
            if text_norm_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_norm_7.frameNStart = frameN  # exact frame index
                text_norm_7.tStart = t  # local t and not account for scr refresh
                text_norm_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_norm_7, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_norm_7.status = STARTED
                text_norm_7.setAutoDraw(True)
            
            # if text_norm_7 is active this frame...
            if text_norm_7.status == STARTED:
                # update params
                pass
            
            # *key_instruct_7* updates
            waitOnFlip = False
            
            # if key_instruct_7 is starting this frame...
            if key_instruct_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_instruct_7.frameNStart = frameN  # exact frame index
                key_instruct_7.tStart = t  # local t and not account for scr refresh
                key_instruct_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_instruct_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_instruct_7.started')
                # update status
                key_instruct_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_instruct_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_instruct_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_instruct_7.status == STARTED and not waitOnFlip:
                theseKeys = key_instruct_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_instruct_7_allKeys.extend(theseKeys)
                if len(_key_instruct_7_allKeys):
                    key_instruct_7.keys = _key_instruct_7_allKeys[0].name  # just the first key pressed
                    key_instruct_7.rt = _key_instruct_7_allKeys[0].rt
                    key_instruct_7.duration = _key_instruct_7_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *image_10* updates
            
            # if image_10 is starting this frame...
            if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_10.frameNStart = frameN  # exact frame index
                image_10.tStart = t  # local t and not account for scr refresh
                image_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_10.started')
                # update status
                image_10.status = STARTED
                image_10.setAutoDraw(True)
            
            # if image_10 is active this frame...
            if image_10.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instruct7Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instruct7" ---
        for thisComponent in Instruct7Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Instruct7.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_instruct_7.keys in ['', [], None]:  # No response was made
            key_instruct_7.keys = None
        ifQuizWrong.addData('key_instruct_7.keys',key_instruct_7.keys)
        if key_instruct_7.keys != None:  # we had a response
            ifQuizWrong.addData('key_instruct_7.rt', key_instruct_7.rt)
            ifQuizWrong.addData('key_instruct_7.duration', key_instruct_7.duration)
        # Run 'End Routine' code from text_align_7
        thisExp.addData('trial_type','instruct_7')
        thisExp.nextEntry()
        
        study.append({
            "ID": "",
            "TrialType":"Instruction_7",
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
        # the Routine "Instruct7" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "practiceQuiz" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('practiceQuiz.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code
        # Reset all responses in the Form manually
        for item in form.items:
            item['response'] = None
        form._currentIndex = 0  # Reset scroll position
        
        print("Form responses at start:", [item['response'] for item in form.items])
        # keep track of which components have finished
        practiceQuizComponents = [form]
        for thisComponent in practiceQuizComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practiceQuiz" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *form* updates
            
            # if form is starting this frame...
            if form.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                form.frameNStart = frameN  # exact frame index
                form.tStart = t  # local t and not account for scr refresh
                form.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(form, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'form.started')
                # update status
                form.status = STARTED
                form.setAutoDraw(True)
            
            # if form is active this frame...
            if form.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code
            
            answers = form.getData()
            responses = [ans['response'] for ans in answers if ans['response'] not in [None, ""]]
            correct_answers = ["The number of gems you collect", "Is fixed", "False"]
            QuizCorrect = True
            for i in range(len(responses)):
                if responses[i] != correct_answers[i]:
                    QuizCorrect = False
                    break
            if quizTries == 0:
                if len(responses) == 3 and all(response is not None for response in responses):
                    continueRoutine = False
            else:
                if responses == correct_answers:
                    break
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceQuizComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practiceQuiz" ---
        for thisComponent in practiceQuizComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('practiceQuiz.stopped', globalClock.getTime(format='float'))
        form.addDataToExp(thisExp, 'rows')
        form.autodraw = False
        # Run 'End Routine' code from code
        quizTries +=1
        thisExp.addData('trial_type','quiz')
        thisExp.addData('QuizResp',responses)
        thisExp.addData('QuizFailedNum',quizTries-1)
        thisExp.nextEntry()
        
        study.append({
                "ID": "",
                "TrialType":f"practice_quiz",
                "BlockNum": "",
                "AlienOrder": "",
                "QuizResp": responses,
                "QuizFailedNum": quizTries - 1,
                "TimeElapsed": experiment_clock.getTime(),
                "RT": "",
                "PRT": "",
                "Galaxy":"",
                "DecayRate": "",
                "AlienIndex": "",
                "GemValue": "",
                "TimeInBlock": ""
            })
        # the Routine "practiceQuiz" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "QuizFeedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('QuizFeedback.started', globalClock.getTime(format='float'))
        feedbackText.setText("Correct! Press SPACE to continue." if QuizCorrect else "Incorrect. Press SPACE to reread the instructions and try again.")
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        QuizFeedbackComponents = [feedbackText, key_resp]
        for thisComponent in QuizFeedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "QuizFeedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbackText* updates
            
            # if feedbackText is starting this frame...
            if feedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackText.frameNStart = frameN  # exact frame index
                feedbackText.tStart = t  # local t and not account for scr refresh
                feedbackText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedbackText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbackText.started')
                # update status
                feedbackText.status = STARTED
                feedbackText.setAutoDraw(True)
            
            # if feedbackText is active this frame...
            if feedbackText.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in QuizFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "QuizFeedback" ---
        for thisComponent in QuizFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('QuizFeedback.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        ifQuizWrong.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            ifQuizWrong.addData('key_resp.rt', key_resp.rt)
            ifQuizWrong.addData('key_resp.duration', key_resp.duration)
        # Run 'End Routine' code from code_2
        if QuizCorrect:
            ifQuizWrong.finished = True
        # the Routine "QuizFeedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 50.0 repeats of 'ifQuizWrong'
    
    # get names of stimulus parameters
    if ifQuizWrong.trialList in ([], [None], None):
        params = []
    else:
        params = ifQuizWrong.trialList[0].keys()
    # save data for this loop
    ifQuizWrong.saveAsExcel(filename + '.xlsx', sheetName='ifQuizWrong',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "Instruct8" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruct8.started', globalClock.getTime(format='float'))
    key_instruct_8.keys = []
    key_instruct_8.rt = []
    _key_instruct_8_allKeys = []
    # keep track of which components have finished
    Instruct8Components = [text_norm_8, key_instruct_8]
    for thisComponent in Instruct8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruct8" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_8* updates
        
        # if text_norm_8 is starting this frame...
        if text_norm_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_8.frameNStart = frameN  # exact frame index
            text_norm_8.tStart = t  # local t and not account for scr refresh
            text_norm_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_8, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm_8.status = STARTED
            text_norm_8.setAutoDraw(True)
        
        # if text_norm_8 is active this frame...
        if text_norm_8.status == STARTED:
            # update params
            pass
        
        # *key_instruct_8* updates
        waitOnFlip = False
        
        # if key_instruct_8 is starting this frame...
        if key_instruct_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instruct_8.frameNStart = frameN  # exact frame index
            key_instruct_8.tStart = t  # local t and not account for scr refresh
            key_instruct_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instruct_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_instruct_8.started')
            # update status
            key_instruct_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instruct_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instruct_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instruct_8.status == STARTED and not waitOnFlip:
            theseKeys = key_instruct_8.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instruct_8_allKeys.extend(theseKeys)
            if len(_key_instruct_8_allKeys):
                key_instruct_8.keys = _key_instruct_8_allKeys[0].name  # just the first key pressed
                key_instruct_8.rt = _key_instruct_8_allKeys[0].rt
                key_instruct_8.duration = _key_instruct_8_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruct8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruct8" ---
    for thisComponent in Instruct8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruct8.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_instruct_8.keys in ['', [], None]:  # No response was made
        key_instruct_8.keys = None
    thisExp.addData('key_instruct_8.keys',key_instruct_8.keys)
    if key_instruct_8.keys != None:  # we had a response
        thisExp.addData('key_instruct_8.rt', key_instruct_8.rt)
        thisExp.addData('key_instruct_8.duration', key_instruct_8.duration)
    # Run 'End Routine' code from text_align_8
    thisExp.addData('trial_type','instruct_8')
    thisExp.nextEntry()
    
    study.append({
        "ID": "",
        "TrialType":f"Instruction_8",
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
    thisExp.nextEntry()
    # the Routine "Instruct8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceLoop = data.TrialHandler(nReps=10.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practiceLoop')
    thisExp.addLoop(practiceLoop)  # add the loop to the experiment
    thisPracticeLoop = practiceLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            globals()[paramName] = thisPracticeLoop[paramName]
    
    for thisPracticeLoop in practiceLoop:
        currentLoop = practiceLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
        if thisPracticeLoop != None:
            for paramName in thisPracticeLoop:
                globals()[paramName] = thisPracticeLoop[paramName]
        
        # --- Prepare to start Routine "practiceAlien" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('practiceAlien.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        practiceAlienComponents = [pracAlienIMG]
        for thisComponent in practiceAlienComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practiceAlien" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pracAlienIMG* updates
            
            # if pracAlienIMG is starting this frame...
            if pracAlienIMG.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pracAlienIMG.frameNStart = frameN  # exact frame index
                pracAlienIMG.tStart = t  # local t and not account for scr refresh
                pracAlienIMG.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pracAlienIMG, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'pracAlienIMG.started')
                # update status
                pracAlienIMG.status = STARTED
                pracAlienIMG.setAutoDraw(True)
            
            # if pracAlienIMG is active this frame...
            if pracAlienIMG.status == STARTED:
                # update params
                pass
            
            # if pracAlienIMG is stopping this frame...
            if pracAlienIMG.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > pracAlienIMG.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    pracAlienIMG.tStop = t  # not accounting for scr refresh
                    pracAlienIMG.tStopRefresh = tThisFlipGlobal  # on global time
                    pracAlienIMG.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'pracAlienIMG.stopped')
                    # update status
                    pracAlienIMG.status = FINISHED
                    pracAlienIMG.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practiceAlienComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practiceAlien" ---
        for thisComponent in practiceAlienComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('practiceAlien.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        
        # set up handler to look after randomisation of conditions etc
        practiceDigLoop = data.TrialHandler(nReps=10.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='practiceDigLoop')
        thisExp.addLoop(practiceDigLoop)  # add the loop to the experiment
        thisPracticeDigLoop = practiceDigLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeDigLoop.rgb)
        if thisPracticeDigLoop != None:
            for paramName in thisPracticeDigLoop:
                globals()[paramName] = thisPracticeDigLoop[paramName]
        
        for thisPracticeDigLoop in practiceDigLoop:
            currentLoop = practiceDigLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisPracticeDigLoop.rgb)
            if thisPracticeDigLoop != None:
                for paramName in thisPracticeDigLoop:
                    globals()[paramName] = thisPracticeDigLoop[paramName]
            
            # set up handler to look after randomisation of conditions etc
            practiceDig = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('psychopy-vars.xlsx', selection='0:3'),
                seed=None, name='practiceDig')
            thisExp.addLoop(practiceDig)  # add the loop to the experiment
            thisPracticeDig = practiceDig.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisPracticeDig.rgb)
            if thisPracticeDig != None:
                for paramName in thisPracticeDig:
                    globals()[paramName] = thisPracticeDig[paramName]
            
            for thisPracticeDig in practiceDig:
                currentLoop = practiceDig
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisPracticeDig.rgb)
                if thisPracticeDig != None:
                    for paramName in thisPracticeDig:
                        globals()[paramName] = thisPracticeDig[paramName]
                
                # --- Prepare to start Routine "digLoop" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('digLoop.started', globalClock.getTime(format='float'))
                image_4.setImage(dig_image)
                # keep track of which components have finished
                digLoopComponents = [image_4]
                for thisComponent in digLoopComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "digLoop" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 0.666667:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *image_4* updates
                    
                    # if image_4 is starting this frame...
                    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_4.frameNStart = frameN  # exact frame index
                        image_4.tStart = t  # local t and not account for scr refresh
                        image_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_4.started')
                        # update status
                        image_4.status = STARTED
                        image_4.setAutoDraw(True)
                    
                    # if image_4 is active this frame...
                    if image_4.status == STARTED:
                        # update params
                        pass
                    
                    # if image_4 is stopping this frame...
                    if image_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > image_4.tStartRefresh + 0.666667-frameTolerance:
                            # keep track of stop time/frame for later
                            image_4.tStop = t  # not accounting for scr refresh
                            image_4.tStopRefresh = tThisFlipGlobal  # on global time
                            image_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'image_4.stopped')
                            # update status
                            image_4.status = FINISHED
                            image_4.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in digLoopComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "digLoop" ---
                for thisComponent in digLoopComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('digLoop.stopped', globalClock.getTime(format='float'))
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.666667)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1.0 repeats of 'practiceDig'
            
            # get names of stimulus parameters
            if practiceDig.trialList in ([], [None], None):
                params = []
            else:
                params = practiceDig.trialList[0].keys()
            # save data for this loop
            practiceDig.saveAsExcel(filename + '.xlsx', sheetName='practiceDig',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # --- Prepare to start Routine "practiceGem" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('practiceGem.started', globalClock.getTime(format='float'))
            # keep track of which components have finished
            practiceGemComponents = [practice_gem]
            for thisComponent in practiceGemComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "practiceGem" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *practice_gem* updates
                
                # if practice_gem is starting this frame...
                if practice_gem.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    practice_gem.frameNStart = frameN  # exact frame index
                    practice_gem.tStart = t  # local t and not account for scr refresh
                    practice_gem.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(practice_gem, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'practice_gem.started')
                    # update status
                    practice_gem.status = STARTED
                    practice_gem.setAutoDraw(True)
                
                # if practice_gem is active this frame...
                if practice_gem.status == STARTED:
                    # update params
                    pass
                
                # if practice_gem is stopping this frame...
                if practice_gem.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > practice_gem.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        practice_gem.tStop = t  # not accounting for scr refresh
                        practice_gem.tStopRefresh = tThisFlipGlobal  # on global time
                        practice_gem.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'practice_gem.stopped')
                        # update status
                        practice_gem.status = FINISHED
                        practice_gem.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in practiceGemComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "practiceGem" ---
            for thisComponent in practiceGemComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('practiceGem.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_10
            thisExp.addData('trial_type','practice_gem')
            thisExp.nextEntry()
            gem = 'practiceGem'
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "digOptions" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('digOptions.started', globalClock.getTime(format='float'))
            digChoices.keys = []
            digChoices.rt = []
            _digChoices_allKeys = []
            # Run 'Begin Routine' code from code_4
            practiceRTclock = core.Clock()
            # keep track of which components have finished
            digOptionsComponents = [text_norm_9, image_11, digChoices]
            for thisComponent in digOptionsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "digOptions" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_norm_9* updates
                
                # if text_norm_9 is starting this frame...
                if text_norm_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_norm_9.frameNStart = frameN  # exact frame index
                    text_norm_9.tStart = t  # local t and not account for scr refresh
                    text_norm_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_norm_9, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    text_norm_9.status = STARTED
                    text_norm_9.setAutoDraw(True)
                
                # if text_norm_9 is active this frame...
                if text_norm_9.status == STARTED:
                    # update params
                    pass
                
                # if text_norm_9 is stopping this frame...
                if text_norm_9.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_norm_9.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        text_norm_9.tStop = t  # not accounting for scr refresh
                        text_norm_9.tStopRefresh = tThisFlipGlobal  # on global time
                        text_norm_9.frameNStop = frameN  # exact frame index
                        # update status
                        text_norm_9.status = FINISHED
                        text_norm_9.setAutoDraw(False)
                
                # *image_11* updates
                
                # if image_11 is starting this frame...
                if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_11.frameNStart = frameN  # exact frame index
                    image_11.tStart = t  # local t and not account for scr refresh
                    image_11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_11.started')
                    # update status
                    image_11.status = STARTED
                    image_11.setAutoDraw(True)
                
                # if image_11 is active this frame...
                if image_11.status == STARTED:
                    # update params
                    pass
                
                # if image_11 is stopping this frame...
                if image_11.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_11.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        image_11.tStop = t  # not accounting for scr refresh
                        image_11.tStopRefresh = tThisFlipGlobal  # on global time
                        image_11.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_11.stopped')
                        # update status
                        image_11.status = FINISHED
                        image_11.setAutoDraw(False)
                
                # *digChoices* updates
                waitOnFlip = False
                
                # if digChoices is starting this frame...
                if digChoices.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    digChoices.frameNStart = frameN  # exact frame index
                    digChoices.tStart = t  # local t and not account for scr refresh
                    digChoices.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(digChoices, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'digChoices.started')
                    # update status
                    digChoices.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(digChoices.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(digChoices.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if digChoices is stopping this frame...
                if digChoices.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > digChoices.tStartRefresh + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        digChoices.tStop = t  # not accounting for scr refresh
                        digChoices.tStopRefresh = tThisFlipGlobal  # on global time
                        digChoices.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'digChoices.stopped')
                        # update status
                        digChoices.status = FINISHED
                        digChoices.status = FINISHED
                if digChoices.status == STARTED and not waitOnFlip:
                    theseKeys = digChoices.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                    _digChoices_allKeys.extend(theseKeys)
                    if len(_digChoices_allKeys):
                        digChoices.keys = _digChoices_allKeys[0].name  # just the first key pressed
                        digChoices.rt = _digChoices_allKeys[0].rt
                        digChoices.duration = _digChoices_allKeys[0].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in digOptionsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "digOptions" ---
            for thisComponent in digOptionsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('digOptions.stopped', globalClock.getTime(format='float'))
            # check responses
            if digChoices.keys in ['', [], None]:  # No response was made
                digChoices.keys = None
            practiceDigLoop.addData('digChoices.keys',digChoices.keys)
            if digChoices.keys != None:  # we had a response
                practiceDigLoop.addData('digChoices.rt', digChoices.rt)
                practiceDigLoop.addData('digChoices.duration', digChoices.duration)
            # Run 'End Routine' code from code_4
            if digChoices.keys is not None and 'l' in digChoices.keys:
                practiceDigLoop.finished = True
                
            if digChoices.keys is None:
                too_slow_check = True
            else:
                too_slow_check = False
            
            thisExp.addData('trial_type','dig_choice')
            thisExp.addData('key_press',digChoices.keys)
            thisExp.nextEntry()
            if digChoices.keys:
                pracRT = practiceRTclock.getTime()
            else:
                pracRT = 'NA'
            study.append({
                "ID": "",
                "TrialType":f"Practice_Trial",
                "BlockNum": "",
                "AlienOrder": "",
                "QuizResp": "",
                "QuizFailedNum": "",
                "TimeElapsed": experiment_clock.getTime(),
                "RT": pracRT,
                "PRT": "",
                "Galaxy": "",
                "DecayRate": "",
                "AlienIndex": "",
                "GemValue": "",
                "TimeInBlock": ""
            })
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            
            # --- Prepare to start Routine "tooSlow" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('tooSlow.started', globalClock.getTime(format='float'))
            # skip this Routine if its 'Skip if' condition is True
            continueRoutine = continueRoutine and not (too_slow_check == False)
            # keep track of which components have finished
            tooSlowComponents = [too_slow_img]
            for thisComponent in tooSlowComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "tooSlow" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 2.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *too_slow_img* updates
                
                # if too_slow_img is starting this frame...
                if too_slow_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    too_slow_img.frameNStart = frameN  # exact frame index
                    too_slow_img.tStart = t  # local t and not account for scr refresh
                    too_slow_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(too_slow_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'too_slow_img.started')
                    # update status
                    too_slow_img.status = STARTED
                    too_slow_img.setAutoDraw(True)
                
                # if too_slow_img is active this frame...
                if too_slow_img.status == STARTED:
                    # update params
                    pass
                
                # if too_slow_img is stopping this frame...
                if too_slow_img.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > too_slow_img.tStartRefresh + 2.0-frameTolerance:
                        # keep track of stop time/frame for later
                        too_slow_img.tStop = t  # not accounting for scr refresh
                        too_slow_img.tStopRefresh = tThisFlipGlobal  # on global time
                        too_slow_img.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'too_slow_img.stopped')
                        # update status
                        too_slow_img.status = FINISHED
                        too_slow_img.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in tooSlowComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "tooSlow" ---
            for thisComponent in tooSlowComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('tooSlow.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_11
            thisExp.addData('trial_type','too_slow')
            thisExp.nextEntry()
            
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
                "GemValue": "",
                "TimeInBlock": ""
            })
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-2.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 10.0 repeats of 'practiceDigLoop'
        
        # get names of stimulus parameters
        if practiceDigLoop.trialList in ([], [None], None):
            params = []
        else:
            params = practiceDigLoop.trialList[0].keys()
        # save data for this loop
        practiceDigLoop.saveAsExcel(filename + '.xlsx', sheetName='practiceDigLoop',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # set up handler to look after randomisation of conditions etc
        practiceTravelLoop = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('psychopy-vars.xlsx'),
            seed=None, name='practiceTravelLoop')
        thisExp.addLoop(practiceTravelLoop)  # add the loop to the experiment
        thisPracticeTravelLoop = practiceTravelLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeTravelLoop.rgb)
        if thisPracticeTravelLoop != None:
            for paramName in thisPracticeTravelLoop:
                globals()[paramName] = thisPracticeTravelLoop[paramName]
        
        for thisPracticeTravelLoop in practiceTravelLoop:
            currentLoop = practiceTravelLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisPracticeTravelLoop.rgb)
            if thisPracticeTravelLoop != None:
                for paramName in thisPracticeTravelLoop:
                    globals()[paramName] = thisPracticeTravelLoop[paramName]
            
            # --- Prepare to start Routine "travelLoop" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('travelLoop.started', globalClock.getTime(format='float'))
            image_7.setImage(rocket_image)
            # Run 'Begin Routine' code from code_9
            t_loop +=1
            # keep track of which components have finished
            travelLoopComponents = [image_7]
            for thisComponent in travelLoopComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "travelLoop" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_7* updates
                
                # if image_7 is starting this frame...
                if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_7.frameNStart = frameN  # exact frame index
                    image_7.tStart = t  # local t and not account for scr refresh
                    image_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_7.started')
                    # update status
                    image_7.status = STARTED
                    image_7.setAutoDraw(True)
                
                # if image_7 is active this frame...
                if image_7.status == STARTED:
                    # update params
                    pass
                
                # if image_7 is stopping this frame...
                if image_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_7.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        image_7.tStop = t  # not accounting for scr refresh
                        image_7.tStopRefresh = tThisFlipGlobal  # on global time
                        image_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_7.stopped')
                        # update status
                        image_7.status = FINISHED
                        image_7.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in travelLoopComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "travelLoop" ---
            for thisComponent in travelLoopComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('travelLoop.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_9
            if mainPhase:
                
                if block_timer.getTime() >= block_duration:
                    timeLoop.finished = True
                    if numBlocks == 5:
                        endStudy = True
            if t_loop == 1:
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
                thisExp.addData('trial_type','travel_trial')
                thisExp.nextEntry()
            
            
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'practiceTravelLoop'
        
        # get names of stimulus parameters
        if practiceTravelLoop.trialList in ([], [None], None):
            params = []
        else:
            params = practiceTravelLoop.trialList[0].keys()
        # save data for this loop
        practiceTravelLoop.saveAsExcel(filename + '.xlsx', sheetName='practiceTravelLoop',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "travel_init" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('travel_init.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        travel_initComponents = [image_15]
        for thisComponent in travel_initComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "travel_init" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_15* updates
            
            # if image_15 is starting this frame...
            if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_15.frameNStart = frameN  # exact frame index
                image_15.tStart = t  # local t and not account for scr refresh
                image_15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_15.started')
                # update status
                image_15.status = STARTED
                image_15.setAutoDraw(True)
            
            # if image_15 is active this frame...
            if image_15.status == STARTED:
                # update params
                pass
            
            # if image_15 is stopping this frame...
            if image_15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_15.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image_15.tStop = t  # not accounting for scr refresh
                    image_15.tStopRefresh = tThisFlipGlobal  # on global time
                    image_15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_15.stopped')
                    # update status
                    image_15.status = FINISHED
                    image_15.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in travel_initComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "travel_init" ---
        for thisComponent in travel_initComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('travel_init.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "choiceScreen" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('choiceScreen.started', globalClock.getTime(format='float'))
        # reset buttonPractice to account for continued clicks & clear times on/off
        buttonPractice.reset()
        # reset buttonReal to account for continued clicks & clear times on/off
        buttonReal.reset()
        # keep track of which components have finished
        choiceScreenComponents = [text_norm_12, buttonPractice, buttonReal]
        for thisComponent in choiceScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "choiceScreen" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_norm_12* updates
            
            # if text_norm_12 is starting this frame...
            if text_norm_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_norm_12.frameNStart = frameN  # exact frame index
                text_norm_12.tStart = t  # local t and not account for scr refresh
                text_norm_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_norm_12, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_norm_12.status = STARTED
                text_norm_12.setAutoDraw(True)
            
            # if text_norm_12 is active this frame...
            if text_norm_12.status == STARTED:
                # update params
                pass
            # *buttonPractice* updates
            
            # if buttonPractice is starting this frame...
            if buttonPractice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                buttonPractice.frameNStart = frameN  # exact frame index
                buttonPractice.tStart = t  # local t and not account for scr refresh
                buttonPractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buttonPractice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'buttonPractice.started')
                # update status
                buttonPractice.status = STARTED
                buttonPractice.setAutoDraw(True)
            
            # if buttonPractice is active this frame...
            if buttonPractice.status == STARTED:
                # update params
                pass
                # check whether buttonPractice has been pressed
                if buttonPractice.isClicked:
                    if not buttonPractice.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        buttonPractice.timesOn.append(buttonPractice.buttonClock.getTime())
                        buttonPractice.timesOff.append(buttonPractice.buttonClock.getTime())
                    elif len(buttonPractice.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        buttonPractice.timesOff[-1] = buttonPractice.buttonClock.getTime()
                    if not buttonPractice.wasClicked:
                        # end routine when buttonPractice is clicked
                        continueRoutine = False
                    if not buttonPractice.wasClicked:
                        # run callback code when buttonPractice is clicked
                        pass
            # take note of whether buttonPractice was clicked, so that next frame we know if clicks are new
            buttonPractice.wasClicked = buttonPractice.isClicked and buttonPractice.status == STARTED
            # *buttonReal* updates
            
            # if buttonReal is starting this frame...
            if buttonReal.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                buttonReal.frameNStart = frameN  # exact frame index
                buttonReal.tStart = t  # local t and not account for scr refresh
                buttonReal.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(buttonReal, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'buttonReal.started')
                # update status
                buttonReal.status = STARTED
                buttonReal.setAutoDraw(True)
            
            # if buttonReal is active this frame...
            if buttonReal.status == STARTED:
                # update params
                pass
                # check whether buttonReal has been pressed
                if buttonReal.isClicked:
                    if not buttonReal.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        buttonReal.timesOn.append(buttonReal.buttonClock.getTime())
                        buttonReal.timesOff.append(buttonReal.buttonClock.getTime())
                    elif len(buttonReal.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        buttonReal.timesOff[-1] = buttonReal.buttonClock.getTime()
                    if not buttonReal.wasClicked:
                        # end routine when buttonReal is clicked
                        continueRoutine = False
                    if not buttonReal.wasClicked:
                        # run callback code when buttonReal is clicked
                        pass
            # take note of whether buttonReal was clicked, so that next frame we know if clicks are new
            buttonReal.wasClicked = buttonReal.isClicked and buttonReal.status == STARTED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in choiceScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "choiceScreen" ---
        for thisComponent in choiceScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('choiceScreen.stopped', globalClock.getTime(format='float'))
        practiceLoop.addData('buttonPractice.numClicks', buttonPractice.numClicks)
        if buttonPractice.numClicks:
           practiceLoop.addData('buttonPractice.timesOn', buttonPractice.timesOn)
           practiceLoop.addData('buttonPractice.timesOff', buttonPractice.timesOff)
        else:
           practiceLoop.addData('buttonPractice.timesOn', "")
           practiceLoop.addData('buttonPractice.timesOff', "")
        practiceLoop.addData('buttonReal.numClicks', buttonReal.numClicks)
        if buttonReal.numClicks:
           practiceLoop.addData('buttonReal.timesOn', buttonReal.timesOn)
           practiceLoop.addData('buttonReal.timesOff', buttonReal.timesOff)
        else:
           practiceLoop.addData('buttonReal.timesOn', "")
           practiceLoop.addData('buttonReal.timesOff', "")
        # Run 'End Routine' code from code_5
        if buttonPractice.isClicked:
            choice = 'practice'
        
        elif buttonReal.isClicked:
            choice = 'real'
            practiceLoop.finished = True
            
            
        thisExp.addData('trial_type','practice_move_on')
        thisExp.nextEntry()
        study.append({
            "ID": "",
            "TrialType":f"Instruction_Button",
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
        # the Routine "choiceScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 10.0 repeats of 'practiceLoop'
    
    # get names of stimulus parameters
    if practiceLoop.trialList in ([], [None], None):
        params = []
    else:
        params = practiceLoop.trialList[0].keys()
    # save data for this loop
    practiceLoop.saveAsExcel(filename + '.xlsx', sheetName='practiceLoop',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    blockLoopFull = data.TrialHandler(nReps=5.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='blockLoopFull')
    thisExp.addLoop(blockLoopFull)  # add the loop to the experiment
    thisBlockLoopFull = blockLoopFull.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlockLoopFull.rgb)
    if thisBlockLoopFull != None:
        for paramName in thisBlockLoopFull:
            globals()[paramName] = thisBlockLoopFull[paramName]
    
    for thisBlockLoopFull in blockLoopFull:
        currentLoop = blockLoopFull
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisBlockLoopFull.rgb)
        if thisBlockLoopFull != None:
            for paramName in thisBlockLoopFull:
                globals()[paramName] = thisBlockLoopFull[paramName]
        
        # --- Prepare to start Routine "Instruct9" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Instruct9.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        Instruct9Components = [text_norm_10]
        for thisComponent in Instruct9Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Instruct9" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_norm_10* updates
            
            # if text_norm_10 is starting this frame...
            if text_norm_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_norm_10.frameNStart = frameN  # exact frame index
                text_norm_10.tStart = t  # local t and not account for scr refresh
                text_norm_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_norm_10, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_norm_10.status = STARTED
                text_norm_10.setAutoDraw(True)
            
            # if text_norm_10 is active this frame...
            if text_norm_10.status == STARTED:
                # update params
                pass
            
            # if text_norm_10 is stopping this frame...
            if text_norm_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_norm_10.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_norm_10.tStop = t  # not accounting for scr refresh
                    text_norm_10.tStopRefresh = tThisFlipGlobal  # on global time
                    text_norm_10.frameNStop = frameN  # exact frame index
                    # update status
                    text_norm_10.status = FINISHED
                    text_norm_10.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instruct9Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instruct9" ---
        for thisComponent in Instruct9Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Instruct9.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from text_align_9
        first_trial = True
        galaxy = None
        mainPhase = True
        if first_trial:
            galaxy = np.random.randint(0, 3)
        else:
            percentNum = np.random.randint(1, 11)
            if percentNum > 8:
                newGalaxy = galaxy
                while newGalaxy == galaxy:
                    newGalaxy = np.random.randint(0, 3)
                galaxy = newGalaxy
        print(galaxy)
        decay = get_decay_rate(galaxy=galaxy)
        gem = round(np.max([np.min([np.random.normal(100,5),135]),0]))
        gem_path = f"../images/task_images/gems/{gem}.jpg"
        
        from psychopy import core
        block_timer = core.Clock()
        block_duration = 6 * 60  # 6 minutes
        
        numBlocks +=1
        
        thisExp.addData('trial_type','beginBlock')
        thisExp.addData('blockNum',numBlocks)
        thisExp.addData('Galaxy',galaxy)
        thisExp.addData('alienIndex',alien_index)
        thisExp.addData('planet',planets[alien_index])
        thisExp.nextEntry()
        
        study.append({
            "ID": "",
            "TrialType":f"start_loop",
            "BlockNum": numBlocks,
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
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # set up handler to look after randomisation of conditions etc
        timeLoop = data.TrialHandler(nReps=300.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='timeLoop')
        thisExp.addLoop(timeLoop)  # add the loop to the experiment
        thisTimeLoop = timeLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTimeLoop.rgb)
        if thisTimeLoop != None:
            for paramName in thisTimeLoop:
                globals()[paramName] = thisTimeLoop[paramName]
        
        for thisTimeLoop in timeLoop:
            currentLoop = timeLoop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTimeLoop.rgb)
            if thisTimeLoop != None:
                for paramName in thisTimeLoop:
                    globals()[paramName] = thisTimeLoop[paramName]
            
            # --- Prepare to start Routine "alienVisit" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('alienVisit.started', globalClock.getTime(format='float'))
            image_12.setImage(planets[alien_index])
            # keep track of which components have finished
            alienVisitComponents = [image_12]
            for thisComponent in alienVisitComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "alienVisit" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 5.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_12* updates
                
                # if image_12 is starting this frame...
                if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_12.frameNStart = frameN  # exact frame index
                    image_12.tStart = t  # local t and not account for scr refresh
                    image_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_12.started')
                    # update status
                    image_12.status = STARTED
                    image_12.setAutoDraw(True)
                
                # if image_12 is active this frame...
                if image_12.status == STARTED:
                    # update params
                    pass
                
                # if image_12 is stopping this frame...
                if image_12.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_12.tStartRefresh + 5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_12.tStop = t  # not accounting for scr refresh
                        image_12.tStopRefresh = tThisFlipGlobal  # on global time
                        image_12.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_12.stopped')
                        # update status
                        image_12.status = FINISHED
                        image_12.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in alienVisitComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "alienVisit" ---
            for thisComponent in alienVisitComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('alienVisit.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from code_6
            alien_index += 1
            first_trial = False
            prt_check = True
            if first_trial:
                galaxy = np.random.randint(0, 3)
            else:
                percentNum = np.random.randint(1, 11)
                if percentNum > 8:
                    newGalaxy = galaxy
                    while newGalaxy == galaxy:
                        newGalaxy = np.random.randint(0, 3)
                    galaxy = newGalaxy
            print(galaxy)
            decay = get_decay_rate(galaxy=galaxy)
            gem = round(np.max([np.min([np.random.normal(100,5),135]),0]))
            gem_path = f"../images/task_images/gems/{gem}.jpg"
            
            thisExp.addData('gemValue',gem)
            thisExp.addData('decay_rate',decay)
            thisExp.nextEntry()
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.000000)
            
            # set up handler to look after randomisation of conditions etc
            digloop_main = data.TrialHandler(nReps=100.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='digloop_main')
            thisExp.addLoop(digloop_main)  # add the loop to the experiment
            thisDigloop_main = digloop_main.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisDigloop_main.rgb)
            if thisDigloop_main != None:
                for paramName in thisDigloop_main:
                    globals()[paramName] = thisDigloop_main[paramName]
            
            for thisDigloop_main in digloop_main:
                currentLoop = digloop_main
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisDigloop_main.rgb)
                if thisDigloop_main != None:
                    for paramName in thisDigloop_main:
                        globals()[paramName] = thisDigloop_main[paramName]
                
                # set up handler to look after randomisation of conditions etc
                digs = data.TrialHandler(nReps=1.0, method='sequential', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=data.importConditions('psychopy-vars.xlsx', selection='0:3'),
                    seed=None, name='digs')
                thisExp.addLoop(digs)  # add the loop to the experiment
                thisDig = digs.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisDig.rgb)
                if thisDig != None:
                    for paramName in thisDig:
                        globals()[paramName] = thisDig[paramName]
                
                for thisDig in digs:
                    currentLoop = digs
                    thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisDig.rgb)
                    if thisDig != None:
                        for paramName in thisDig:
                            globals()[paramName] = thisDig[paramName]
                    
                    # --- Prepare to start Routine "digLoop" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('digLoop.started', globalClock.getTime(format='float'))
                    image_4.setImage(dig_image)
                    # keep track of which components have finished
                    digLoopComponents = [image_4]
                    for thisComponent in digLoopComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "digLoop" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 0.666667:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *image_4* updates
                        
                        # if image_4 is starting this frame...
                        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            image_4.frameNStart = frameN  # exact frame index
                            image_4.tStart = t  # local t and not account for scr refresh
                            image_4.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'image_4.started')
                            # update status
                            image_4.status = STARTED
                            image_4.setAutoDraw(True)
                        
                        # if image_4 is active this frame...
                        if image_4.status == STARTED:
                            # update params
                            pass
                        
                        # if image_4 is stopping this frame...
                        if image_4.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > image_4.tStartRefresh + 0.666667-frameTolerance:
                                # keep track of stop time/frame for later
                                image_4.tStop = t  # not accounting for scr refresh
                                image_4.tStopRefresh = tThisFlipGlobal  # on global time
                                image_4.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'image_4.stopped')
                                # update status
                                image_4.status = FINISHED
                                image_4.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in digLoopComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "digLoop" ---
                    for thisComponent in digLoopComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('digLoop.stopped', globalClock.getTime(format='float'))
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-0.666667)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed 1.0 repeats of 'digs'
                
                # get names of stimulus parameters
                if digs.trialList in ([], [None], None):
                    params = []
                else:
                    params = digs.trialList[0].keys()
                # save data for this loop
                digs.saveAsExcel(filename + '.xlsx', sheetName='digs',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                
                # --- Prepare to start Routine "digTrial" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('digTrial.started', globalClock.getTime(format='float'))
                gemIMG.setImage(gem_path)
                # keep track of which components have finished
                digTrialComponents = [gemIMG]
                for thisComponent in digTrialComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "digTrial" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.5:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *gemIMG* updates
                    
                    # if gemIMG is starting this frame...
                    if gemIMG.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        gemIMG.frameNStart = frameN  # exact frame index
                        gemIMG.tStart = t  # local t and not account for scr refresh
                        gemIMG.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(gemIMG, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'gemIMG.started')
                        # update status
                        gemIMG.status = STARTED
                        gemIMG.setAutoDraw(True)
                    
                    # if gemIMG is active this frame...
                    if gemIMG.status == STARTED:
                        # update params
                        pass
                    
                    # if gemIMG is stopping this frame...
                    if gemIMG.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > gemIMG.tStartRefresh + 1.5-frameTolerance:
                            # keep track of stop time/frame for later
                            gemIMG.tStop = t  # not accounting for scr refresh
                            gemIMG.tStopRefresh = tThisFlipGlobal  # on global time
                            gemIMG.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'gemIMG.stopped')
                            # update status
                            gemIMG.status = FINISHED
                            gemIMG.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in digTrialComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "digTrial" ---
                for thisComponent in digTrialComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('digTrial.stopped', globalClock.getTime(format='float'))
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.500000)
                
                # --- Prepare to start Routine "stay_leave" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('stay_leave.started', globalClock.getTime(format='float'))
                digChoices_2.keys = []
                digChoices_2.rt = []
                _digChoices_2_allKeys = []
                # Run 'Begin Routine' code from code_8
                RTclock =core.Clock()
                # keep track of which components have finished
                stay_leaveComponents = [text_norm_11, image_13, digChoices_2]
                for thisComponent in stay_leaveComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "stay_leave" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 2.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_norm_11* updates
                    
                    # if text_norm_11 is starting this frame...
                    if text_norm_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_norm_11.frameNStart = frameN  # exact frame index
                        text_norm_11.tStart = t  # local t and not account for scr refresh
                        text_norm_11.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_norm_11, 'tStartRefresh')  # time at next scr refresh
                        # update status
                        text_norm_11.status = STARTED
                        text_norm_11.setAutoDraw(True)
                    
                    # if text_norm_11 is active this frame...
                    if text_norm_11.status == STARTED:
                        # update params
                        pass
                    
                    # if text_norm_11 is stopping this frame...
                    if text_norm_11.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_norm_11.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            text_norm_11.tStop = t  # not accounting for scr refresh
                            text_norm_11.tStopRefresh = tThisFlipGlobal  # on global time
                            text_norm_11.frameNStop = frameN  # exact frame index
                            # update status
                            text_norm_11.status = FINISHED
                            text_norm_11.setAutoDraw(False)
                    
                    # *image_13* updates
                    
                    # if image_13 is starting this frame...
                    if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_13.frameNStart = frameN  # exact frame index
                        image_13.tStart = t  # local t and not account for scr refresh
                        image_13.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_13.started')
                        # update status
                        image_13.status = STARTED
                        image_13.setAutoDraw(True)
                    
                    # if image_13 is active this frame...
                    if image_13.status == STARTED:
                        # update params
                        pass
                    
                    # if image_13 is stopping this frame...
                    if image_13.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > image_13.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            image_13.tStop = t  # not accounting for scr refresh
                            image_13.tStopRefresh = tThisFlipGlobal  # on global time
                            image_13.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'image_13.stopped')
                            # update status
                            image_13.status = FINISHED
                            image_13.setAutoDraw(False)
                    
                    # *digChoices_2* updates
                    waitOnFlip = False
                    
                    # if digChoices_2 is starting this frame...
                    if digChoices_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        digChoices_2.frameNStart = frameN  # exact frame index
                        digChoices_2.tStart = t  # local t and not account for scr refresh
                        digChoices_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(digChoices_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'digChoices_2.started')
                        # update status
                        digChoices_2.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(digChoices_2.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(digChoices_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if digChoices_2 is stopping this frame...
                    if digChoices_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > digChoices_2.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            digChoices_2.tStop = t  # not accounting for scr refresh
                            digChoices_2.tStopRefresh = tThisFlipGlobal  # on global time
                            digChoices_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'digChoices_2.stopped')
                            # update status
                            digChoices_2.status = FINISHED
                            digChoices_2.status = FINISHED
                    if digChoices_2.status == STARTED and not waitOnFlip:
                        theseKeys = digChoices_2.getKeys(keyList=['a','l'], ignoreKeys=["escape"], waitRelease=False)
                        _digChoices_2_allKeys.extend(theseKeys)
                        if len(_digChoices_2_allKeys):
                            digChoices_2.keys = _digChoices_2_allKeys[0].name  # just the first key pressed
                            digChoices_2.rt = _digChoices_2_allKeys[0].rt
                            digChoices_2.duration = _digChoices_2_allKeys[0].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in stay_leaveComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "stay_leave" ---
                for thisComponent in stay_leaveComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('stay_leave.stopped', globalClock.getTime(format='float'))
                # check responses
                if digChoices_2.keys in ['', [], None]:  # No response was made
                    digChoices_2.keys = None
                digloop_main.addData('digChoices_2.keys',digChoices_2.keys)
                if digChoices_2.keys != None:  # we had a response
                    digloop_main.addData('digChoices_2.rt', digChoices_2.rt)
                    digloop_main.addData('digChoices_2.duration', digChoices_2.duration)
                # Run 'End Routine' code from code_8
                gem = round(decay*gem) # Adds decay to next gem value for following trial
                image_prefix = '../images/task_images/'
                gem_path = image_prefix + f"gems/{gem}.jpg"
                if prt_check:
                    prt_clock = core.Clock()
                t_loop = 0
                prt_check = False
                thisExp.addData('trial_type', 'dig_choice')
                if digChoices_2.keys is not None and 'l' in digChoices_2.keys:
                    digloop_main.finished = True
                    thisExp.addData('PRT', prt_clock.getTime())
                    thisExp.addData('key_press','l')
                    thisExp.nextEntry()
                if digChoices_2.keys is not None and 'a' in digChoices_2.keys:
                    thisExp.addData('key_press','a')
                    thisExp.nextEntry()
                    
                if digChoices_2.keys is None:
                    too_slow_check = True
                    thisExp.nextEntry()
                else:
                    too_slow_check = False
                if digChoices_2.keys:
                    RT = RTclock.getTime()
                else:
                    RT = 'NA'
                dig_index += 1
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
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-2.000000)
                
                # --- Prepare to start Routine "tooSlow" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('tooSlow.started', globalClock.getTime(format='float'))
                # skip this Routine if its 'Skip if' condition is True
                continueRoutine = continueRoutine and not (too_slow_check == False)
                # keep track of which components have finished
                tooSlowComponents = [too_slow_img]
                for thisComponent in tooSlowComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "tooSlow" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 2.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *too_slow_img* updates
                    
                    # if too_slow_img is starting this frame...
                    if too_slow_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        too_slow_img.frameNStart = frameN  # exact frame index
                        too_slow_img.tStart = t  # local t and not account for scr refresh
                        too_slow_img.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(too_slow_img, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'too_slow_img.started')
                        # update status
                        too_slow_img.status = STARTED
                        too_slow_img.setAutoDraw(True)
                    
                    # if too_slow_img is active this frame...
                    if too_slow_img.status == STARTED:
                        # update params
                        pass
                    
                    # if too_slow_img is stopping this frame...
                    if too_slow_img.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > too_slow_img.tStartRefresh + 2.0-frameTolerance:
                            # keep track of stop time/frame for later
                            too_slow_img.tStop = t  # not accounting for scr refresh
                            too_slow_img.tStopRefresh = tThisFlipGlobal  # on global time
                            too_slow_img.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'too_slow_img.stopped')
                            # update status
                            too_slow_img.status = FINISHED
                            too_slow_img.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in tooSlowComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "tooSlow" ---
                for thisComponent in tooSlowComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('tooSlow.stopped', globalClock.getTime(format='float'))
                # Run 'End Routine' code from code_11
                thisExp.addData('trial_type','too_slow')
                thisExp.nextEntry()
                
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
                    "GemValue": "",
                    "TimeInBlock": ""
                })
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-2.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 100.0 repeats of 'digloop_main'
            
            # get names of stimulus parameters
            if digloop_main.trialList in ([], [None], None):
                params = []
            else:
                params = digloop_main.trialList[0].keys()
            # save data for this loop
            digloop_main.saveAsExcel(filename + '.xlsx', sheetName='digloop_main',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # set up handler to look after randomisation of conditions etc
            travel_animation = data.TrialHandler(nReps=1.0, method='sequential', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions('psychopy-vars.xlsx'),
                seed=None, name='travel_animation')
            thisExp.addLoop(travel_animation)  # add the loop to the experiment
            thisTravel_animation = travel_animation.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTravel_animation.rgb)
            if thisTravel_animation != None:
                for paramName in thisTravel_animation:
                    globals()[paramName] = thisTravel_animation[paramName]
            
            for thisTravel_animation in travel_animation:
                currentLoop = travel_animation
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTravel_animation.rgb)
                if thisTravel_animation != None:
                    for paramName in thisTravel_animation:
                        globals()[paramName] = thisTravel_animation[paramName]
                
                # --- Prepare to start Routine "travelLoop" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('travelLoop.started', globalClock.getTime(format='float'))
                image_7.setImage(rocket_image)
                # Run 'Begin Routine' code from code_9
                t_loop +=1
                # keep track of which components have finished
                travelLoopComponents = [image_7]
                for thisComponent in travelLoopComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "travelLoop" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *image_7* updates
                    
                    # if image_7 is starting this frame...
                    if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_7.frameNStart = frameN  # exact frame index
                        image_7.tStart = t  # local t and not account for scr refresh
                        image_7.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_7.started')
                        # update status
                        image_7.status = STARTED
                        image_7.setAutoDraw(True)
                    
                    # if image_7 is active this frame...
                    if image_7.status == STARTED:
                        # update params
                        pass
                    
                    # if image_7 is stopping this frame...
                    if image_7.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > image_7.tStartRefresh + 1.0-frameTolerance:
                            # keep track of stop time/frame for later
                            image_7.tStop = t  # not accounting for scr refresh
                            image_7.tStopRefresh = tThisFlipGlobal  # on global time
                            image_7.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'image_7.stopped')
                            # update status
                            image_7.status = FINISHED
                            image_7.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in travelLoopComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "travelLoop" ---
                for thisComponent in travelLoopComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('travelLoop.stopped', globalClock.getTime(format='float'))
                # Run 'End Routine' code from code_9
                if mainPhase:
                    
                    if block_timer.getTime() >= block_duration:
                        timeLoop.finished = True
                        if numBlocks == 5:
                            endStudy = True
                if t_loop == 1:
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
                    thisExp.addData('trial_type','travel_trial')
                    thisExp.nextEntry()
                
                
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1.0 repeats of 'travel_animation'
            
            # get names of stimulus parameters
            if travel_animation.trialList in ([], [None], None):
                params = []
            else:
                params = travel_animation.trialList[0].keys()
            # save data for this loop
            travel_animation.saveAsExcel(filename + '.xlsx', sheetName='travel_animation',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            
            # --- Prepare to start Routine "travel_init" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('travel_init.started', globalClock.getTime(format='float'))
            # keep track of which components have finished
            travel_initComponents = [image_15]
            for thisComponent in travel_initComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "travel_init" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_15* updates
                
                # if image_15 is starting this frame...
                if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_15.frameNStart = frameN  # exact frame index
                    image_15.tStart = t  # local t and not account for scr refresh
                    image_15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_15.started')
                    # update status
                    image_15.status = STARTED
                    image_15.setAutoDraw(True)
                
                # if image_15 is active this frame...
                if image_15.status == STARTED:
                    # update params
                    pass
                
                # if image_15 is stopping this frame...
                if image_15.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_15.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        image_15.tStop = t  # not accounting for scr refresh
                        image_15.tStopRefresh = tThisFlipGlobal  # on global time
                        image_15.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_15.stopped')
                        # update status
                        image_15.status = FINISHED
                        image_15.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in travel_initComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "travel_init" ---
            for thisComponent in travel_initComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('travel_init.stopped', globalClock.getTime(format='float'))
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 300.0 repeats of 'timeLoop'
        
        # get names of stimulus parameters
        if timeLoop.trialList in ([], [None], None):
            params = []
        else:
            params = timeLoop.trialList[0].keys()
        # save data for this loop
        timeLoop.saveAsExcel(filename + '.xlsx', sheetName='timeLoop',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "homeBase" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('homeBase.started', globalClock.getTime(format='float'))
        # skip this Routine if its 'Skip if' condition is True
        continueRoutine = continueRoutine and not (endStudy)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # Run 'Begin Routine' code from code_12
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
                "TimeInBlock": block_timer.getTime() # Block time is fixed from block_loop
            })
        # keep track of which components have finished
        homeBaseComponents = [text_norm_13, image_14, key_resp_2]
        for thisComponent in homeBaseComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "homeBase" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 60.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_norm_13* updates
            
            # if text_norm_13 is starting this frame...
            if text_norm_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_norm_13.frameNStart = frameN  # exact frame index
                text_norm_13.tStart = t  # local t and not account for scr refresh
                text_norm_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_norm_13, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_norm_13.status = STARTED
                text_norm_13.setAutoDraw(True)
            
            # if text_norm_13 is active this frame...
            if text_norm_13.status == STARTED:
                # update params
                pass
            
            # if text_norm_13 is stopping this frame...
            if text_norm_13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_norm_13.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    text_norm_13.tStop = t  # not accounting for scr refresh
                    text_norm_13.tStopRefresh = tThisFlipGlobal  # on global time
                    text_norm_13.frameNStop = frameN  # exact frame index
                    # update status
                    text_norm_13.status = FINISHED
                    text_norm_13.setAutoDraw(False)
            
            # *image_14* updates
            
            # if image_14 is starting this frame...
            if image_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_14.frameNStart = frameN  # exact frame index
                image_14.tStart = t  # local t and not account for scr refresh
                image_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_14.started')
                # update status
                image_14.status = STARTED
                image_14.setAutoDraw(True)
            
            # if image_14 is active this frame...
            if image_14.status == STARTED:
                # update params
                pass
            
            # if image_14 is stopping this frame...
            if image_14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_14.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    image_14.tStop = t  # not accounting for scr refresh
                    image_14.tStopRefresh = tThisFlipGlobal  # on global time
                    image_14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_14.stopped')
                    # update status
                    image_14.status = FINISHED
                    image_14.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_2 is stopping this frame...
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 60-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                    # update status
                    key_resp_2.status = FINISHED
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[0].rt
                    key_resp_2.duration = _key_resp_2_allKeys[0].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in homeBaseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "homeBase" ---
        for thisComponent in homeBaseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('homeBase.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        blockLoopFull.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            blockLoopFull.addData('key_resp_2.rt', key_resp_2.rt)
            blockLoopFull.addData('key_resp_2.duration', key_resp_2.duration)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-60.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 5.0 repeats of 'blockLoopFull'
    
    # get names of stimulus parameters
    if blockLoopFull.trialList in ([], [None], None):
        params = []
    else:
        params = blockLoopFull.trialList[0].keys()
    # save data for this loop
    blockLoopFull.saveAsExcel(filename + '.xlsx', sheetName='blockLoopFull',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "thank_you" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('thank_you.started', globalClock.getTime(format='float'))
    key_instruct_9.keys = []
    key_instruct_9.rt = []
    _key_instruct_9_allKeys = []
    # keep track of which components have finished
    thank_youComponents = [text_norm_14, key_instruct_9]
    for thisComponent in thank_youComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "thank_you" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_norm_14* updates
        
        # if text_norm_14 is starting this frame...
        if text_norm_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_norm_14.frameNStart = frameN  # exact frame index
            text_norm_14.tStart = t  # local t and not account for scr refresh
            text_norm_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_norm_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_norm_14.status = STARTED
            text_norm_14.setAutoDraw(True)
        
        # if text_norm_14 is active this frame...
        if text_norm_14.status == STARTED:
            # update params
            pass
        
        # *key_instruct_9* updates
        waitOnFlip = False
        
        # if key_instruct_9 is starting this frame...
        if key_instruct_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_instruct_9.frameNStart = frameN  # exact frame index
            key_instruct_9.tStart = t  # local t and not account for scr refresh
            key_instruct_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_instruct_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_instruct_9.started')
            # update status
            key_instruct_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_instruct_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_instruct_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_instruct_9.status == STARTED and not waitOnFlip:
            theseKeys = key_instruct_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_instruct_9_allKeys.extend(theseKeys)
            if len(_key_instruct_9_allKeys):
                key_instruct_9.keys = _key_instruct_9_allKeys[0].name  # just the first key pressed
                key_instruct_9.rt = _key_instruct_9_allKeys[0].rt
                key_instruct_9.duration = _key_instruct_9_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thank_youComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thank_you" ---
    for thisComponent in thank_youComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('thank_you.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_instruct_9.keys in ['', [], None]:  # No response was made
        key_instruct_9.keys = None
    thisExp.addData('key_instruct_9.keys',key_instruct_9.keys)
    if key_instruct_9.keys != None:  # we had a response
        thisExp.addData('key_instruct_9.rt', key_instruct_9.rt)
        thisExp.addData('key_instruct_9.duration', key_instruct_9.duration)
    # Run 'End Routine' code from text_align_10
    thisExp.addData("trial_type","thank_you")
    thisExp.nextEntry()
    
    save_data(expInfo['participant'], study)
    thisExp.nextEntry()
    # the Routine "thank_you" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
