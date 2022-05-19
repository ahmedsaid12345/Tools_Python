################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../MCAL/USART/USART.c 

OBJS += \
./MCAL/USART/USART.o 

C_DEPS += \
./MCAL/USART/USART.d 


# Each subdirectory must supply rules for building sources it contributes
MCAL/USART/%.o: ../MCAL/USART/%.c MCAL/USART/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DDEBUG -DSTM32 -DSTM32F1 -DSTM32F103C6Tx -c -I../Inc -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/MCAL/inc" -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/FreeRTOS/Source/include" -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/FreeRTOS/Source/portable/GCC/ARM_CM3" -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/HAL/inc" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"

clean: clean-MCAL-2f-USART

clean-MCAL-2f-USART:
	-$(RM) ./MCAL/USART/USART.d ./MCAL/USART/USART.o

.PHONY: clean-MCAL-2f-USART

