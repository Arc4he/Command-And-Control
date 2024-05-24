#!/usr/bin/env python3

from command_and_control import Listener
from termcolor import colored

if __name__ == '__main__':
    ip = input(colored("\n[+] Enter your IP Address >> ", 'green'))
    my_listener = Listener(ip, 443)
    my_listener.run()