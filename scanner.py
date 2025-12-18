'''import socket

target_ip = "127.0.0.1"
port_to_check = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
result = s.connect_ex((target_ip, port_to_check))
if result == 0:
    print(f"Port {port_to_check} is open on {target_ip}")   
else:
    print(f"Port {port_to_check} is closed on {target_ip}")
s.close() '''

import socket
import sys

# Get input from the user
try:
    target_ip = input("Enter the target IP address (e.g., 192.168.1.1): ")
    
    # Define a range of common ports to scan
    port_range_start = 1
    port_range_end = 1024 
    
except KeyboardInterrupt:
    print("\n\nExiting program.")
    sys.exit()

# --- Start Scan ---
print("-" * 50)
print(f"Scanning target: {target_ip}")
print("-" * 50)

# Loop through the defined port range
for port in range(port_range_start, port_range_end + 1):
    # 1. Create the Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # Shorter timeout for speed

    # 2. Attempt to Connect
    # connect_ex is preferred as it avoids throwing exceptions for closed ports
    result = s.connect_ex((target_ip, port))

    # 3. Report the Result
    if result == 0:
        try:
            # Attempt to identify the service running on the port
            service = socket.getservbyport(port, "tcp")
        except:
            service = "Unknown"

        print(f"Port {port}: OPEN ({service})")

    # 4. Close the Connection
    s.close()

print("-" * 50)
print("Scan complete.")