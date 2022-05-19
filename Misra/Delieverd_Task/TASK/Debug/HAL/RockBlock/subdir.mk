################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../HAL/RockBlock/RockBlock.c 

OBJS += \
./HAL/RockBlock/RockBlock.o 

C_DEPS += \
./HAL/RockBlock/RockBlock.d 


# Each subdirectory must supply rules for building sources it contributes
HAL/RockBlock/%.o: ../HAL/RockBlock/%.c HAL/RockBlock/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DDEBUG -DSTM32 -DSTM32F1 -DSTM32F103C6Tx -c -I../Inc -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/MCAL/inc" -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/FreeRTOS/Source/include" -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/FreeRTOS/Source/portable/GCC/ARM_CM3" -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/HAL/inc" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"

clean: clean-HAL-2f-RockBlock

clean-HAL-2f-RockBlock:
	-$(RM) ./HAL/RockBlock/RockBlock.d ./HAL/RockBlock/RockBlock.o

.PHONY: clean-HAL-2f-RockBlock

