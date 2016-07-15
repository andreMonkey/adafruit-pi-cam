#!/usr/bin/env python
print("""
This example shows how you can monitor an analog input by attaching a function to its changed event.

You should see the analog value being printed out as it changes.

Try connecting up a rotary potentiometer or analog sensor to input one.

""")

from subprocess import call
call(["ls", "-l"])

call(["python", "cam.py"])
call(["python", "pixelsort.py"])

