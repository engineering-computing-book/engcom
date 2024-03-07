# Engcom

A Python package for engineering computing.

## Installation

The package is available from [PyPI](https://pypi.org) and can be installed or updated with

```bash
pip install engcom --upgrade
```

### Installing LaTeX for Publishing PDF Files

To [publish code files](#Publishing-Code) to PDF format, a LaTeX installation is required.
We recommend [TeX Live](https://tug.org/texlive/).

## Basic Usage

### Getting Data Sets

TODO

### Creating Tufte-Style Plots

TODO

### Publishing Code

You can publish your Python scripts (`.py`) and Jupyter notebooks (`.ipynb`) via the `Publication` class.
For scripts, it is best to break your code down into **cells** via the "[percent format](https://jupytext.readthedocs.io/en/latest/formats-scripts.html)" so the output is interleaved with the code.

It can be used from within the file to be published, call it `pub.py` as follows:

```python
# %% This is a code cell
x = 3

# %% [markdown]
# Here is a Markdown cell with some math: $x = 4$.

# %% Another code cell
x**2

# %% [markdown]
## Here Is a Header
# And some regular text.

# %% Another code cell
x**3 + 1

# %% tags=["active-py"]
# This cell will not appear in the output due to its tag
import engcom
pub = engcom.Publication(title="A Title", author="Your Name")
pub.write(to="pdf")
```

This publishes a pdf file `pub.pdf` that appears as follows:

![A published pdf file.](/resources/pub.png)

Alternatively, the last cell could be left off and another file could be used to publish it:

```python
import engcom
pub = engcom.Publication(
    source_filename="pub.py", title="A Title", author="Your Name"
)
pub.write(to="pdf")
```

Finally, a third alternative is to use the `publish` CLI from a terminal window:

```bash
publish pub.py pdf --title "A Title" --author "Your Name"
```

In this example, we have used the `"pdf"` output for publishing.
This requires [LaTeX to be installed](#Installing-LaTeX-for-Publishing-PDF-Files).
Alternatively, `"docx"` could be used to create a Microsoft Word document.
Finally, Markdown `"md"` and LaTeX `"tex"` can be used if you would like to include the published file in another document.

## Troubleshooting

### Error: `pdflatex not found`

```
RuntimeError: Pandoc died with exitcode "47" during conversion: pdflatex not found. Please select a different --pdf-engine or install pdflatex
```

If you haven't yet, make sure [LaTeX is installed](#Installing-LaTeX-for-Publishing-PDF-Files).
If LaTeX is installed, the issue is probably that `pdflatex` is not available in the `PATH` environment variable in your default shell.

If you are using Spyder, the IPython console may not use your default shell `PATH`.

- _Windows_: Add the directory containing `pdflatex` (e.g., `C:\texlive\2023\bin\windows`) to your user `PATH`. Here are [directions for adding an environment variable](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/).
- _Linux/macOS_: Open Spyder, open Preferences > IPython console > Startup and enter the following in the Lines box:
    
```
import os; os.environ['PATH']+=':<directory with pdflatex>'
```
    
On macOS, you can use `/usr/local/bin` and create a symlink there to the `pdflatex` directory (e.g. `ln -s /Library/TeX/texbin/pdflatex /usr/local/bin/`).
To discover the current `PATH` recognized by IPython in Spyder type `!echo $PATH` into the Console.
