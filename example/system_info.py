#!/usr/bin/env python3
"""
Hey Claude, write a Python script that uses the sys and os modules, and possibly others, 
to fetch and print various python and platform information.

System and Python Information Script
Displays comprehensive information about the Python interpreter and platform
"""

import sys
import os
import platform
import site
from datetime import datetime


def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)


def python_info():
    """Display Python interpreter information"""
    print_section("PYTHON INTERPRETER INFORMATION")
    print(f"Python Version: {sys.version}")
    print(f"Python Version Info: {sys.version_info}")
    print(f"Python Implementation: {platform.python_implementation()}")
    print(f"Python Compiler: {platform.python_compiler()}")
    print(f"Python Build: {platform.python_build()}")
    print(f"Python Branch: {platform.python_branch()}")
    print(f"Python Revision: {platform.python_revision()}")


def platform_info():
    """Display platform/OS information"""
    print_section("PLATFORM INFORMATION")
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Architecture: {platform.architecture()}")
    print(f"Platform: {platform.platform()}")
    print(f"Node (hostname): {platform.node()}")


def path_info():
    """Display Python path and executable information"""
    print_section("PATH INFORMATION")
    print(f"Python Executable: {sys.executable}")
    print(f"Python Prefix: {sys.prefix}")
    print(f"Python Exec Prefix: {sys.exec_prefix}")
    print(f"Base Prefix: {sys.base_prefix}")
    print(f"Base Exec Prefix: {sys.base_exec_prefix}")
    print(f"\nSite Packages:")
    for path in site.getsitepackages():
        print(f"  - {path}")
    print(f"\nUser Site Packages: {site.getusersitepackages()}")
    print(f"\nPython Path (sys.path):")
    for i, path in enumerate(sys.path, 1):
        print(f"  {i}. {path}")


def environment_info():
    """Display relevant environment variables"""
    print_section("ENVIRONMENT VARIABLES")
    env_vars = ['PATH', 'PYTHONPATH', 'PYTHONHOME', 'HOME', 'USER', 
                'SHELL', 'LANG', 'LC_ALL', 'VIRTUAL_ENV']
    
    for var in env_vars:
        value = os.environ.get(var, 'Not set')
        if var == 'PATH' and value != 'Not set':
            print(f"{var}:")
            for path in value.split(os.pathsep):
                print(f"  - {path}")
        else:
            print(f"{var}: {value}")


def system_info():
    """Display system-level information"""
    print_section("SYSTEM INFORMATION")
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"User: {os.getenv('USER', 'Unknown')}")
    print(f"Process ID: {os.getpid()}")
    #print(f"Parent Process ID: {os.getppid()}")
    
    # File system encoding
    print(f"File System Encoding: {sys.getfilesystemencoding()}")
    print(f"Default Encoding: {sys.getdefaultencoding()}")
    
    # CPU count
    try:
        print(f"CPU Count: {os.cpu_count()}")
    except AttributeError:
        print("CPU Count: Not available")
    
    # Load average (Unix-like systems only)
    try:
        load1, load5, load15 = os.getloadavg()
        print(f"Load Average (1, 5, 15 min): {load1:.2f}, {load5:.2f}, {load15:.2f}")
    except (AttributeError, OSError):
        print("Load Average: Not available on this platform")


def runtime_info():
    """Display runtime and limits information"""
    print_section("RUNTIME INFORMATION")
    print(f"Max Integer Size: {sys.maxsize}")
    print(f"Max Unicode: {sys.maxunicode}")
    print(f"Recursion Limit: {sys.getrecursionlimit()}")
    print(f"Byte Order: {sys.byteorder}")
    print(f"Float Info: {sys.float_info}")
    print(f"Int Info: {sys.int_info}")


def main():
    """Main function to display all information"""
    print("\n" + "="*60)
    print("  SYSTEM AND PYTHON INFORMATION REPORT")
    print(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)
    
    python_info()
    platform_info()
    path_info()
    environment_info()
    system_info()
    runtime_info()
    
    print("\n" + "="*60)
    print("  END OF REPORT")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
