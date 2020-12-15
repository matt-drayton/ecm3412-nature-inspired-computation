# ECM3412 Nature Inspired Computing - Evolutionary Algorithms
This is an implementation of a static-state Evolutionary Algorithm using binary tournaments, weakest replacement, M-gene mutation and single-point crossover to solve the Binpacking Problem. 

## Getting Started
To begin with, it is recommended that you create a virtual Python environment. This is done by entering the command `python -m venv .venv`. 

We then want to activate the environment through the command `.venv\scripts\activate.bat`. 

Finally, we want to fetch the requirements for this project. `pip install -r requirements.txt`.

The `main.py` file will execute a number of trials, printing the batch of results. The notebook, opened using `jupyter notebook notebook.ipynb` will then output the resuts as a LaTeX table. 

The `evolution` module can by used by using `from evolution import evolve_bin_packing_solution`. 
