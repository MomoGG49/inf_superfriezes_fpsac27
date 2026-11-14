#Latex display in Jupiter notebook for Sage developement
#This is a small function that alow to display latex as an ouput of a cell run in a ipynb in VSCode, since the normal %display latex sage command does not work
#TODO: Why is it that %display latex  it doesn't work?
#Usage: from latex_disp_VSCode import slatex

from sage.misc.latex import latex
from IPython.display import display, Math

def slatex(*args):
    for expr in args:
        display(Math(latex(expr)))
