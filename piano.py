import tdt
from win32com.client import Dispatch
import slab
import numpy
import os
from pathlib import Path
from matplotlib import pyplot as plt
path = Path.cwd()
# fs = 48828
fs = 24414
proc = Dispatch('RPco.X')
proc.ConnectRM1('USB', 1)  # connect processor
proc.ClearCOF() # remove previous program from processor
proc.LoadCOF(path / 'piano.rcx')  # load target program
proc.SetTagVal('f0', 220)  # write a single val to a tag
proc.Run()  # start processor - play sound

duration = 1
n_samples = duration * fs
t = numpy.linspace(0, duration, n_samples)

data = numpy.array(proc.ReadTagV('Data', 0, n_samples))
plt.figure()
plt.plot(t, data)
tone = slab.Sound(data, samplerate=fs)
tone.spectrum()
tone.waveform()

# data1 = numpy.array(proc.ReadTagV('Data1', 0, n_samples))
# plt.figure()
# plt.plot(t, data1)
# tone1 = slab.Sound(data1, samplerate=fs)
# tone1.spectrum()


proc.Halt()

