# IMU-Data-Logger
STM32 Data Logger using MPU6500

Overview

This project implements a high-speed data logging system using the STM32F446RE Nucleo development board and the MPU6500 motion sensor. The system captures sensor data at approximately 1 kHz, timestamps each reading using the RTC, and transmits the data to a PC via UART for storage and analysis.
The received serial data is parsed using a Python script and saved into a CSV (Excel-compatible) file for further processing.

Hardware Used

- Microcontroller: Nucleo Board STM32F446RE 
- Sensor: MPU6500 (Accelerometer + Gyroscope)
- Communication Interfaces: SPI, UART
- Peripherals: RTC, GPIO

Features

 High-frequency data acquisition (~1 kHz)
 Timestamped sensor readings using RTC
 Reliable sensor communication via SPI
 Real-time data transmission over UART
 Automatic CSV generation using Python
 Excel-ready dataset for analysis

System Workflow

1. MPU6500 collects motion data.
2. STM32 reads sensor values via I2C/SPI.
3. Each reading is tagged with a real-time timestamp.
4. Data is transmitted to the PC through UART.
5. A Python script captures the serial stream and stores it as a CSV file.

How to Run the Project

1. Clone or download this repository.
2. Open the project in STM32CubeIDE.
3. Build and flash the code to the STM32F446RE board.
4. Connect the board to your PC via UART.
5. Open a serial monitor to verify the output.
6. Run the provided Python script to log data into a CSV file.

Applications

- Motion tracking
- Vibration analysis
- Robotics
- Embedded system research
- Inertial measurement projects

Author

Developed as part of an embedded systems/data logging project using STM32.
