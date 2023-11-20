import tdt
from win32com.client import Dispatch
import slab
import numpy as np
import os
from pathlib import Path
path = Path.cwd()

proc = Dispatch('RPco.X')

proc.ConnectRM1('USB', 1)  # connect processor
proc.ClearCOF() # remove previous program from processor
proc.LoadCOF(path / 'random_access_test.rcx')  # load target program

proc.SetTagVal('size', s_samples) # write a single val to a tag
proc.WriteTagV('signal', 0, combined_signal) # specify buffer array using n_samples of sound (inserts data)
#a=proc.ReadTagV('s0', 0, s0.n_samples)
proc.SoftTrg(1)  # buffer trigger (read and play stim)
proc.Run()  # start processor - play sound
proc.Halt()

# specify directory
# data
signals=[] # create empty list for all wav files
# Iterate through files from s_0 to s_7
for i in range(8):
    file_path = os.path.join(dir_path, f's_{i}.wav')
    if os.path.exists(file_path):
        s = slab.Binaural(data=file_path)
        signals.append(s.data[:, 0])

# Combine all signals
combined_signal = np.concatenate(signals)

# get len of combined signal
s_samples = len(combined_signal)

proc.SetTagVal('size', s_samples) # write a single val to a tag
proc.WriteTagV('signal', 0, combined_signal) # specify buffer array using n_samples of sound (inserts data)
#a=proc.ReadTagV('s0', 0, s0.n_samples)
proc.SoftTrg(1)  # buffer trigger (read and play stim)
proc.Run()  # start processor - play sound
proc.Halt()

ild = slab.Binaural.azimuth_to_ild(45) # degrees azimuth
# -9.12  # correct ILD in dB
signal=signal.ild(ild)  # apply the ILD


signal.play()

proc.SetTagVal('isi_in', isi)  # send initial isi to tdt processor

proc.SoftTrg(3)  # pulse train trigger #todo make better buffer loop

proc.SetTagVal('isi', isi)  # write ISI in rcx pulsetrain tag

proc.SoftTrg(2)
proc.Halt()

