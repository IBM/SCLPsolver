/*********************************************
 * OPL 12.8.0.0 Model
 * Author: evgensh
 * Creation Date: Apr 16, 2019 at 2:13:53 PM
 *********************************************/

execute{
  cplex.lpmethod = 4; // barrier
}
 
float T = ...;
int VarDimension = ...; 
int ConstrDimensionH = ...; 
int ConstrDimensionG = ...; 
int NumIntervals = 5;
//int NumIntervals = ftoi(T/10);
range intervals = 1..NumIntervals;
range intervals0 = 0..NumIntervals;
float tau = T/(NumIntervals);
range cols = 1..VarDimension;
range rowsH = 1..ConstrDimensionH;
range rowsG = 1..ConstrDimensionG;

tuple MATRIX {
  int row;
  int col;
  float value;
}

{MATRIX} G = ...;
{MATRIX} H = ...;
{MATRIX} b = ...;
{MATRIX} a = ...;
{MATRIX} alpha = ...;
{MATRIX} gamma = ...;
{MATRIX} c = ...;

{MATRIX} H_i[r in rowsH] = {H_i | H_i in H : H_i.row == r};
{MATRIX} G_i[r in rowsG] = {G_i | G_i in G : G_i.row == r};
 
 
dvar float+ u[cols][intervals];
dvar float+ x[rowsG][intervals0];

maximize
	 	sum (g in gamma, tt in intervals) 
	 	       tau*g.value*u[g.row][tt]
	 	+
	 	
	 	sum (cc in c, tt in intervals) 
			tau*cc.value*u[cc.row][tt]*(T - tau*(tt + 1/2));
			
			
subject to {
  
//H \cdot u(VarDimension,t) \leq b

forall (i in rowsH, bb in b : bb.row == i, tt in intervals)
	sum (h in H_i[i]) h.value*u[h.col][tt] <= bb.value; 


//int_0^t G u(s) ds + F x(t) ? alpha + a t


forall (i in rowsG, alp in alpha : alp.row == i)
	x[i][0] == alp.value; 	

forall (i in rowsG, aa in a : aa.row == i,  tt in intervals)
	sum (g in G_i[i]) (tau*g.value*u[g.col][tt]) == x[i][tt-1] - x[i][tt] + aa.value*tau; 	


}			 