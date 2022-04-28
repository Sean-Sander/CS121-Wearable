# CS121-Wearable

## Project Goal
I wanted to design a device, for my open-ended project for my CS121 course, that would have practical use in the real world. This device would be an implementation 
of wearable, open-source technology that would allow individuals to use their own hardware. The implementation I made was that of a glove with flex sensors, a gyro, 
an accelerometer, and some buttons. The software was initially designed to be separate of the device in logic. This would allow, in concept, someone to make their 
own device that may fit their ergonomic needs, and use the software to make custom bindings.

### What there is and isn't
There is an IR sensor and emitter on the wrist of the glove, to use as an example of binding inputs to outputs. The user can train the device to blast an IR signal 
of whatever was inputted to the IR sensor, in reaction to a supplied gesture. Gesture files are saved in JSON forms, with the name indicating finger state. The file 
included in the repo, FFFFF.json is the action that will be fired when all five fingers are flexed. 

Due to technical and software limitations, the finer details of the gyro/accel combo weren't used to full ability. This was left to expand on in the future, 
where machine learning would be a great fit to combine the gesture recognition through movement along with the finger position recognition that is currently in place.

As the device is currently only geared for IR, there isn't USB capability. In the original design spec, it was desired for the device to also work as a macro input device 
that would work similar to a keyboard on a traditional PC. Trained gestures could do things such as opening an Outlook window on Windows - things that a user 
possibly without full use of all 10 digits on their hands would find use of.

The repo currently is a direct rip of the folder stored on the Raspberry Pi, there may need to be some formatting done to tidy loose ends on this remote version.
