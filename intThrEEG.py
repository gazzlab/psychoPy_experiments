#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---#-O-o-#---# The path to the target/probe jpg files will vary based on the computer on which this is being run.  To edit the path, please go to line ~325 and amend 'MediTrain_Conditions'\
#----#---#-- to the appropriate subfile (ie: MediTrain_Conditions_EmtecThumbDrive.xlsx or MediTrain_Conditions_Gazzlab19.xlsx). 
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.74.00), Tue Dec 18 15:38:18 2012
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division #so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import * #things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray, mean
from numpy.random import random, randint, normal, shuffle
import copy, time #from the std python libs
import os #handy system and path functions
from random import choice
import psychopy.info #for information about the system



#store info about the experiment session
expName='MentalRotation_Thresholding'
expInfo={'participant ID':'', 'session':'001',}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
if expInfo['participant ID']=='':
    print "Please enter a valid participant ID"
    core.quit()
if expInfo['session']=='':
    print "Please enter a valid session ID "
    core.quit()


#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + 'intThr_{0}_{1}'.format(expInfo['participant ID'], expInfo['session'])
logFile=logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)#this outputs to the screen, not a file

#this Experiment Handler is going to keep track of multiple loops (one trial_loop randomly looping through target and probe stimuli, and another staircase_loop looping up and down in orientation, based on performance in previous trial)
thisExp = data.ExperimentHandler(name=expName, version='05/02/13',
    extraInfo=expInfo,
    runtimeInfo=None,
    originPath=None,
    savePickle=True,
    saveWideText=True,
    dataFileName=filename)
    
#setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb')
   
   #Initialise components for Routine "instr1"
instr1Clock=core.Clock()
welcome_txt=visual.TextStim(win=win, ori=0, name="welcome_txt",
    text="Welcome to the\r\nMental Rotation task!\r\n\n\n",
    font='Papyrus',
    pos=[0,4.5], height=1.5,wrapWidth=None,
    color='Peru', colorSpace='rgb', opacity=1,
    depth=0.0)
instr1_txt=visual.TextStim(win=win, ori=0, name='instr1_txt',
    text='\r\n\nYou will learn how to perform a specific, one-step mental rotation on an abstract shape.\r\n\nAfter viewing an abstract shape, you will respond as to whether a second shape, shown a few seconds later, matches your mental rotation.\r\n\nIf the shape matches your mental rotation, please press "YES"; if it does not match, please press "NO".',
    font='Lucida Bright',
    pos=[0, .0], height=.75,wrapWidth=None,
    color='NavajoWhite', colorSpace='rgb', opacity=.75,
    depth=0.0)
ready_1=visual.TextStim(win=win, ori=0, name='ready_1',
    text="Please press 'Enter' after you have read these instructions and are ready to continue.",
    font='Geneva',
    pos=[0, -10], height=.75,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0) 

#Initialise components for Routine "instr2"
instr2Clock=core.Clock()

instr2_staticjpg =visual.ImageStim(win=win,name='instr2_staticjpg',
    image='/Users/gazzlab/Desktop/IDv2_EEG/targetImages/009.jpg', mask=None,
    ori=0, pos=[-7.5,-5], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=False, depth=0)
instr2_rotatingjpg=visual.ImageStim(win=win,name='instr2_rotatingjpg',
    image='/Users/gazzlab/Desktop/IDv2_EEG/targetImages/009.jpg', mask=None,
    ori=90, pos=[0,-5], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=128, interpolate=False, depth=0)
instr2_txt=visual.TextStim(win=win, ori=0, name='instr2_txt',
    text='Mental Rotation Instructions:\r\n\n\nYou will be shown a shape.\r\nRotate this shape clockwise by 90 degrees',
    font='Geneva',
    pos=[0,5], height=0.65,wrapWidth=None,
    color='aqua', colorSpace='rgb', opacity=1,
    depth=0.0)

instr2_clockwise=visual.ImageStim(win=win,name='instr2_clockwise',
    image='/Users/gazzlab/Desktop/IDv2_EEG/otherImages/circle_360.gif', mask=None,
    ori=0, pos=[0,-5], size=[6,6],
    color=[1,1,1], colorSpace='rgb', opacity=.3,
    texRes=128, interpolate=True, depth=-1)

instr2_ready=visual.TextStim(win=win, ori=0, name='instr2_ready',
    text="Please press ENTER when you are ready to begin the task.",
    font='Geneva',
    pos=[0, -11], height=.6,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
   
  
 #initialize components for Routine "yourTarget": yourTarget_text, target_image,
yourTargetClock=core.Clock()
yourTarget_text=visual.TextStim(win=win, ori=0, name='yourTarget_text',
    text='You will begin with 5 practice trials\r\n\n\n\n\n\t\t\t\tPlease press ENTER when you are ready.', #will be updated for recorded runs (myCount1 and myCount2)
    pos=[0,4], height=.75,wrapWidth=None,
    color='DeepSkyBlue', colorSpace='rgb', opacity=1,
    depth=-2.0)
    
photodiodeSquare = visual.GratingStim(win=win, name='photodiodeSquare',
    tex=None, mask=None,
    ori=0, pos=[0, 0], size=[4, 4], sf=None, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
    
photodiodeSquare_Target = visual.GratingStim(win=win, name='photodiodeSquare_Target',
    tex=None, mask=None,
    ori=0, pos=[-13, 10], size=[4, 4], sf=None, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=True, depth=0.0)
#target_image=visual.ImageStim(win=win, name='target_image',
#    image='/Users/gazzlabgazzlab/Desktop/MediTrain/MediTrain_Targets/012.jpg', mask=None, #image is set to change on the practice run (myCount 0) and each of the recorded runs (myCount 1 and 2)
#    ori=0, pos=[0,3], size=None, #[0.2, 0.2],
#    color=[1,1,1], colorSpace='rgb', opacity=1,
#    texRes=300, interpolate=False, depth=-3.0) 
   
#initialize components  for pre_cross
pre_crossClock=core.Clock()
pre_crossCross=visual.TextStim(win=win, ori=0, name='pre_crossCross',
    text='+',
    font='Arial',
    pos=[0, 0], height=1,wrapWidth=None,
    color='yellow', colorSpace='rgb', opacity=1,
    depth=0.0) 
   
#  #Initialise components for Routine "ExpTrial"
ExpTrialClock=core.Clock()
target_image_clock=core.Clock()
probe_clock=core.Clock()
probe_resp_clock="noResp" 

target_fixationcross=visual.TextStim(win=win, ori=0, name='target_fixationcross',
    text='+',
    font='Arial',
    pos=[0, 0], height=1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

target_image=visual.ImageStim(win=win, name='target_image',
    image='sin', mask=None,
    ori=0, pos=[0,3], size=None, #[0.2, 0.2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=300, interpolate=True, depth=-3.0)
probe_jpg=visual.ImageStim(win=win, name='probe_jpg',
    image='sin', mask=None,
    pos=[0,3], size=None, 
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=300, interpolate=True, depth=-4.0)
exp_ready=visual.TextStim(win=win, ori=0, name='exp_ready',
    text="Please press ENTER when you are ready to begin your practice run.",
    font='Geneva',
    pos=[0, -5], height=.6,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)


#Initialise components for Routine "feedback"
feedbackClock=core.Clock()
msg='feedback_placeholder'
feedback_msg=visual.TextStim(win=win, ori=0, name='feedback_msg',
    text='+',
    font='Arial',
    pos=[0, 0], height=1,wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

#end of loops.. should cycle through t times before entering conclusion
#Initialise components for Routine "conclusion"
conclusionClock=core.Clock()
conclusion_text=visual.TextStim(win=win, ori=0, name='conclusion_text',
    text='Congratulations, you have completed the Mental Rotation task!  ',
    font='Lucida',
    pos=[0, 0], height=0.7,wrapWidth=None,
    color='DeepSkyBlue', colorSpace='rgb', opacity=1,
    depth=0.0)
# Create some handy timers
globalClock=core.Clock() #to track the time since experiment started
routineTimer=core.CountdownTimer() #to track time remaining of each (non-slip) routine 

#------Prepare to start Routine"instr1"-------
t=0; instr1Clock.reset() #clock 
frameN=-1
#update component parameters for each repeat
ready1_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
ready1_resp.status=NOT_STARTED
#keep track of which components have finished
instr1Components=[]
instr1Components.append(welcome_txt)
instr1Components.append(instr1_txt)
instr1Components.append(ready_1)
instr1Components.append(ready1_resp)
for thisComponent in instr1Components:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#-------Start Routine "instr1"-------
continueRoutine=True
while continueRoutine:
    #get current time
    t=instr1Clock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
        #*instr1_txt* updates
    if t>=0.0 and welcome_txt.status==NOT_STARTED:
        #keep track of start time/frame for later
        welcome_txt.tStart=t#underestimates by a little under one frame
        welcome_txt.frameNStart=frameN#exact frame index
        welcome_txt.setAutoDraw(True)
        
    if t>=1.5 and instr1_txt.status==NOT_STARTED:
        #keep track of start time/frame for later
        instr1_txt.tStart=t#underestimates by a little under one frame
        instr1_txt.frameNStart=frameN#exact frame index
        instr1_txt.setAutoDraw(True)
    
    #*ready_1* updates
    if t>=3 and ready_1.status==NOT_STARTED:
        #keep track of start time/frame for later
        ready_1.tStart=t#underestimates by a little under one frame
        ready_1.frameNStart=frameN#exact frame index
        ready_1.setAutoDraw(True)
    
    #*ready1_resp* updates
    if t>=1 and ready1_resp.status==NOT_STARTED:
        #keep track of start time/frame for later
        ready1_resp.tStart=t#underestimates by a little under one frame
        ready1_resp.frameNStart=frameN#exact frame index
        ready1_resp.status=STARTED
        #keyboard checking is just starting
        event.clearEvents
    if ready1_resp.status==STARTED:#only update if being drawn
        theseKeys = event.getKeys(keyList=['enter','return'])
        if len(theseKeys)>0:#at least one key was pressed
            #abort routine on response
            continueRoutine=False 
    #check if all components have finished
    if not continueRoutine: #a component has requested that we end
        routineTimer.reset() #this is the new t0 for non-slip Routines
        break
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()

#End of Routine "instr1"
for thisComponent in instr1Components:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    
    
    
    #------Prepare to start Routine"instr2"-------
t=0; instr2Clock.reset() #clock 
frameN=-1
#routineTimer.add(15.000000)

#update component parameters for each repeat
instr2_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
instr2_resp.status=NOT_STARTED
#keep track of which components have finished
instr2Components=[]
instr2Components.append(instr2_txt)
instr2Components.append(instr2_clockwise)
instr2Components.append(instr2_staticjpg)
instr2Components.append(instr2_rotatingjpg)
instr2Components.append(instr2_ready)
instr2Components.append(instr2_resp)


for thisComponent in instr2Components:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED

#-------Start Routine "instr2"-------
continueRoutine=True
while continueRoutine:
    #get current time
    t=instr2Clock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*instr2_txt* updates
    if t>=0.0 and instr2_txt.status==NOT_STARTED:
        #keep track of start time/frame for later
        instr2_txt.tStart=t#underestimates by a little under one frame
        instr2_txt.frameNStart=frameN#exact frame index
        instr2_txt.setAutoDraw(True)
#    elif instr2_txt.status==STARTED and t>=(30):
#        instr2_txt.setAutoDraw(False)
    

    #*instr2_staticjpg* updates
    if t>=0.0 and instr2_staticjpg.status==NOT_STARTED:
        #keep track of start time/frame for later
        instr2_staticjpg.tStart=t#underestimates by a little under one frame
        instr2_staticjpg.frameNStart=frameN#exact frame index
        instr2_staticjpg.setAutoDraw(True)
        
             #*instr2_clockwise* updates
    if t>=0.0 and instr2_clockwise.status==NOT_STARTED:
        #keep track of start time/frame for later
        instr2_clockwise.tStart=t#underestimates by a little under one frame
        instr2_clockwise.frameNStart=frameN#exact frame index
        instr2_clockwise.setAutoDraw(True)
        
    if t>=0.0 and instr2_rotatingjpg.status==NOT_STARTED:
        #keep track of start time/frame for later
        instr2_rotatingjpg.tStart=t#underestimates by a little under one frame
        instr2_rotatingjpg.frameNStart=frameN#exact frame index
        instr2_rotatingjpg.setAutoDraw(True)
        
        
    if t>=0.0 and instr2_ready.status==NOT_STARTED:
        #keep track of start time/frame for later
        instr2_ready.tStart=t#underestimates by a little under one frame
        instr2_ready.frameNStart=frameN#exact frame index
        instr2_ready.setAutoDraw(True)
   
  #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit() 
       
    if t>=1.000 and instr2_resp.status==NOT_STARTED:
        #keep track of start time/frame for later
        instr2_resp.tStart=t#underestimates by a little under one frame
        instr2_resp.frameNStart=frameN#exact frame index
        instr2_resp.status=STARTED
        #keyboard checking is just starting
        event.clearEvents
    if instr2_resp.status==STARTED:#only update if being drawn
        instr2Keys = event.getKeys(keyList=['enter','return','space','j'])
        if event.getKeys(["escape"]):
            core.quit()
        if len(instr2Keys)>0:
#            print "allKeys are:{0}".format(instr2Keys)
            continueRoutine=False 

           
          #check if all components have finished
    if not continueRoutine: #a component has requested that we end
        routineTimer.reset() #this is the new t0 for non-slip Routines
        break
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in instr2Components:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()
#End of Routine "instr2"
for thisComponent in instr2Components:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False) 
event.clearEvents

#check for quit (the [Esc] key)
if event.getKeys(["escape"]):
    core.quit()


add_ori=0#staircase adapted on each trial; only applied if ori_base is 45; if previous answer is correct, will increase by 2 (ie: 45+(0+2)-->47 degrees, which is closer to the anticipated 90 degrees); if previous answer is incorrect, add_ori will decrease by 4 (ie: 45 + (0-4)=41 degrees, a difference that should be more easy to detect)
ori_base=[] #in each trial, chosen randomly.  if 90, the target will be a match; if 45, the target will be a non-match
lastOris=[]
correctRotation=99
myCount=0

trialMax=30
if myCount==0:
    trialMax=8
 

while myCount <=2:
    nTrials=0
    #------Prepare to start Routine"yourTarget"-------
    t=0; yourTargetClock.reset() #clock 
    frameN=-1
    yourTarget_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
    yourTarget_resp.status=NOT_STARTED 
   
    if myCount==0:
        yourTarget_text.setText("You will begin with 5 practice trials.\r\n\n\n\n\n\n\n\n\n\nPress ENTER when you are ready to begin your practice run.")
    elif myCount==1:
        yourTarget_text.setText("Remember: rotate by 90 degrees clockwise.\r\n\n\n\n\nIf you have any questions, please ask.\r\n\nOtherwise, press ENTER when you are ready to begin run 1 of 2")
    elif myCount==2:
        yourTarget_text.setText("Feel free to take a short break.\r\n\n\n\n\n\n\n\n\nPlease press ENTER when you are ready to begin\r\n\run 2 of 2")
       
         #keep track of which components have finished
    yourTargetComponents=[]
    yourTargetComponents.append(yourTarget_text)
    yourTargetComponents.append(yourTarget_resp)

    for thisComponent in yourTargetComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
       
      
     #start yourTarget routine
    continueRoutine=True
    while continueRoutine:
    #get current time
        t=yourTargetClock.getTime()
        frameN=frameN+1
        if t>=0.0 and yourTarget_text.status==NOT_STARTED:
            #keep track of start time/frame for later
            yourTarget_text.tStart=t#underestimates by a little under one frame
            yourTarget_text.frameNStart=frameN#exact frame index
            yourTarget_text.setAutoDraw(True)
        #check for quit (the [Esc] key)
        if event.getKeys(["escape","q","j"]):
            core.quit()               
            
#        if t>=0.0 and target_image.status==NOT_STARTED:
#            #keep track of start time/frame for later
#            target_image.tStart=t#underestimates by a little under one frame
#            target_image.frameNStart=frameN#exact frame index
#            target_image.setAutoDraw(True)
            
        if t>=1.000 and yourTarget_resp.status==NOT_STARTED:
        #keep track of start time/frame for later
            yourTarget_resp.tStart=t#underestimates by a little under one frame
            yourTarget_resp.frameNStart=frameN#exact frame index
            yourTarget_resp.status=STARTED
            #keyboard checking is just starting
            event.clearEvents
        if yourTarget_resp.status==STARTED:#only update if being drawn
            yourTargetKeys = event.getKeys(keyList=['enter','return','space','j'])
                    #check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            if len(yourTargetKeys)>0:
#                print "yourTargetKeys are: {0}".format(yourTargetKeys)
                continueRoutine=False 
           
          #check if all components have finished
        if not continueRoutine: #a component has requested that we end
            routineTimer.reset() #this is the new t0 for non-slip Routines
            break
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in yourTargetComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
        #refresh the screen
        if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
            win.flip()
            
#    End of Routine "yourTarget"
    for thisComponent in yourTargetComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False) 
                #check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
            core.quit()
        
    event.clearEvents
                
    if event.getKeys(["escape","q","j"]):
        core.quit()
        
    #prepare to start pre_cross
    t=0; pre_crossClock.reset() #clock 
    frameN=-1
    routineTimer.add(2.0000)
    
    #keep track of which components have finished
    pre_crossComponents=[]
    pre_crossComponents.append(pre_crossCross)
    
    for thisComponent in pre_crossComponents:
        if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
        
    continueRoutine=True
    while continueRoutine:
        #get current time
        t=pre_crossClock.getTime()
        frameN=frameN+1#number of completed frames (so 0 in first frame)
        #update/draw components on each frame
                        #*pre_cross* updates
        if t>=0 and pre_crossCross.status==NOT_STARTED:
            #keep track of start time/frame for later
            pre_crossCross.tStart=t#underestimates by a little under one frame
            pre_crossCross.frameNStart=frameN#exact frame index
            pre_crossCross.setAutoDraw(True)
        elif pre_crossCross.status==STARTED and t>=(0.0+2.0):
            pre_crossCross.setAutoDraw(False)

            #check if all components have finished
        if not continueRoutine: #a component has requested that we end
            routineTimer.reset() #this is the new t0 for non-slip Routines
            break
        continueRoutine=False#will revert to True if at least one component still running
        for thisComponent in pre_crossComponents:
            if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()
    
    #End of Routine "pre_cross"
    for thisComponent in pre_crossComponents:
        if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
        
    event.clearEvents    

   
      #set up TRIAL handler to look after randomisation of conditions etc
    trials=data.TrialHandler(nReps=3, method='random',
        extraInfo=expInfo,
        originPath=None,
        trialList=data.importConditions('../conditionFiles/MediTrain_InternalConditions_thr_gazzlab.xlsx'),
        seed=None,
        name='trials_block{0}'.format(myCount))
    trials.data.addDataType('participant_ID')
    trials.data.addDataType('jpg_path')#random, from xlsx
    trials.data.addDataType('ori_base')#random, from xlsx
    trials.data.addDataType('add_ori')#staircased
    trials.data.addDataType('randomaddorsubtract')#how far should stimulus be rotated?
    trials.data.addDataType('actual_probe_ori')#how far is stimulus rotated?
    trials.data.addDataType('corr_ans')#either "0"(yes) or "."(no)
    trials.data.addDataType('key_resp.key')#
    trials.data.addDataType('key_resp.rt')#
    trials.data.addDataType('key_resp.corr')#works
    trials.data.addDataType('target_clock')
    trials.data.addDataType('probe_clock')
    trials.data.addDataType('probe_resp_clock')
    trials.data.addDataType('block')
    trials.data.addDataType('degreeDiff')
    trials.data.addDataType('photodiodeSquareClock')

    

    
    add_ori=add_ori#staircase adapted on each trial; only applied if ori_base is 45; if previous answer is correct, will increase by 2 (ie: 45+(0+2)-->47 degrees, which is closer to the anticipated 90 degrees); if previous answer is incorrect, add_ori will decrease by 4 (ie: 45 + (0-4)=41 degrees, a difference that should be more easy to detect)
    ori_base=[] #in each trial, chosen randomly.  if 90, the target will be a match; if 45, the target will be a non-match
    lastOris=[]
    correctRotation=99

    trialMax=30
    if myCount==0:
        trialMax=5
        
    thisExp.addLoop(trials)#add the loop to the experiment
    thisTrial=trials.trialList[0]#so we can initialise stimuli with some valuesdir 
    
    if nTrials>=trialMax:
        trials.finished=True

    elif nTrials<trialMax:
        for thisTrial in trials:

            ori_base=thisTrial.ori_base #in each trial, chosen randomly.  if 90, the target will be a match; if 45, the target will be a non-match
            target_clock="NoTargetClock"
            probe_clock="NoProbeClock"
            probe_resp_clock="NoProbeResp"
        
        
            if myCount<=1 and nTrials==0:
                add_ori=0
            else:
                if correctRotation==1:#for a correct response on the previous trial 
                    if add_ori<=42:
                        add_ori=add_ori+2
                    else:
                        add_ori=44  #will create a maximum add_ori of 45+44=89 degrees, which will be very difficult to distinguish from the anticipated rotation of 90 degrees
                elif correctRotation==0:
                    if add_ori>=-221:
                        add_ori=add_ori-4
                    else:
                        add_ori=-225 #will create a minimum add_ori of 45+-225=-180 degrees, which will be 270 degrees off of the anticipated rotation (90 degs).. should be easy  to distinguish
                        
            addto90=(90+(ori_base-add_ori))
            subfrom90=(90-(ori_base-add_ori))
            addorsub=[addto90,subfrom90]
            randomaddorsubtract=choice(addorsub)
        
            
            
            #------Prepare to start Routine"ExpTrial"-------
            t=0; ExpTrialClock.reset() #clock 
            frameN=-1
            routineTimer.add(8.500000)
            degreez=u"\u00B0"
            #update component parameters for each repeat
            target_image.setImage(thisTrial.targetJPGpath)
            probe_jpg.setImage(thisTrial.probeJPGpath)
            key_resp = event.BuilderKeyResponse() #create an object of type KeyResponse
            key_resp.status=NOT_STARTED
            if ori_base==90:
                probe_jpg.setOri(90) #match
                corr_ans="num_0" #"yes" on keypad"
                photodiodeSquare.setPos([13,-10])
            elif ori_base==45:
                probe_jpg.setOri(randomaddorsubtract) #not a match with target
                corr_ans="num_decimal" #"no" on keypad
                photodiodeSquare.setPos([-13,-10])

        
            
          #keep track of which components have finished
            ExpTrialComponents=[]
            ExpTrialComponents.append(target_fixationcross)
            ExpTrialComponents.append(target_image)
            ExpTrialComponents.append(probe_jpg)
            ExpTrialComponents.append(key_resp)
            ExpTrialComponents.append(photodiodeSquare)
            ExpTrialComponents.append(photodiodeSquare_Target)
            
            
            key_resp.keys="None"
            key_resp.rt="NoKeyResp"
            keyRespTime="noResponse"

            probe_resp_clock="NoProbeRespTime"
            correctRotation="noKeyPress"
            
            for thisComponent in ExpTrialComponents:
                if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
                    
            #-------Start Routine "ExpTrial"-------
            continueRoutine=True
            while continueRoutine and routineTimer.getTime()>0:
                #get current time
                t=ExpTrialClock.getTime()
                frameN=frameN+1#number of completed frames (so 0 in first frame)
                #update/draw components on each frame
                
#                #*pre_cross* updates
#                if t>=0.0 and pre_cross.status==NOT_STARTED:
#                    #keep track of start time/frame for later
#                    pre_cross.tStart=t#underestimates by a little under one frame
#                    pre_cross.frameNStart=frameN#exact frame index
#                    pre_cross.setAutoDraw(True)
#                elif pre_cross.status==STARTED and t>=(0.0+2.0):
#                    pre_cross.setAutoDraw(False)
                
                #*target_fixationcross* updates
                if t>=2 and target_fixationcross.status==NOT_STARTED:
                    #keep track of start time/frame for later
                    target_fixationcross.tStart=t#underestimates by a little under one frame
                    target_fixationcross.frameNStart=frameN#exact frame index
                    target_fixationcross.setAutoDraw(True)
                elif target_fixationcross.status==STARTED and t>=(2+6.5):
                    target_fixationcross.setAutoDraw(False)
        
        
                #*target_image* updates
                if t>=2 and target_image.status==NOT_STARTED:
                    #keep track of start time/frame for later
                    target_image.tStart=t#underestimates by a little under one frame
                    target_image.frameNStart=frameN#exact frame index
                    target_image.setAutoDraw(True)
                    target_image_clock=globalClock.getTime()
                elif target_image.status==STARTED and t>=(2+2.0):
                    target_image.setAutoDraw(False)
                    
                # *photodiodeSquare_Target* updates
                if t >= 2.0 and photodiodeSquare_Target.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    photodiodeSquare_Target.tStart = t  # underestimates by a little under one frame
                    photodiodeSquare_Target.frameNStart = frameN  # exact frame index
                    photodiodeSquare_Target.setAutoDraw(True)
        #            parallel.setPin(3,1)
    #                photodiodeSquareClock=globalClock.getTime()
                elif photodiodeSquare_Target.status == STARTED and t >= (2.0 + .005):
                    photodiodeSquare_Target.setAutoDraw(False)
                
                #*probe_jpg* updates
                if t>=6.500 and probe_jpg.status==NOT_STARTED: 
                    #keep track of start time/frame for later
                    probe_jpg.tStart=t#underestimates by a little under one frame
                    probe_jpg.frameNStart=frameN#exact frame index
                    probe_jpg.setAutoDraw(True)
                    probe_clock=globalClock.getTime()
                elif probe_jpg.status==STARTED and t>=(6.5+2): 
                    probe_jpg.setAutoDraw(False)
                    
                # *photodiodeSquare* updates
                if t >= 6.500 and photodiodeSquare.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    photodiodeSquare.tStart = t  # underestimates by a little under one frame
                    photodiodeSquare.frameNStart = frameN  # exact frame index
                    photodiodeSquare.setAutoDraw(True)
        #            parallel.setPin(3,1)
                    photodiodeSquareClock=globalClock.getTime()
                elif photodiodeSquare.status == STARTED and t >= (6.50 + .005):
                    photodiodeSquare.setAutoDraw(False)
                            
                
                #*key_resp* updates
                if t>=6.5 and key_resp.status==NOT_STARTED: 
                    #keep track of start time/frame for later
                    key_resp.tStart=t#underestimates by a little under one frame
                    key_resp.frameNStart=frameN#exact frame index
                    key_resp.status=STARTED
                    
                    #keyboard checking is just starting
                    key_resp.clock.reset() # now t=0
                    event.clearEvents()
                elif key_resp.status==STARTED and t>=(6.5+2.00): 
                    key_resp.status=STOPPED
                if key_resp.status==STARTED:#only update if being drawn
                    allKeys = event.getKeys() #(keyList=['num_decimal','num_0'])
                    if len(allKeys)>0: #at least one key was pressed
                        key_resp.keys=allKeys[-1]
                        key_resp.rt=key_resp.clock.getTime()
                        keyRespTime=float(key_resp.rt)

                        probe_resp_clock=globalClock.getTime()
                        # check for accuracy
                        if (key_resp.keys=='num_0' and ori_base==90) or (key_resp.keys=='num_decimal' and ori_base==45):
                            key_resp.corr=1
                            correctRotation=1
                        elif (key_resp.keys=='num_0' and ori_base==45) or (key_resp.keys=='num_decimal' and  ori_base==90):
                            key_resp.corr=0
                            correctRotation=0
                            
                        #abort routine on response
                        continueRoutine=False
        
                       #check if all components have finished
                if not continueRoutine: #a component has requested that we end
                    routineTimer.reset() #this is the new t0 for non-slip Routines
                    break
                    
                continueRoutine=False#will revert to True if at least one component still running
                for thisComponent in ExpTrialComponents:
                    if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                        continueRoutine=True; break #at least one component has not yet finished
        
               #check for quit (the [Esc] key)
                if event.getKeys(["escape"]):
                    core.quit()
            
                #refresh the screen
                if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
                    win.flip() 
                    
            for thisComponent in ExpTrialComponents:
                if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
                
            #print "ori_base={0}; add_ori={1}; random add/subtract={3}; actual_probe_ori={2}; corr_ans={4}".format(ori_base,add_ori,probe_jpg.ori, randomaddorsubtract, corr_ans)
            actual_probe_ori=probe_jpg.ori
            
        
        #------Prepare to start Routine"feedback"-------
            t=0; feedbackClock.reset() #clock 
            frameN=-1
            if keyRespTime!="noResponse":
                feedbackTime=(2.00-keyRespTime)
#                    print feedbackTime
            elif keyRespTime=="noResponse":
                feedbackTime=1.25
            routineTimer.add(feedbackTime)
                
        #update component parameters for each repeat
            if key_resp.corr:#stored on last run routine
              msg="+"
              feedback_msg.setColor('green')
            else:
              msg="+"
              feedback_msg.setColor('red')
            feedback_msg.setText(msg)
            #keep track of which components have finished
            feedbackComponents=[]
            feedbackComponents.append(feedback_msg)
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
                #-------Start Routine "feedback"-------
                continueRoutine=True
                while continueRoutine and routineTimer.getTime()>0:
                    #get current time
                    t=feedbackClock.getTime()
                    frameN=frameN+1#number of completed frames (so 0 in first frame)
                    #update/draw components on each frame 
                   
                    #*feedback_msg* updates
                    if t>=0.0 and feedback_msg.status==NOT_STARTED:
                        #keep track of start time/frame for later
                        feedback_msg.tStart=t#underestimates by a little under one frame
                        feedback_msg.frameNStart=frameN#exact frame index
                        feedback_msg.setAutoDraw(True)
                        mw_clock=globalClock.getTime()
                    elif feedback_msg.status==STARTED and t>=(0.0+feedbackTime):
                        feedback_msg.setAutoDraw(False)
                    
                    #check if all components have finished
                    if not continueRoutine: #a component has requested that we end
                        routineTimer.reset() #this is the new t0 for non-slip Routines
                        break
                    continueRoutine=False#will revert to True if at least one component still running
                    for thisComponent in feedbackComponents:
                        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
                            continueRoutine=True; break#at least one component has not yet finished
                    
                    #check for quit (the [Esc] key)
                    if event.getKeys(["escape"]):
                        core.quit()
                         
                        #refresh the screen
                    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                #End of Routine "feedback"
                for thisComponent in feedbackComponents:
                    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
            degreeDiff=90-(45+add_ori)
        
        
            trials.data.add('participant_ID', expInfo['participant ID'])#
            trials.data.add('jpg_path',thisTrial.probeJPGpath)#random, from xlsx
            trials.data.add('ori_base',ori_base)#random, from xlsx
            trials.data.add('add_ori',add_ori)#staircased
            trials.data.add('randomaddorsubtract',randomaddorsubtract)#how far should stimulus be rotated?
            trials.data.add('actual_probe_ori',actual_probe_ori)#how far is stimulus rotated?
            trials.data.add('corr_ans',corr_ans)#either "0"(yes) or "."(no)
            trials.data.add('key_resp.key',key_resp.keys)#
            trials.data.add('key_resp.rt',key_resp.rt)#
            trials.data.add('key_resp.corr',key_resp.corr)#works
            trials.data.add('target_clock',target_image_clock)
            trials.data.add('probe_clock',probe_clock)
            trials.data.add('probe_resp_clock',probe_resp_clock)
            trials.data.add('block',myCount)
            trials.data.add('degreeDiff',degreeDiff)
            trials.data.add('photodiodeSquareClock',photodiodeSquareClock)

            

            
        
            if nTrials>=25: #change back to 25
                lastOris.append((90-(45+add_ori)))
                
            #print "completed trial {0} on run {1}; degreeDiff={2}".format(nTrials,myCount,degreeDiff)
            nTrials=nTrials+1
            if nTrials==trialMax:
                
                
            #get names of stimulus parameters
                if trials.trialList in ([], [None], None):  params=[]
                else:  params = trials.trialList[0].keys()
                #save data for this loop
                trials.saveAsPickle(filename+'raw_data', fileCollisionMethod='rename')
#                trials.saveAsExcel(filename+'.xlsx', sheetName='rawData_block{0}.'.format(myCount),
#                    #stimOut=params,
#                    dataOut=['all_raw'])
                    #dataOut=['n','all_mean','all_std', 'all_raw'])
                myCount=myCount+1
                trials.finished=True
            
    



#end of loops.. should cycle through t times before entering conclusion
#Initialise components for Routine "conclusion"
conclusionClock=core.Clock()
conclusion_text=visual.TextStim(win=win, ori=0, name='conclusion_text',
    text='Congratulations, you have completed the Mental Rotation task!',
    font='Papyrus',
    pos=[0, 0], height=0.75,wrapWidth=None,
    color='DeepSkyBlue', colorSpace='rgb', opacity=1,
    depth=0.0)
# Create some handy timers

print "Internal thresholding level for {1}= {0}".format(int(average(lastOris)), expInfo['participant ID'])


#------Prepare to start Routine"conclusion"-------
t=0; conclusionClock.reset() #clock 
frameN=-1
routineTimer.add(90.000000)
#update component parameters for each repeat
#keep track of which components have finished
conclusionComponents=[]
conclusionComponents.append(conclusion_text)
for thisComponent in conclusionComponents:
    if hasattr(thisComponent,'status'): thisComponent.status = NOT_STARTED
#-------Start Routine "conclusion"-------
continueRoutine=True
while continueRoutine and routineTimer.getTime()>0:
    #get current time
    t=conclusionClock.getTime()
    frameN=frameN+1#number of completed frames (so 0 in first frame)
    #update/draw components on each frame
    
    #*conclusion_text* updates
    if t>=0.0 and conclusion_text.status==NOT_STARTED:
        #keep track of start time/frame for later
        conclusion_text.tStart=t#underestimates by a little under one frame
        conclusion_text.frameNStart=frameN#exact frame index
        conclusion_text.setAutoDraw(True)
    elif conclusion_text.status==STARTED and t>=(0.0+90.0):
        conclusion_text.setAutoDraw(False)
    
    #check if all components have finished
    if not continueRoutine: #a component has requested that we end
        routineTimer.reset() #this is the new t0 for non-slip Routines
        break
    continueRoutine=False#will revert to True if at least one component still running
    for thisComponent in conclusionComponents:
        if hasattr(thisComponent,"status") and thisComponent.status!=FINISHED:
            continueRoutine=True; break#at least one component has not yet finished
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    #refresh the screen
    if continueRoutine:#don't flip if this routine is over or we'll get a blank screen
        win.flip()
    
#End of Routine "conclusion"
for thisComponent in conclusionComponents:
    if hasattr(thisComponent,"setAutoDraw"): thisComponent.setAutoDraw(False)
    


#Shutting down:
win.close()
core.quit()   