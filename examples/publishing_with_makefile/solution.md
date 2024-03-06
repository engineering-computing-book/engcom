::: {#0ce6a79f .cell .code execution_count="1" execution="{\"iopub.execute_input\":\"2024-03-06T22:36:45.095488Z\",\"iopub.status.busy\":\"2024-03-06T22:36:45.095346Z\",\"iopub.status.idle\":\"2024-03-06T22:36:45.518795Z\",\"shell.execute_reply\":\"2024-03-06T22:36:45.518503Z\"}"}
``` python
""""Solution to Chapter 3 problem DN"""
import numpy as np
import matplotlib.pyplot as plt
```
:::

::: {#de35006b .cell .code execution_count="2" execution="{\"iopub.execute_input\":\"2024-03-06T22:36:45.520793Z\",\"iopub.status.busy\":\"2024-03-06T22:36:45.520533Z\",\"iopub.status.idle\":\"2024-03-06T22:36:45.814061Z\",\"shell.execute_reply\":\"2024-03-06T22:36:45.813523Z\"}" tags="[]" transient="{\"remove_source\":true}"}
:::

::: {#765eae73 .cell .markdown lines_to_next_cell="0"}
# Introduction

This program defines several mathematical functions as vectorized
functions that can handle NumPy array inputs and plots them over the
given domain using Matplotlib.
:::

::: {#862d25cb .cell .markdown lines_to_next_cell="0"}
# Define Mathematical Functions

Define $f(x) = x^2 + 3 x + 9$:
:::

::: {#49424bbb .cell .code execution_count="3" execution="{\"iopub.execute_input\":\"2024-03-06T22:36:45.817438Z\",\"iopub.status.busy\":\"2024-03-06T22:36:45.817227Z\",\"iopub.status.idle\":\"2024-03-06T22:36:45.819342Z\",\"shell.execute_reply\":\"2024-03-06T22:36:45.819034Z\"}"}
``` python
def f(x: np.ndarray) -> np.ndarray:
    return np.tanh(4 * np.sin(x))
```
:::

::: {#d2e03871 .cell .markdown lines_to_next_cell="0"}
Define $g(x) = 1 + \sin^2 x$:
:::

::: {#5a8ebf47 .cell .code execution_count="4" execution="{\"iopub.execute_input\":\"2024-03-06T22:36:45.820855Z\",\"iopub.status.busy\":\"2024-03-06T22:36:45.820753Z\",\"iopub.status.idle\":\"2024-03-06T22:36:45.822657Z\",\"shell.execute_reply\":\"2024-03-06T22:36:45.822288Z\"}"}
``` python
def g(x: np.ndarray) -> np.ndarray:
    return np.sin(np.sqrt(x))
```
:::

::: {#5f284289 .cell .markdown lines_to_next_cell="0"}
Define $h(x, y) = e^{-3 x} + \ln y$:
:::

::: {#a1622d9d .cell .code execution_count="5" execution="{\"iopub.execute_input\":\"2024-03-06T22:36:45.824277Z\",\"iopub.status.busy\":\"2024-03-06T22:36:45.824146Z\",\"iopub.status.idle\":\"2024-03-06T22:36:45.826100Z\",\"shell.execute_reply\":\"2024-03-06T22:36:45.825815Z\"}"}
``` python
def h(x: np.ndarray) -> np.ndarray:
    return np.where(x >= 0, np.exp(-x) * np.sin(2 * np.pi * x), 0)
```
:::

::: {#083611e0 .cell .markdown lines_to_next_cell="0"}
# Plotting

Define a plotting function:
:::

::: {#e7125d45 .cell .code execution_count="6" execution="{\"iopub.execute_input\":\"2024-03-06T22:36:45.827605Z\",\"iopub.status.busy\":\"2024-03-06T22:36:45.827496Z\",\"iopub.status.idle\":\"2024-03-06T22:36:45.829573Z\",\"shell.execute_reply\":\"2024-03-06T22:36:45.829275Z\"}"}
``` python
def plotter(fig, fun, limits, labels):
    x = np.linspace(limits[0], limits[1], 201)
    fig.gca().plot(x, fun(x))
    fig.gca().set_xlabel(labels[0])
    fig.gca().set_ylabel(labels[1])
    return fig
```
:::

::: {#949191d6 .cell .markdown}
Plot $f(x)$:
:::

::: {#0faf190c .cell .code execution="{\"iopub.execute_input\":\"2024-03-06T22:36:45.831298Z\",\"iopub.status.busy\":\"2024-03-06T22:36:45.831190Z\",\"iopub.status.idle\":\"2024-03-06T22:36:46.111535Z\",\"shell.execute_reply\":\"2024-03-06T22:36:46.111221Z\"}" tags="[\"remove_output\"]"}
``` python
fig, ax = plt.subplots()
plotter(fig, fun=f, limits=(-5, 8), labels=("$x$", "$f(x)$"))
```
:::

::: {#ae468724 .cell .code execution_count="8" execution="{\"iopub.execute_input\":\"2024-03-06T22:36:46.113168Z\",\"iopub.status.busy\":\"2024-03-06T22:36:46.113040Z\",\"iopub.status.idle\":\"2024-03-06T22:36:47.647397Z\",\"shell.execute_reply\":\"2024-03-06T22:36:47.647002Z\"}" tags="[]" transient="{\"remove_source\":true}"}
::: {.output .execute_result execution_count="8"}
![](examples/publishing_with_makefile/figure-0.pgf){#fig:publishing_with_makefile-figure-0 .figure .pgf}
:::
:::

::: {#29855387 .cell .markdown}
Plot $g(x)$:
:::

::: {#da01184d .cell .code execution="{\"iopub.execute_input\":\"2024-03-06T22:36:47.649087Z\",\"iopub.status.busy\":\"2024-03-06T22:36:47.648967Z\",\"iopub.status.idle\":\"2024-03-06T22:36:47.803923Z\",\"shell.execute_reply\":\"2024-03-06T22:36:47.801341Z\"}" tags="[\"remove_output\"]"}
``` python
fig, ax = plt.subplots()
plotter(fig, fun=g, limits=(0, 100), labels=("$x$", "$g(x)$"))
```
:::

::: {#2a37072d .cell .code execution_count="10" execution="{\"iopub.execute_input\":\"2024-03-06T22:36:47.813453Z\",\"iopub.status.busy\":\"2024-03-06T22:36:47.812736Z\",\"iopub.status.idle\":\"2024-03-06T22:36:47.861029Z\",\"shell.execute_reply\":\"2024-03-06T22:36:47.855645Z\"}" tags="[]" transient="{\"remove_source\":true}"}
::: {.output .execute_result execution_count="10"}
![](examples/publishing_with_makefile/figure-1.pgf){#fig:publishing_with_makefile-figure-1 .figure .pgf}
:::
:::

::: {#d72ac30c .cell .markdown}
Plot $h(x)$:
:::

::: {#0b18902e .cell .code execution="{\"iopub.execute_input\":\"2024-03-06T22:36:47.867097Z\",\"iopub.status.busy\":\"2024-03-06T22:36:47.866916Z\",\"iopub.status.idle\":\"2024-03-06T22:36:47.993945Z\",\"shell.execute_reply\":\"2024-03-06T22:36:47.993670Z\"}" tags="[\"remove_output\"]"}
``` python
fig, ax = plt.subplots()
plotter(fig, fun=h, limits=(-2, 6), labels=("$x$", "$h(x)$"))
```
:::

::: {#ee525fa3 .cell .code execution_count="12" execution="{\"iopub.execute_input\":\"2024-03-06T22:36:47.995328Z\",\"iopub.status.busy\":\"2024-03-06T22:36:47.995222Z\",\"iopub.status.idle\":\"2024-03-06T22:36:48.037165Z\",\"shell.execute_reply\":\"2024-03-06T22:36:48.036902Z\"}" tags="[]" transient="{\"remove_source\":true}"}
::: {.output .execute_result execution_count="12"}
![](examples/publishing_with_makefile/figure-2.pgf){#fig:publishing_with_makefile-figure-2 .figure .pgf}
:::
:::

::: {#4c29f712 .cell .code execution_count="13" execution="{\"iopub.execute_input\":\"2024-03-06T22:36:48.038735Z\",\"iopub.status.busy\":\"2024-03-06T22:36:48.038652Z\",\"iopub.status.idle\":\"2024-03-06T22:36:48.150579Z\",\"shell.execute_reply\":\"2024-03-06T22:36:48.150271Z\"}"}
``` python
plt.show()
```
:::
