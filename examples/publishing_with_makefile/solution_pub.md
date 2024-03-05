::: {#6a8a4653 .cell .code execution_count="1" execution="{\"iopub.execute_input\":\"2024-03-05T09:43:02.798582Z\",\"iopub.status.busy\":\"2024-03-05T09:43:02.798492Z\",\"iopub.status.idle\":\"2024-03-05T09:43:03.073698Z\",\"shell.execute_reply\":\"2024-03-05T09:43:03.072387Z\"}"}
``` python
""""Solution to Chapter 3 problem DN"""
import numpy as np
import matplotlib.pyplot as plt
```
:::

::: {#f8e1ac23 .cell .code execution_count="2" execution="{\"iopub.execute_input\":\"2024-03-05T09:43:03.075612Z\",\"iopub.status.busy\":\"2024-03-05T09:43:03.075487Z\",\"iopub.status.idle\":\"2024-03-05T09:43:03.352355Z\",\"shell.execute_reply\":\"2024-03-05T09:43:03.352035Z\"}" tags="[]" transient="{\"remove_source\":true}"}
:::

::: {#7b9bc200 .cell .markdown lines_to_next_cell="0"}
# Introduction

This program defines several mathematical functions as vectorized
functions that can handle NumPy array inputs and plots them over the
given domain using Matplotlib.
:::

::: {#55831adb .cell .markdown lines_to_next_cell="0"}
# Define Mathematical Functions

Define $f(x) = x^2 + 3 x + 9$:
:::

::: {#cbacd0c4 .cell .code execution_count="3" execution="{\"iopub.execute_input\":\"2024-03-05T09:43:03.354306Z\",\"iopub.status.busy\":\"2024-03-05T09:43:03.354141Z\",\"iopub.status.idle\":\"2024-03-05T09:43:03.355945Z\",\"shell.execute_reply\":\"2024-03-05T09:43:03.355701Z\"}"}
``` python
def f(x: np.ndarray) -> np.ndarray:
    return np.tanh(4 * np.sin(x))
```
:::

::: {#cb6d3b38 .cell .markdown lines_to_next_cell="0"}
Define $g(x) = 1 + \sin^2 x$:
:::

::: {#0eefca5f .cell .code execution_count="4" execution="{\"iopub.execute_input\":\"2024-03-05T09:43:03.357214Z\",\"iopub.status.busy\":\"2024-03-05T09:43:03.357141Z\",\"iopub.status.idle\":\"2024-03-05T09:43:03.358714Z\",\"shell.execute_reply\":\"2024-03-05T09:43:03.358505Z\"}"}
``` python
def g(x: np.ndarray) -> np.ndarray:
    return np.sin(np.sqrt(x))
```
:::

::: {#ca89f9cf .cell .markdown lines_to_next_cell="0"}
Define $h(x, y) = e^{-3 x} + \ln y$:
:::

::: {#5b54a4b9 .cell .code execution_count="5" execution="{\"iopub.execute_input\":\"2024-03-05T09:43:03.360036Z\",\"iopub.status.busy\":\"2024-03-05T09:43:03.359969Z\",\"iopub.status.idle\":\"2024-03-05T09:43:03.361859Z\",\"shell.execute_reply\":\"2024-03-05T09:43:03.361540Z\"}"}
``` python
def h(x: np.ndarray) -> np.ndarray:
    return np.where(x >= 0, np.exp(-x) * np.sin(2 * np.pi * x), 0)
```
:::

::: {#2eeddae1 .cell .markdown lines_to_next_cell="0"}
# Plotting

Define a plotting function:
:::

::: {#671f5f46 .cell .code execution_count="6" execution="{\"iopub.execute_input\":\"2024-03-05T09:43:03.363158Z\",\"iopub.status.busy\":\"2024-03-05T09:43:03.363082Z\",\"iopub.status.idle\":\"2024-03-05T09:43:03.364987Z\",\"shell.execute_reply\":\"2024-03-05T09:43:03.364790Z\"}"}
``` python
def plotter(fig, fun, limits, labels):
    x = np.linspace(limits[0], limits[1], 201)
    fig.gca().plot(x, fun(x))
    fig.gca().set_xlabel(labels[0])
    fig.gca().set_ylabel(labels[1])
    return fig
```
:::

::: {#4e8e0782 .cell .markdown}
Plot $f(x)$:
:::

::: {#edbf3ec7 .cell .code execution="{\"iopub.execute_input\":\"2024-03-05T09:43:03.366185Z\",\"iopub.status.busy\":\"2024-03-05T09:43:03.366117Z\",\"iopub.status.idle\":\"2024-03-05T09:43:03.558156Z\",\"shell.execute_reply\":\"2024-03-05T09:43:03.556665Z\"}" tags="[\"remove_output\"]"}
``` python
fig, ax = plt.subplots()
plotter(fig, fun=f, limits=(-5, 8), labels=("$x$", "$f(x)$"))
```
:::

::: {#542468b0 .cell .code execution_count="8" execution="{\"iopub.execute_input\":\"2024-03-05T09:43:03.564084Z\",\"iopub.status.busy\":\"2024-03-05T09:43:03.563782Z\",\"iopub.status.idle\":\"2024-03-05T09:43:05.015504Z\",\"shell.execute_reply\":\"2024-03-05T09:43:05.015183Z\"}" tags="[]" transient="{\"remove_source\":true}"}
::: {.output .execute_result execution_count="8"}
![](examples/publishing_with_makefile/figure-0.pgf){#fig:publishing_with_makefile-figure-0 .figure .pgf}
:::
:::

::: {#3ba10501 .cell .markdown}
Plot $g(x)$:
:::

::: {#29ca0241 .cell .code execution="{\"iopub.execute_input\":\"2024-03-05T09:43:05.017041Z\",\"iopub.status.busy\":\"2024-03-05T09:43:05.016930Z\",\"iopub.status.idle\":\"2024-03-05T09:43:05.216681Z\",\"shell.execute_reply\":\"2024-03-05T09:43:05.201419Z\"}" tags="[\"remove_output\"]"}
``` python
fig, ax = plt.subplots()
plotter(fig, fun=g, limits=(0, 100), labels=("$x$", "$g(x)$"))
```
:::

::: {#f089d350 .cell .code execution_count="10" execution="{\"iopub.execute_input\":\"2024-03-05T09:43:05.225060Z\",\"iopub.status.busy\":\"2024-03-05T09:43:05.224772Z\",\"iopub.status.idle\":\"2024-03-05T09:43:05.292066Z\",\"shell.execute_reply\":\"2024-03-05T09:43:05.291730Z\"}" tags="[]" transient="{\"remove_source\":true}"}
::: {.output .execute_result execution_count="10"}
![](examples/publishing_with_makefile/figure-1.pgf){#fig:publishing_with_makefile-figure-1 .figure .pgf}
:::
:::

::: {#d0c28ed4 .cell .markdown}
Plot $h(x)$:
:::

::: {#1e338fb2 .cell .code execution="{\"iopub.execute_input\":\"2024-03-05T09:43:05.293508Z\",\"iopub.status.busy\":\"2024-03-05T09:43:05.293435Z\",\"iopub.status.idle\":\"2024-03-05T09:43:05.404888Z\",\"shell.execute_reply\":\"2024-03-05T09:43:05.404638Z\"}" tags="[\"remove_output\"]"}
``` python
fig, ax = plt.subplots()
plotter(fig, fun=h, limits=(-2, 6), labels=("$x$", "$h(x)$"))
```
:::

::: {#f1170349 .cell .code execution_count="12" execution="{\"iopub.execute_input\":\"2024-03-05T09:43:05.406303Z\",\"iopub.status.busy\":\"2024-03-05T09:43:05.406223Z\",\"iopub.status.idle\":\"2024-03-05T09:43:05.446471Z\",\"shell.execute_reply\":\"2024-03-05T09:43:05.446220Z\"}" tags="[]" transient="{\"remove_source\":true}"}
::: {.output .execute_result execution_count="12"}
![](examples/publishing_with_makefile/figure-2.pgf){#fig:publishing_with_makefile-figure-2 .figure .pgf}
:::
:::

::: {#00aeaa37 .cell .code execution_count="13" execution="{\"iopub.execute_input\":\"2024-03-05T09:43:05.447844Z\",\"iopub.status.busy\":\"2024-03-05T09:43:05.447770Z\",\"iopub.status.idle\":\"2024-03-05T09:43:05.553944Z\",\"shell.execute_reply\":\"2024-03-05T09:43:05.553640Z\"}"}
``` python
plt.show()
```
:::
