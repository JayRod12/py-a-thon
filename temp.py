# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#press: shift -> start freq (time)
#       1, 0, MHz (s)
#       start freq
#(enter freq)
#       stop freq
#       (enter freq)
#       shift -> auto / manual / single
#
#auto is a smooth, repeating sweep
#manual is a not smooth sweep
#single is a smooth single sweep


import ivi
import visa
import random
import pickle
import numpy as np
from tkinter import *

__author__ = "Blaine Rogers <br1314@ic.ac.uk>"

def getConstantlyDifferentInt():
    """l337 haxx"""
    try:
        with open('temp', 'rb') as file:
            i = pickle.load(file)
    except:
        i = 0
    r = random.randrange(4,11)
    while r == i:
        r = random.randrange(4,11)
    with open('temp', 'wb') as file:
        pickle.dump(r, file)
    return r
    

rm = visa.ResourceManager()
#print(rm.list_resources_info())
print(rm.list_resources())

SIGNAL_GENERATOR_ADDRESS = "GPIB0::19::INSTR"
OSCILLOSCOPE_ADDRESS = "USB0::0x0957::0x1724::MY45003725::INSTR"

signal_generator = ivi.agilent.agilent8642A(SIGNAL_GENERATOR_ADDRESS)
oscilloscope = ivi.agilent.agilentDSO6014A(OSCILLOSCOPE_ADDRESS)

#signal_generator._write("nonsense")
# attempt to clear screen
rm.get_instrument(SIGNAL_GENERATOR_ADDRESS).clear()

print(signal_generator.identity.instrument_model)
#print(signal_generator.rf.frequency)
#print(signal_generator._ask("FROA"))

#i = getConstantlyDifferentInt()
#print("Attempting to set frequency to {}".format(i))
#signal_generator.rf.frequency = i * 1e7
#signal_generator.rf.level = 1
#signal_generator.rf.output_enabled = True

#print(signal_generator.identity.instrument_model)
#print(signal_generator.rf.frequency)
#print(signal_generator._ask("FROA"))



#sweep.configure
#sweep.mode
#sweep.trigger_source
#sweep.frequency_sweep.configure_center_span
#sweep.frequency_sweep.configure_start_stop
signal_generator.rf.level = 1
signal_generator.rf.output_enabled = True
#signal_generator.sweep.frequency_sweep.time = 50000
rm.get_instrument(SIGNAL_GENERATOR_ADDRESS).write("ST 5000 MS")
signal_generator._write("FR 4.0 MZ")
signal_generator.sweep.frequency_sweep.start = 1e2
signal_generator.sweep.frequency_sweep.stop = 1e6
signal_generator.sweep.mode = 1
#sweep.power_sweep.configure_start_stop
#sweep.power_sweep.start
#sweep.power_sweep.stop
#sweep.power_sweep.time

#signal_generator.rf.output_enabled = True

vpp = oscilloscope.channels[0].measurement.fetch_waveform_measurement("voltage_peak_to_peak")
print(vpp)



#signal_generator.lf_generator.waveform = 

#signal_generator.digital_modulation.arb.selected_waveform = 'wfm'
#signal_generator.digital_modulation.arb.clock_frequency = 10e6
#signal_generator.iq.source = 'arb_generator'
#signal_generator.iq.enabled = True
#signal_generator.iq.output_enabled = True

#oscilloscope.configure_center_span(i, 100e3)
#oscilloscope.fetch_screenshot()
