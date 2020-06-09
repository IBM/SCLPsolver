
## 1. Prerequisite: Install Anaconda Python 3.7

1. Go to Anaconda Individual Edition site: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)
2. Download the **64-Bit Graphical Installer**
3. Run downloaded '.exe' file and follow Anaconda installation instructions.

## 2. Optional: Install CPlex

- You can get a free [Community Edition](http://www-01.ibm.com/software/websphere/products/optimization/cplex-studio-community-edition) of CPLEX Optimization Studio, with limited solving capabilities in term of problem size.

- Faculty members, research professionals at accredited institutions can get access to an unlimited version of CPLEX through the [IBM® Academic Initiative](http://www-01.ibm.com/software/websphere/products/optimization/cplex-studio-community-edition).

## 3. Prerequisite: Get code from Github

That is, get this repo.

1. `cd SCLPsolver`

## 4. Prerequisite: Set up an Anaconda environment

An Anaconda environment will allow you to install packages and configure Python for running SCLP. You can activate/deactivate the environment whenever you like, so that the SCLP setup is contained to this project.

1. Optional: create an Anaconda environment `conda create --name SCLP python=3.7`
2. Optional: activate the environment `conda activate SCLP`

## 5. Install Microsoft C++ Build Tools

1. Go to Microsoft C++ Build Tools site: [https://visualstudio.microsoft.com/visual-cpp-build-tools/]( https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Download and install Microsoft C++ Build Tools

## 6. Prerequisite: Install required packages

1. Use conda installer. `conda install --yes --file sclp_requirements.txt`
2. If you want to run the Design of Experiments, and you have CPLEX installed, install the CPLEX installer PIP installer `pip install -r doe/cplex_integration/cplex_requirements.txt`. Note: as of this writing, you cannot use *conda install* for the *doopl* package.

## 7. Compile cython files

_Note: there is now a script for Windows that compiles and runs all of the below steps._

0. `cythonize.bat`

Or do it manually:

1. `cd subroutines/equation_tools`
2. `python setup.py build_ext --inplace`
3. `cd ../lp_tools`
4. `python setup.py build_ext --inplace`
5. `cd ../state_tools`
6. `python setup.py build_ext --inplace`

## 8. Optional: run doe tests

1. `cd tests`
2. Generate random re-entrant line problem and solve it using simplex-type algorithm and CPLEX discretization.
_Note: if you have now CPLEX you should comment lines 66 and 72_  
 `python simple_reentrant_test.py`
3. Generate random MCQN problem and solve it using simplex-type algorithm and CPLEX discretization.
_Note: if you have now CPLEX you should comment lines 76 and 82_  
`python MCQN_test.py`

