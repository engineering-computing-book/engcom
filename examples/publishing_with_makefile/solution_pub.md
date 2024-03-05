::: {#026d8899 .cell .code execution_count="1" execution="{\"iopub.execute_input\":\"2024-03-05T09:31:18.077768Z\",\"iopub.status.busy\":\"2024-03-05T09:31:18.077566Z\",\"iopub.status.idle\":\"2024-03-05T09:31:18.358350Z\",\"shell.execute_reply\":\"2024-03-05T09:31:18.351054Z\"}"}
``` python
""""Solution to Chapter 3 problem DN"""
import numpy as np
import matplotlib.pyplot as plt
```
:::

::: {#ce12d62f .cell .code execution_count="2" execution="{\"iopub.execute_input\":\"2024-03-05T09:31:18.360443Z\",\"iopub.status.busy\":\"2024-03-05T09:31:18.360251Z\",\"iopub.status.idle\":\"2024-03-05T09:31:18.662521Z\",\"shell.execute_reply\":\"2024-03-05T09:31:18.662231Z\"}" tags="[\"remove_input\"]" transient="{\"remove_source\":true}"}
:::

::: {#6cb294b1 .cell .markdown lines_to_next_cell="0"}
# Introduction

This program defines several mathematical functions as vectorized
functions that can handle NumPy array inputs and plots them over the
given domain using Matplotlib.
:::

::: {#643d814d .cell .markdown lines_to_next_cell="0"}
# Define Mathematical Functions

Define $f(x) = x^2 + 3 x + 9$:
:::

::: {#f2fdeb24 .cell .code execution_count="3" execution="{\"iopub.execute_input\":\"2024-03-05T09:31:18.664419Z\",\"iopub.status.busy\":\"2024-03-05T09:31:18.664227Z\",\"iopub.status.idle\":\"2024-03-05T09:31:18.666156Z\",\"shell.execute_reply\":\"2024-03-05T09:31:18.665920Z\"}"}
``` python
def f(x: np.ndarray) -> np.ndarray:
    return np.tanh(4 * np.sin(x))
```
:::

::: {#8a6ff470 .cell .markdown lines_to_next_cell="0"}
Define $g(x) = 1 + \sin^2 x$:
:::

::: {#f430c017 .cell .code execution_count="4" execution="{\"iopub.execute_input\":\"2024-03-05T09:31:18.667722Z\",\"iopub.status.busy\":\"2024-03-05T09:31:18.667601Z\",\"iopub.status.idle\":\"2024-03-05T09:31:18.669201Z\",\"shell.execute_reply\":\"2024-03-05T09:31:18.668958Z\"}"}
``` python
def g(x: np.ndarray) -> np.ndarray:
    return np.sin(np.sqrt(x))
```
:::

::: {#21201cf7 .cell .markdown lines_to_next_cell="0"}
Define $h(x, y) = e^{-3 x} + \ln y$:
:::

::: {#1365225f .cell .code execution_count="5" execution="{\"iopub.execute_input\":\"2024-03-05T09:31:18.670506Z\",\"iopub.status.busy\":\"2024-03-05T09:31:18.670418Z\",\"iopub.status.idle\":\"2024-03-05T09:31:18.672201Z\",\"shell.execute_reply\":\"2024-03-05T09:31:18.671987Z\"}"}
``` python
def h(x: np.ndarray) -> np.ndarray:
    return np.where(x >= 0, np.exp(-x) * np.sin(2 * np.pi * x), 0)
```
:::

::: {#3a5ebb47 .cell .markdown lines_to_next_cell="0"}
# Plotting

Define a plotting function:
:::

::: {#b08028b3 .cell .code execution_count="6" execution="{\"iopub.execute_input\":\"2024-03-05T09:31:18.673432Z\",\"iopub.status.busy\":\"2024-03-05T09:31:18.673360Z\",\"iopub.status.idle\":\"2024-03-05T09:31:18.675222Z\",\"shell.execute_reply\":\"2024-03-05T09:31:18.675010Z\"}"}
``` python
def plotter(fig, fun, limits, labels):
    x = np.linspace(limits[0], limits[1], 201)
    fig.gca().plot(x, fun(x))
    fig.gca().set_xlabel(labels[0])
    fig.gca().set_ylabel(labels[1])
    return fig
```
:::

::: {#1f0e8a71 .cell .markdown}
Plot $f(x)$:
:::

::: {#a43a7b8e .cell .code execution="{\"iopub.execute_input\":\"2024-03-05T09:31:18.676538Z\",\"iopub.status.busy\":\"2024-03-05T09:31:18.676464Z\",\"iopub.status.idle\":\"2024-03-05T09:31:18.980847Z\",\"shell.execute_reply\":\"2024-03-05T09:31:18.980585Z\"}" tags="[\"remove_output\"]"}
``` python
fig, ax = plt.subplots()
plotter(fig, fun=f, limits=(-5, 8), labels=("$x$", "$f(x)$"))
```
:::

::: {#3f7f1c33 .cell .code execution_count="8" execution="{\"iopub.execute_input\":\"2024-03-05T09:31:18.982371Z\",\"iopub.status.busy\":\"2024-03-05T09:31:18.982261Z\",\"iopub.status.idle\":\"2024-03-05T09:31:20.676394Z\",\"shell.execute_reply\":\"2024-03-05T09:31:20.676057Z\"}" tags="[\"remove_input\"]" transient="{\"remove_source\":true}"}
::: {.output .execute_result execution_count="8"}
![](examples/publishing_with_makefile/figure-0.pgf){#fig:publishing_with_makefile-figure-0 .figure .pgf}
:::
:::

::: {#4f12fdb0 .cell .markdown}
Plot $g(x)$:
:::

::: {#aa803749 .cell .code execution="{\"iopub.execute_input\":\"2024-03-05T09:31:20.678143Z\",\"iopub.status.busy\":\"2024-03-05T09:31:20.678023Z\",\"iopub.status.idle\":\"2024-03-05T09:31:20.929463Z\",\"shell.execute_reply\":\"2024-03-05T09:31:20.928405Z\"}" tags="[\"remove_output\"]"}
``` python
fig, ax = plt.subplots()
plotter(fig, fun=g, limits=(0, 100), labels=("$x$", "$g(x)$"))
```
:::

::: {#2be57f03 .cell .code execution_count="10" execution="{\"iopub.execute_input\":\"2024-03-05T09:31:20.936070Z\",\"iopub.status.busy\":\"2024-03-05T09:31:20.934997Z\",\"iopub.status.idle\":\"2024-03-05T09:31:20.981277Z\",\"shell.execute_reply\":\"2024-03-05T09:31:20.980999Z\"}" tags="[\"remove_input\"]" transient="{\"remove_source\":true}"}
::: {.output .execute_result execution_count="10"}
![](examples/publishing_with_makefile/figure-1.pgf){#fig:publishing_with_makefile-figure-1 .figure .pgf}
:::
:::

::: {#c9a40f0b .cell .markdown}
Plot $h(x)$:
:::

::: {#fd1feeb6 .cell .code execution="{\"iopub.execute_input\":\"2024-03-05T09:31:20.982584Z\",\"iopub.status.busy\":\"2024-03-05T09:31:20.982507Z\",\"iopub.status.idle\":\"2024-03-05T09:31:21.061479Z\",\"shell.execute_reply\":\"2024-03-05T09:31:21.061218Z\"}" tags="[\"remove_output\"]"}
``` python
fig, ax = plt.subplots()
plotter(fig, fun=h, limits=(-2, 6), labels=("$x$", "$h(x)$"))
```
:::

::: {#abc96e5f .cell .code execution_count="12" execution="{\"iopub.execute_input\":\"2024-03-05T09:31:21.063003Z\",\"iopub.status.busy\":\"2024-03-05T09:31:21.062820Z\",\"iopub.status.idle\":\"2024-03-05T09:31:21.103119Z\",\"shell.execute_reply\":\"2024-03-05T09:31:21.102868Z\"}" tags="[\"remove_input\"]" transient="{\"remove_source\":true}"}
::: {.output .execute_result execution_count="12"}
![](examples/publishing_with_makefile/figure-2.pgf){#fig:publishing_with_makefile-figure-2 .figure .pgf}
:::
:::

::: {#5eb363b1 .cell .code execution_count="13" execution="{\"iopub.execute_input\":\"2024-03-05T09:31:21.104528Z\",\"iopub.status.busy\":\"2024-03-05T09:31:21.104450Z\",\"iopub.status.idle\":\"2024-03-05T09:31:21.213947Z\",\"shell.execute_reply\":\"2024-03-05T09:31:21.213679Z\"}"}
``` python
plt.show()
```
:::
