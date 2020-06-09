cd /D "%~dp0"
cd subroutines/equation_tools
python setup.py build_ext --inplace
cd ../lp_tools
python setup.py build_ext --inplace
cd ../state_tools
python setup.py build_ext --inplace
