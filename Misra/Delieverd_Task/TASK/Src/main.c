/**
 ******************************************************************************
 * @file           : main.c
 * @author         : Mahmoud Elkot
 * @brief          : STM32F103C6
 ******************************************************************************
 */

#include "main.h"



/////////////////////////////////////ISR/////////////////////
void  ROCKBLOCK_Call_Back (void) {
 //check from status Flag IF interrupt from TX OR RX.
    if((USART1->SR & ((uint32_t)1 << 7)) != 0)   //check if tx Register is empty.
    {
//do what ever here...when transmit is ended .....

    }
    else{
     static uint8_t i=0;
	MCAL_USART_Receive_Data(USART1, &ch, disable) ;
     if(ch != '\r'){
    	String_Data[i]=ch;   // Store it in array.
    	i++;
     }
     else{

    	// Add  '\0' at the end
    	 String_Data[i]='\0';
    	 i=0;   //Reset Index

    // xTaskNotifyFromISR(Relay_Task_Handle,0x0,eNoAction,3);
    xTaskNotify(Relay_Task_Handle,0x0,eNoAction);


     }
   }


}



int main(void)
{
     ///init_pins//
	GPIO_Init();
      ///init Rock_Block
	HAL_Usart_RockBlock__Init();
	//////////Create Task_Relay///////
	xTaskCreate(Relay_Task, "Relay_Task", configMINIMAL_STACK_SIZE, NULL, 2, &Relay_Task_Handle);
	/////////////////Create System_X_Check_Task/////////
	xTaskCreate(check_system_x, "check_system_x", configMINIMAL_STACK_SIZE, NULL, 2, NULL);

	//
   vTaskStartScheduler();

	while (1) {
		//don't do anything
	//if detect low from this pin Send Alert.

	}

}



void Relay_Task(void*params){

	//Task Notification
	//xTaskNotifyWait(ulBitsToClearOnEntry, ulBitsToClearOnExit, pulNotificationValue, xTicksToWait)
	//xTaskNotifyFromISR()
	//uint16_t* TURNON=(uint16_t*)"TURNON";
	//uint16_t* TURNOFF=(uint16_t*)"TURNOFF";
	uint16_t TURNON []={'T','U','R','N','O','N','\0'};
	uint16_t TURNOFF []={'T','U','R','N','O','F','F','\0'};
	while(1){
	if(xTaskNotifyWait(0, 0, NULL, portMAX_DELAY)==pdTRUE){
      //Compare String In String_Data.


		if(string_compare(String_Data,TURNON ) == TRUE){
   		 //turn on Relay
   		 MCAL_GPIO_WritePin(GPIOB,GPIO_PIN_2, GPIO_PIN_SET);

   	           }

   	  else if(string_compare(String_Data,TURNOFF)== TRUE)
   		 {
   		 //Turn off Relay.
   			 MCAL_GPIO_WritePin(GPIOB,GPIO_PIN_2, GPIO_PIN_RESET);


   		 }
   	  else{

   		  //cause not to violate Misra Rule..
   	  }



	    }
	}

}

/*
 * 		@Fn			   -	check_system_x
 * 		@brief			-	Check if system-x send low signal
 * 		@param[in]		-	None
 * 		@param[out]		-	  None
 * 		@return value		-	None
 * 		Note			-	None
 */

void check_system_x(void* params){

	while(1){
	if(MCAL_GPIO_ReadPin(GPIOB,GPIO_PIN_3) == GPIO_PIN_RESET)  //Detect active low
	{

    HAL_ROCKBLOCK_Send_ALERT();
		vTaskDelay(10);   //  Send Alert Every 10 MS
	  }



	}
}


/*
 * 		@Fn			   -	string_compare
 * 		@brief			-	compare Two String
 * 		@param[in]		-	Two pointer to strings
 * 		@param[out]		-	  none
 * 		@return value		-	1 | 0 to indicate if matched or not.
 * 		Note			-	the String len shouldn't exceed 255 character len.
 */


uint8_t string_compare(uint16_t* str1, uint16_t* str2)
{
    uint8_t ctr=0;

    while(str1[ctr]==str2[ctr])
    {
        if(str1[ctr]==(uint16_t)'\0'||str2[ctr]==(uint16_t)'\0'){
            break;
        }
        ctr++;
    }
    if(str1[ctr]==(uint16_t)'\0' && str2[ctr]==(uint16_t)'\0')
    {
        return 1;
    }
        else
        {
        return 0;

        }
}

/*
 * 		@Fn			   -	GPIO_INIT
 * 		@brief			-	Inilization pins
 * 		@param[in]		-	None
 * 		@param[out]		-	  None
 * 		@return value		-	None
 * 		Note			-	None.
 */

void GPIO_Init(void){
	GPIO_PinConfig_t gpio_PB2;
	gpio_PB2.GPIO_PinNumber = GPIO_PIN_2;
	gpio_PB2.GPIO_MODE = GPIO_MODE_OUTPUT_PUSH_PULL;
	gpio_PB2.GPIO_Output_Speed= GPIO_SPEED_10M;
	MCAL_GPIO_Init(GPIOB, &gpio_PB2);  ///init pin
      //MCAL_GPIO_Init(GPIOx, PinConfig)

	////////input from system x  active low//////////
	GPIO_PinConfig_t gpio_PB3;
	gpio_PB2.GPIO_PinNumber = GPIO_PIN_3;
	gpio_PB2.GPIO_MODE = GPIO_MODE_INPUT_PULL_UP;  //active low
	gpio_PB2.GPIO_Output_Speed= GPIO_SPEED_10M;
	MCAL_GPIO_Init(GPIOB, &gpio_PB3);  ///init pin




}







