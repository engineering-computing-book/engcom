import sys
import matplotlib.pyplot as plt

sys.path.append("../")
import engcom.data

step_response = engcom.data.step_response(ntime=201)

fig, ax = plt.subplots()
ax.plot(step_response[0], step_response[1])
ax.plot(step_response[0], step_response[2])
