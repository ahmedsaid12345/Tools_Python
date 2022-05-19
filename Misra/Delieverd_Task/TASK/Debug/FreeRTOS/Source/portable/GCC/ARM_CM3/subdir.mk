################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../FreeRTOS/Source/portable/GCC/ARM_CM3/port.c 

OBJS += \
./FreeRTOS/Source/portable/GCC/ARM_CM3/port.o 

C_DEPS += \
./FreeRTOS/Source/portable/GCC/ARM_CM3/port.d 


# Each subdirectory must supply rules for building sources it contributes
FreeRTOS/Source/portable/GCC/ARM_CM3/%.o: ../FreeRTOS/Source/portable/GCC/ARM_CM3/%.c FreeRTOS/Source/portable/GCC/ARM_CM3/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m3 -std=gnu11 -g3 -DDEBUG -DSTM32 -DSTM32F1 -DSTM32F103C6Tx -c -I../Inc -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/MCAL/inc" -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/FreeRTOS/Source/include" -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/FreeRTOS/Source/portable/GCC/ARM_CM3" -I"C:/Users/m.ali/Desktop/Misra/Delieverd_Task/TASK/HAL/inc" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfloat-abi=soft -mthumb -o "$@"

clean: clean-FreeRTOS-2f-Source-2f-portable-2f-GCC-2f-ARM_CM3

clean-FreeRTOS-2f-Source-2f-portable-2f-GCC-2f-ARM_CM3:
	-$(RM) ./FreeRTOS/Source/portable/GCC/ARM_CM3/port.d ./FreeRTOS/Source/portable/GCC/ARM_CM3/port.o

.PHONY: clean-FreeRTOS-2f-Source-2f-portable-2f-GCC-2f-ARM_CM3

