/*********************************************
 * OPL 12.8.0.0 Model
 * Author: evgensh
 * Creation Date: Apr 16, 2019 at 2:13:53 PM
 *********************************************/

execute{
  cplex.lpmethod = 4;
}

float T = ...;
int VarDimension = ...; 
int ConstrDimensionH = ...; 
int ConstrDimensionG = ...; 
//int NumIntervals = ftoi(T/10);
int NumIntervals = 10;
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

{MATRIX} H_i[r in cols] = {H_i | H_i in H : H_i.col == r};
{MATRIX} G_i[r in cols] = {G_i | G_i in G : G_i.col == r};

{int} nz_gamma = {gm.row | gm in gamma};


dvar float+ p[rowsG][intervals];
dvar float+ q0[cols][intervals0];
dvar float+ q1[rowsH][intervals0];

minimize
	 	sum (alp in alpha, tt in intervals)
	 	       tau*alp.value*p[alp.row][tt]
	 	+

	 	sum (aa in a, tt in intervals)
			tau*aa.value*p[aa.row][tt]*(T - tau*(tt - 0.5))

		+

		sum (bb in b, tt in intervals)
		   tau * bb.value * 0.5 * (q1[bb.row][tt]+q1[bb.row][tt-1]);


subject to {

//H \cdot u(VarDimension,t) \leq b

//forall (i in rowsH, bb in b : bb.row == i, tt in intervals)
//	sum (h in H_i[i]) h.value*u[h.col][tt] <= bb.value;


//int_0^t G u(s) ds + F x(t) ? alpha + a t


forall (i in cols, gm in gamma : gm.row == i)
	sum (h in H_i[i]) (h.value * q1[h.row][0])  == q0[i][0] + gm.value;

forall (i in cols: i not in nz_gamma)
	sum (h in H_i[i]) (h.value * q1[h.row][0])  == q0[i][0];

forall (i in cols, cc in c : cc.row == i,  tt in intervals)
	sum (g in G_i[i]) (tau*g.value*p[g.row][tt])  == q0[i][tt] - q0[i][tt-1] + cc.value*tau - sum(h in H_i[i]) (h.value * (q1[h.row][tt] - q1[h.row][tt-1]));


}