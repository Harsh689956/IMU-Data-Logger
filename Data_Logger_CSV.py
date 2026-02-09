import serial as sr

COM_PORT = 'COM4'
BAUDRATE = 921600
CSV_FILE = 'sensor_data.csv'

ser = sr.Serial(COM_PORT, BAUDRATE, timeout=1)
print(f"Connected to {COM_PORT}")

with open(CSV_FILE, "w") as f:
    f.write("ax,ay,az,gx,gy,gz,Time,Interrupt_Flag\n")

print("Logging data... Press Ctrl+C to stop\n")

try:
    while True:
        line = ser.readline().decode('ascii', errors='ignore').strip()
        
        if line:
            print(f"Logged: {line}")

            with open(CSV_FILE, "a") as f:
                f.write(line + "\n")

except KeyboardInterrupt:
    print("\n\nLogging stopped")
finally:
    ser.close()
    print(f"Data saved to {CSV_FILE}")