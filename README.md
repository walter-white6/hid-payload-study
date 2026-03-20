# hid-payload-study
Educational research project for Cybersecurity Module. This repository explores HID payload delivery and low-level system hooking for behavioral analysis in Windows environments. Developed for lab purposes only to study EDR detection patterns.
This repository contains a Python-based keystroke monitoring tool developed for a Computer Science Cybersecurity module. The project demonstrates the intersection of low-level system hooking, asynchronous event handling, and staged payload delivery via HID (Human Interface Device) emulation.

Key Technical Concepts:

API Hooking: Utilizes the pynput library to interface with the Windows User32.dll for global keyboard events.

Real-Time I/O: Implements unbuffered file writing to a local portable path.

Staged Deployment: The tool is designed to be deployed via a DuckyScript/BadUSB payload, demonstrating how unauthorized code can be executed through automated keystroke injection.

Forensic Logging: Includes ISO 8601 timestamps for session tracking.

Disclaimer: This tool is for educational purposes only. It was developed in a controlled lab environment to study behavioral analysis in modern EDR (Endpoint Detection and Response) systems.
