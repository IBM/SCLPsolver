
## 1. Prerequisite: Install Anaconda Python 3.7

1. Go to Anaconda Individual Edition site: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)
2. Download the **64-bit command line installer for Python 3.7**
3. `chmod +x Anaconda3-<version>-MacOSX-x86_64.sh`
4. `./Anaconda3-2020.02-MacOSX-x86_64.sh -b -t`
5. `~/anaconda3/bin/conda init`
6. If you are using **zsh** shell, add the following to `.zshrc`:
    
		# >>> conda initialize >>>
		# !! Contents within this block are managed by 'conda init' !!
		__conda_setup="$('/Users/harold/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
		if [ $? -eq 0 ]; then
		    eval "$__conda_setup"
		else
		    if [ -f "/Users/harold/anaconda3/etc/profile.d/conda.sh" ]; then
		        . "/Users/harold/anaconda3/etc/profile.d/conda.sh"
		    else
		        export PATH="/Users/harold/anaconda3/bin:$PATH"
		    fi
		fi
		unset __conda_setup
		# <<< conda initialize <<<

7. Start a new shell

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

## 5. Install XCode command line tools

1. `xcode-select --install`

## 6. Prerequisite: Install required packages

1. Use conda installer. `conda install --yes --file sclp_requirements.txt`
2. Install OpenMP. `conda install -c conda-forge openmp`
3. If you want to run the Design of Experiments, and you have CPlex installed, install the CLEX installer PIP installer `pip install -r doe/cplex_integration/cplex_requirements.txt`. Note: as of this writing, you cannot use *conda install* for the *doopl* package on Mac.

## 7. Compile cython files

_Note: there is now a script for Mac that compiles and runs all of the below steps._

0. `./cythonize.sh`

Or do it manually:

1. `cd subroutines/equation_tools`
2. `python setup.py build_ext --inplace`
3. `cd ../lp_tools`
4. `python setup.py build_ext --inplace`
5. `cd ../state_tools`
6. `python setup.py build_ext --inplace`

## 8. Optional: run doe tests

1. `cd tests`
2. `DYLD_LIBRARY_PATH=/Applications/CPLEX_Studio_Community1210/opl/bin/x86-64_osx PYTHONPATH=.. python test.py`
3. **This test requires access to our Box folder.** `DYLD_LIBRARY_PATH=/Applications/CPLEX_Studio_Community1210/opl/bin/x86-64_osx PYTHONPATH=.. python MCQN_test.py`

