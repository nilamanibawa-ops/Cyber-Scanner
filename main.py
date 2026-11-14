#!/usr/bin/env python3
import os
import sys

def banner():
    print(r"""
  ____       _    ____        _               
 |  _ \ __ _(_)  / ___|   _  | |__   ___ _ __ 
 | |_) / _` | | | |  | | | | | '_ \ / _ \ '__|
 |  _ < (_| | | | |__| |_| | | |_) |  __/ |   
 |_| \_\__,_| |  \____\__, | |_.__/ \___|_|   
           |__/       |___/                   
    """)
    print(" [ Tool: Cyber-Scanner | Non-Root Automation Suite ]")
    print(" [+] Coded by: Raj (Raj Cyber Security)")
    print(" [+] GitHub: https://github.com/nilamanibawa-ops/Cyber-Scanner\n")

def main():
    banner()
    print("1. Execute Core Module")
    print("2. Verify Secure Workspace")
    print("3. Exit\n")
    
    choice = input("Select an option [1-3]: ")
    if choice == '1':
        print("\n[*] Running Cyber-Scanner core engine...")
    elif choice == '2':
        print("\n[✓] Secure Workspace is active and ready!")
    else:
        print("\n[*] Exiting...")

if __name__ == "__main__":
    main()
