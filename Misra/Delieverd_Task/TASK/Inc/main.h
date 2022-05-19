/*
 * main.h
 *
 *      Author: Mahmoud Elkot
 */

#ifndef INC_main_H_
#define  INC_main_H_
#include "STM32F103C6.h"
#include "RCC.h"
#include "USART.h"
#include "FreeRTOS.h"
#include "task.h"
#include "RockBlock.h"
#define TRUE 1
#define FALSE 0
//uint16_t address_1 __attribute__((at(0x20000200)));
//uint16_t gSquared __attribute__((section("try_address")))=10;
 uint16_t address_1 = 10 ;
 uint16_t addre = 2;
uint16_t ch ;
uint16_t String_Data[8];    //Received Data
 xTaskHandle Relay_Task_Handle = NULL;


void Relay_Task(void*params);
void check_system_x(void*params);
uint8_t string_compare(uint16_t* str1, uint16_t* str2);
void GPIO_Init();

#endif /* INC_main_H_ */
