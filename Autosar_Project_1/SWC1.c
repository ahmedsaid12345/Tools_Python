#include "RTE_SWC1.h"

void SUM(){
	
	Std_ReturnType status= E_NOT_OK;
	unsigned short x,y;
	unsigned int z=0;
	status = RTE_Read_RP_Sum_Var_1(&x);
	status = RTE_Read_RP_Sum_Var_2(&y);
	z=x+y;
	status = RTE_write_PP_SUM_SUM_Result(z);

}