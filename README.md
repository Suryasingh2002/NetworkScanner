# NetworkScanner
1. Project Title & Description
 
Python-Based Network Reconnaissance Tool
This project is a custom network scanner built in Python. It is designed to perform reconnaissance on a target IP address by identifying active ports and the services running on them. This tool demonstrates core concepts of the TCP/IP stack, socket programming, and vulnerability assessment.

2. Security Features & Concepts
This is the most important section for your resume. It shows you know the "Why" behind the "How."

Security Concepts Implemented
Reconnaissance (Footprinting): Implementing the first stage of the Cyber Attack Lifecycle by gathering information about a target's infrastructure.

TCP Connect Scanning: Utilizing the socket library to complete (or attempt) the TCP Three-Way Handshake to verify if a port is open.

Service Identification: Using socket.getservbyport to identify potentially vulnerable services running on open ports.

Timeout Handling: Managing network latency and preventing detection through controlled connection timeouts.

3. How to Use
Show that your code is functional and well-organized.

Installation & Usage
Clone the repository: git clone <your-repo-link>

Navigate to the directory: cd NetworkScanner

Run the script: python scanner.py

Enter the target IP address when prompted (e.g., 127.0.0.1 for local testing).

4. Technical Skills Demonstrated
 
Tech Stack
Language: Python 3.x

Libraries: socket (Networking), sys (System operations). * Tools: Git/GitHub for version control.
