/*
 * USART.c
 *
 *      Author: Mahmoud Elkot
 */
#include "RockBlock.h"


//-------------------------------------ROCK_BLOCK API-------------------------------
/*
 * 		@Fn			-	    Usart_RockBlock_Init
 * 		@brief			-	Initialize RoclBlock module
 * 		@param[in]		-	void
 *
 * 		@param[out]		-	none
 * 		@return value		-	none
 * 		Note			-
 */
void HAL_Usart_RockBlock__Init(void) {
	    USART_Config_t uart1_cfg ;
		uart1_cfg.Mode = USART_MODE_TX_RX ;
		uart1_cfg.BaudRate = USART_BAUDRATE_9600 ;
		uart1_cfg.PayLoad_Length = USART_PAYLOAD_8B ;
		uart1_cfg.Parity = USART_PARITY_NONE ;
		uart1_cfg.StopBits = USART_STOP_BITS_1 ;
		uart1_cfg.HW_FlowControl = USART_FLOWCONTROL_NONE ;
		uart1_cfg.IRQ_Enable = USART_IRQ_ENABLE_RXNE ;
		uart1_cfg.p_IRQ_CallBack = ROCKBLOCK_Call_Back ;

		MCAL_USART_Init(USART1, &uart1_cfg) ;
		MCAL_USART_GPIO_Pins(USART1) ;
}

/*
 * 		@Fn			-	HAL_Usart_RockBlock__DeInit
 * 		@brief			-	Reset Connection
 * 		@param[in]		-	void
 * 		@param[out]		-	none
 * 		@return value		-	none
 * 		Note			-	none
 */

void HAL_Usart_RockBlock__DeInit(void) {
	MCAL_USART_DeInit(USART1);
}


/*
 * 		@Fn			-	HAL_ROCKBLOCK_Send_ALERT
 * 		@brief			-	Send Alert String to RockBlock
 * 		@param[in]		-	void
 * 		@param[out]		-	none
 * 		@return value		-	none
 * 		Note			-	none
 */

void HAL_ROCKBLOCK_Send_ALERT(void){

	uint16_t p_p[6] = {'A','L','E','R','T','\0'};
       uint8_t i=0;
	while(p_p[i] != (uint16_t)'\0'){
		MCAL_USART_Send_Data(USART1 ,&p_p[i]  ,enable);
		i++;
	}


}












