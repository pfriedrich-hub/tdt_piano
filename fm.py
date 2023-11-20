# after  Schottstaedt, 1977; natural instrument tones

import numpy
import slab
from matplotlib import pyplot as plt
fs = 48828
t = numpy.arange(0, 1, 1/fs)  # time points

# carrier
fc = 1
# amplitude over time
A = 1  # base amp
# Alin = 10 ** (A / 10)  #todo convert to linear scale
AdB = A * 75  # arbitrary dB amplitude to calculate decay time
T = 10 * numpy.sqrt(AdB) / numpy.sqrt(fc)  # decay time
At = numpy.exp(-t * 5/T)  # decay envelope
# At = numpy.e ** (-t)  # same thing
# plt.plot(t, At)

# yc = A * numpy.sin(2 * numpy.pi * fc * t)  # carrier (tone)
# slab.Sound(yc, samplerate=fs).waveform()

# modulating sines
fm1 = fc
fm2 = fc * 4
S = fc / 200  # ymod spectrum is less clean but still sounds fine
# modulation indices (amplitudes of the components)
I1 = 17 * (8 - numpy.log(fc)) / (numpy.log(fc) ** 2)
I2 = 20 * (8 - numpy.log(fc)) / fc
ym1 = I1 * numpy.sin(2 * numpy.pi * (fm1 + S) * t)
ym2 = I2 * numpy.sin(2 * numpy.pi * (fm2 + S) * t)
# ym1 = I1 * numpy.sin(2 * numpy.pi * (fm1) * t)
# ym2 = I2 * numpy.sin(2 * numpy.pi * (fm2) * t)
ymod = A * numpy.sin(2 * numpy.pi * fc * t + ym1 + ym2)  # frequency modulated tone
ymod = ymod * At  # add decay ramp

tone = slab.Sound(ymod, samplerate=fs)
# tone.play()
# tone.waveform()
# tone.spectrum()

