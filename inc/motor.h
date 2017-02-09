/*
 * motor.h
 *
 *  Created on: Jan 27, 2017
 *      Author: dark
 */

#ifndef MOTOR_H_
#define MOTOR_H_

#define MOTOR_COUNT	4

#define MOTOR_A		0x0
#define MOTOR_B		0x1
#define MOTOR_C		0x2
#define MOTOR_D		0x3

typedef struct motor {
	// PWM (speed)
	__IO uint32_t *duty_cycle;
	char input_consigne_rpm;
	uint32_t consigne_pulse;
	char old_consigne_percent;
	char consigne_percent;
	// Direction
	GPIO_TypeDef *DIRx;
	uint16_t dir_pin1;
	uint16_t dir_pin2;
	// Encoder
	TIM_TypeDef *ENCx;
	volatile int32_t motor_speed_rpm;
	volatile uint32_t old_timestamp;
	volatile uint32_t encoder_cnt;
	volatile uint32_t old_encoder_cnt;
} Motor;

Motor motors[MOTOR_COUNT];

#endif /* MOTOR_H_ */