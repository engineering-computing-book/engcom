import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("../")
import engcom.data

d = engcom.data.movie_ratings_binned()
x = list(range(0,len(d["rating_freq"])))

fig, ax = plt.subplots()
ax.bar(x, d["rating_freq"], color="dodgerblue")
ax.set_xticks(x)
ax.set_xticklabels(d["labels"])
ax.set_xlabel("Rating out of $10$")
ax.set_ylabel("Frequency")
plt.show()