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
int NumIntervals = 1;
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

dvar float+ p[rowsG][intervals];
dvar float+ q0[cols][intervals0];
dvar float+ q1[rowsH][intervals0];

minimize
	 	tau*sum (alp in alpha, tt in intervals)
	 	       alp.value*p[alp.row][tt]
	 	+

	 	tau*sum (aa in a, tt in intervals)
			aa.value*p[aa.row][tt]*(T - tau*(tt - 0.5))

		+

		tau * sum (bb in b, tt in intervals)
		   bb.value * 0.5 * (q1[bb.row][tt]+q1[bb.row][tt-1]);


subject to {

//H \cdot u(VarDimension,t) \leq b

//forall (i in rowsH, bb in b : bb.row == i, tt in intervals)
//	sum (h in H_i[i]) h.value*u[h.col][tt] <= bb.value;


//int_0^t G u(s) ds + F x(t) ? alpha + a t


forall (i in cols)
	sum (h in H_i[i]) (h.value * q1[h.row][0])  == q0[i][0] + sum(gm in gamma : gm.row == i) gm.value;

forall (i in cols, tt in intervals)
	tau * sum (g in G_i[i]) (g.value*p[g.row][tt]) + sum(h in H_i[i]) (h.value * (q1[h.row][tt] - q1[h.row][tt-1]))  == q0[i][tt] - q0[i][tt-1] + tau*sum(cc in c : cc.row == i) cc.value;


}