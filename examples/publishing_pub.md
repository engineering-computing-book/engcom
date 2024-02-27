::: {.cell .markdown lines_to_next_cell="0"}
# Here Is a Top-Level Heading

And here is some text. An equation: $$
x^2 = \int_0^t \Phi(t-\tau) B u(\tau) d\tau.
$$ And whatnot.
:::

::: {.cell .code execution_count="1" execution="{\"shell.execute_reply\":\"2024-02-23T08:30:00.450488Z\",\"iopub.execute_input\":\"2024-02-23T08:30:00.289402Z\",\"iopub.status.idle\":\"2024-02-23T08:30:00.460525Z\",\"iopub.status.busy\":\"2024-02-23T08:30:00.289261Z\"}" lines_to_next_cell="1"}
``` {.python}
import numpy as np
```
:::

::: {.cell .markdown lines_to_next_cell="0"}
# Introduction

This program defines several mathematical functions as vectorized
functions that can handle NumPy array inputs.
:::

::: {.cell .markdown lines_to_next_cell="0"}
# $f(x) = x^2 + 3 x + 9$ {#fx--x2--3-x--9}
:::

::: {.cell .code execution_count="2" execution="{\"shell.execute_reply\":\"2024-02-23T08:30:00.493521Z\",\"iopub.execute_input\":\"2024-02-23T08:30:00.485770Z\",\"iopub.status.idle\":\"2024-02-23T08:30:00.498543Z\",\"iopub.status.busy\":\"2024-02-23T08:30:00.485301Z\"}"}
``` {.python}
def f(x: np.ndarray) -> np.ndarray:
    return x**2 + 3 * x + 9
```
:::

::: {.cell .markdown lines_to_next_cell="0"}
# $g(x) = 1 + \sin^2 x$ {#gx--1--sin2-x}
:::

::: {.cell .code execution_count="3" execution="{\"shell.execute_reply\":\"2024-02-23T08:30:00.512163Z\",\"iopub.execute_input\":\"2024-02-23T08:30:00.508275Z\",\"iopub.status.idle\":\"2024-02-23T08:30:00.513139Z\",\"iopub.status.busy\":\"2024-02-23T08:30:00.507517Z\"}"}
``` {.python}
def g(x: np.ndarray) -> np.ndarray:
    return 1 + np.sin(x) ** 2
```
:::

::: {.cell .markdown lines_to_next_cell="0"}
# $h(x, y) = e^{-3 x} + \ln y$ {#hx-y--e-3-x--ln-y}
:::

::: {.cell .code execution_count="4" execution="{\"shell.execute_reply\":\"2024-02-23T08:30:00.521161Z\",\"iopub.execute_input\":\"2024-02-23T08:30:00.519038Z\",\"iopub.status.idle\":\"2024-02-23T08:30:00.522118Z\",\"iopub.status.busy\":\"2024-02-23T08:30:00.518876Z\"}"}
``` {.python}
def h(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.exp(-3 * x) + np.log(y)
```
:::

::: {.cell .markdown lines_to_next_cell="0"}
# $F(x, y) = \left\lfloor x/y \right\rfloor$ {#fx-y--leftlfloor-xy-rightrfloor}
:::

::: {.cell .code execution_count="5" execution="{\"shell.execute_reply\":\"2024-02-23T08:30:00.529973Z\",\"iopub.execute_input\":\"2024-02-23T08:30:00.526646Z\",\"iopub.status.idle\":\"2024-02-23T08:30:00.530886Z\",\"iopub.status.busy\":\"2024-02-23T08:30:00.526362Z\"}"}
``` {.python}
def F(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.floor(x / y)
```
:::

::: {.cell .markdown lines_to_next_cell="0"}
# $G(x, y) = \begin{cases} x^2 + y^2 & \text{if $x > y$} \\ 2 x & \text{otherwise} \end{cases}$ {#gx-y--begincases-x2--y2--textif-x--y--2-x--textotherwise-endcases}
:::

::: {.cell .code execution_count="6" execution="{\"shell.execute_reply\":\"2024-02-23T08:30:00.537841Z\",\"iopub.execute_input\":\"2024-02-23T08:30:00.535172Z\",\"iopub.status.idle\":\"2024-02-23T08:30:00.538732Z\",\"iopub.status.busy\":\"2024-02-23T08:30:00.534780Z\"}"}
``` {.python}
def G(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    return np.where(x > y, x**2 + y**2, 2 * x)
```
:::

::: {.cell .markdown lines_to_next_cell="0"}
# Call Functions and Print
:::

::: {.cell .code execution_count="7" execution="{\"shell.execute_reply\":\"2024-02-23T08:30:00.549450Z\",\"iopub.execute_input\":\"2024-02-23T08:30:00.544902Z\",\"iopub.status.idle\":\"2024-02-23T08:30:00.550670Z\",\"iopub.status.busy\":\"2024-02-23T08:30:00.544037Z\"}" lines_to_next_cell="2"}
``` {.python}
functions_args = (
    (f, 1),
    (g, 1),
    (h, 2),
    (F, 2),
    (G, 2),
)  # (fun, nargs)
x = np.array([1, 5, 10, 20, 30])
y = np.array([2, 7, 5, 10, 30])
print(f"x = {x}\ny = {y}")

for function_args in functions_args:
    if function_args[1] == 1:
        printable = np.array2string(function_args[0](x), precision=3)
        print(f"{function_args[0].__name__}(x) =", printable)
    elif function_args[1] == 2:
        printable = np.array2string(function_args[0](x, y), precision=3)
        print(f"{function_args[0].__name__}(x, y) =", printable)
```

::: {.output .stream .stdout}
    x = [ 1  5 10 20 30]
    y = [ 2  7  5 10 30]
    f(x) = [ 13  49 139 469 999]
    g(x) = [1.708 1.92  1.296 1.833 1.976]
    h(x, y) = [0.743 1.946 1.609 2.303 3.401]
    F(x, y) = [0. 0. 2. 2. 1.]
    G(x, y) = [  2  10 125 500  60]
:::
:::

::: {.cell .raw tags="[\"active-py\"]"}
```{=ipynb}
import sys

sys.path.append("../")
import engcom

pub = engcom.Publication(title="Problem YE", author="Rico Picone")
pub.write(to="md")
```
:::
