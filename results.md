# Script parameters and results

## 1. simple_reentrant_test.py

## 1.1. Parameters:
- I (code line 34) - number of servers,
- K (code line 35) - number of buffers,
- settings (code line 36) - various problem generationsettings. Results presented in the paper obtained using exactly same settings
- seed (code line 37) - random seed. Results presented in the paper obtained for seed=1000..1009
- discretization (code line 71) - number of intervals in discretized LP solved by CPLEX

## 1.2. Results:
_Note: results presented below obtained by running code withot changes. Running time can be different_
0. Following output lines contains results of experiment run.
1. Results of the simplex-type algorithm: 
`SCLP objective: 2350061636.3849287 Problem objective: 307164.90704631805 steps: 4370 intervals: 1305
Solution time: 56.9183304309845 seconds
----------------------------------------------`
2. Results of CPLEX:
`ExpName: simple_reentrant_K1200_I60_T1800.0_ccs0_cs10_alpha_rate10.8_alpha_rate20.45_data.dat OBJECTIVE: 690397.8279605354 Time: 6.209460258483887`
3. Results comparison:
`Discretization relative error: 1.247645522398263 discretization relative solution time: 0.10909420939556684`

## 2. MCQN_test.py

## 2.1. Parameters:
- I (code line 39) - number of servers,
- K (code line 40) - number of buffers,
- settings (code line 41) - various problem generationsettings. Results presented in the paper obtained using exactly same settings
- seed (code line 43) - random seed. Results presented in the paper obtained for seed=1000..1009
- discretization (code line 80) - number of intervals in discretized LP solved by CPLEX

## 2.2. Results:
_Note: results presented below obtained by running code withot changes. Running time can be different_
0. Following output lines contains results of experiment run.
1. Results of the simplex-type algorithm: 
`SCLP objective: 168952.9135105581 Problem objective: 2081.27628910591 steps: 9204 intervals: 1377
Solution time: 92.29702806472778 seconds
----------------------------------------------`
2. Results of CPLEX:
`ExpName: MCQN_K1000_I100_T100_alpr1_cs2_ar0.05_sr0.95_nz0.5_gmr0_ccs0_hr0.2_data.dat OBJECTIVE: 3772.5297171969614 Time: 131.77635836601257`
3. Results comparison:
`Discretization relative error: 0.8126039954155209 discretization relative solution time: 1.427742161682584`
