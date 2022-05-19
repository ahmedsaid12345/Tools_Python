/*
 * RockBlock.h
 *
 *      Author: Mahmoud Elkot
 */

#ifndef INC_ROCKBLOCK_H_
#define  INC_ROCKBLOCK_H_
#include "STM32F103C6.h"
#include "RCC.h"
#include "GPIO.h"
#include "USART.h"



///--------------------API-------------------
//void HAL_Usart_RockBlock_Init(void);
void HAL_Usart_RockBlock__Init(void);
void HAL_Usart_RockBlock__DeInit(void);
void HAL_ROCKBLOCK_Send_ALERT(void);





//----------------ISR API-------------------------------------
extern void  ROCKBLOCK_Call_Back(void);


#endif /* INC_ROCKBLOCK_H_ */
