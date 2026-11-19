
# DC Motor Simulation Using Python

## 1. Project Overview

This project presents a simple mathematical modeling
and simulation of a DC motor using Python.

The objective is to study the motor speed response
when a unit step input is applied.

## 2. Mathematical Model

The first-order system is represented by:

ω(t) = K × u × (1 - exp(-t/τ))

Where:

- K = 0.1 : Motor gain
- τ = 0.5 s : Time constant
- u = 1 : Unit step input
- ω(t) : Angular speed

## 3. Tools and Technologies

- Python
- NumPy
- Matplotlib

## 4. Simulation

The simulation calculates the motor speed
over a period of 5 seconds.

## 5. Expected Results

A step response curve showing how the motor
speed approaches its steady-state value.

## 6. Author

Control Engineering Student
