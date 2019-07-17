# exec(open('Deepanjali data/plot_stepinputcells.py').read())

# Plots all the data one by one
# -100pA to 400pA
# Change

import numpy as np
import quantities as pq
import matplotlib.pyplot as plt
from neo.io import AxonIO
import os
from tkinter.filedialog import askdirectory

Direc = 'Deepanjali data/WT step input cells/' #Directory where all the files are stored
CurrAmp = 10 #0 is for -100pA, 1 for -75pA, and so on till 20 which is 400pA. 10 for 150pA

i = 0
print(os.listdir(Direc))
for filename in os.listdir(Direc):
    i = i+1
    print(i, end = '\r')
    try: #Try is used to skip unsupported files that may be there in the folder
        reader = AxonIO(filename=Direc+filename)
        Samprate = reader.get_signal_sampling_rate()
        seg = reader.read_block().segments[CurrAmp]
        Tdur = np.array(seg.t_stop - seg.t_start)
        plt.plot(np.linspace(0,Tdur,Samprate*Tdur), seg.analogsignals[0], label = f'{filename}')
        plt.legend()
        plt.show()
    except:
        pass
