psychoPy_experiments
====================

psychology/neuroscience experiments in PsychoPy stimulus presentation software

NOTE: In Psychopy v. 1.77.00, 1.77.01, and 1.77.02, there is a small bug in rendering of certain jpg files.
It will be fixed in the next bug release, but if you want to fix this yourself first, go to visual.py and change the line (around 7430) that says:
if im.mode=='L':
to read:
if im.mode=='L' and pixFormat==GL.GL_ALPHA:
