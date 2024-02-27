import sys
import matplotlib.pyplot as plt

sys.path.append("../")
import engcom.data
import engcom.tufte

step_response = engcom.data.step_response(ntime=11, noisy=False)

fig, ax = plt.subplots()
engcom.tufte.plot(ax, step_response[0], step_response[2])
