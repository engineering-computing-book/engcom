::: {.cell .code execution_count="1" execution="{\"shell.execute_reply\":\"2024-03-02T09:23:14.404309Z\",\"iopub.execute_input\":\"2024-03-02T09:23:13.833376Z\",\"iopub.status.idle\":\"2024-03-02T09:23:14.404688Z\",\"iopub.status.busy\":\"2024-03-02T09:23:13.833298Z\"}"}
``` {.python}
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("../")
import engcom.data
```

::: {.output .stream .stderr}
    /Users/ricopicone/anaconda3/envs/systems/lib/python3.12/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
      from .autonotebook import tqdm as notebook_tqdm
:::
:::

::: {.cell .code execution_count="2" execution="{\"shell.execute_reply\":\"2024-03-02T09:23:14.407813Z\",\"iopub.execute_input\":\"2024-03-02T09:23:14.406322Z\",\"iopub.status.idle\":\"2024-03-02T09:23:14.408094Z\",\"iopub.status.busy\":\"2024-03-02T09:23:14.406165Z\"}"}
``` {.python}
d = engcom.data.movie_ratings_binned()
x = list(range(0,len(d["rating_freq"])))
```
:::

::: {.cell .code execution_count="3" execution="{\"shell.execute_reply\":\"2024-03-02T09:23:14.568848Z\",\"iopub.execute_input\":\"2024-03-02T09:23:14.409497Z\",\"iopub.status.idle\":\"2024-03-02T09:23:14.570027Z\",\"iopub.status.busy\":\"2024-03-02T09:23:14.409385Z\"}"}
``` {.python}
fig, ax = plt.subplots()
ax.bar(x, d["rating_freq"], color="dodgerblue")
ax.set_xticks(x)
ax.set_xticklabels(d["labels"])
ax.set_xlabel("Rating out of $10$")
ax.set_ylabel("Frequency")
plt.show()
```

::: {.output .display_data}
![](4238ca954018207934149ab08effb8fb4ce4294b.png)
:::
:::
