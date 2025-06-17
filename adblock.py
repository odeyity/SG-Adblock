import os
from sys import platform
import shlex

class colours:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Install functions

def clear():
    os.system("CLEAR")

def install(osID):

    clear()

    if osID == "darwin":
        os.system("echo '# START Sky Go Adblock Domains' | sudo tee -a /private/etc/hosts > /dev/null")
        os.system("echo '0.0.0.0 skyads.ott.skymedia.co.uk' | sudo tee -a /private/etc/hosts > /dev/null")
        os.system("echo '0.0.0.0 604fc.v.fwmrm.net' | sudo tee -a /private/etc/hosts > /dev/null")
        os.system("echo '# END Sky Go Adblock Domains' | sudo tee -a /private/etc/hosts > /dev/null")
        print("Applying to hosts file...")
        print(colours.GREEN+"Applied ✅"+colours.END)
        input("\nPress any key to exit.")
    elif osID == "win32":
        pass
    else:
        pass

def uninstall(osID):

    clear()

    if osID == "darwin":
        os.chdir('/')
        
        print("Restoring hosts file...")

        # Read and clean the hosts file from local etc/hosts
        with open("etc/hosts", "r") as hosts_i:
            hosts_orig = hosts_i.read()
            cleaned_hosts = (
                hosts_orig
                .replace("# START Sky Go Adblock Domains", "")
                .replace("0.0.0.0 skyads.ott.skymedia.co.uk", "")
                .replace("0.0.0.0 604fc.v.fwmrm.net", "")
                .replace("# END Sky Go Adblock Domains", "")
                .strip()
            )

        print(colours.GREEN + "Restored ✅" + colours.END)
        
        print("Writing to hosts file...")

        # Clear the system hosts file
        os.system("echo '' | sudo tee /private/etc/hosts > /dev/null")

        # Write cleaned lines back
        for line in cleaned_hosts.splitlines():
            line = line.strip()
            if line:
                os.system(f"echo {shlex.quote(line)} | sudo tee -a /private/etc/hosts > /dev/null")

        print(colours.GREEN + "Written ✅" + colours.END)
        input("\nPress any key to exit.")


os.system('color')

installed = True

print(colours.PINK+colours.BOLD+"\n - Sky Go Adblock -\n\n"+colours.END)

if platform == "darwin":
    print("Detected operating system: " + colours.GREEN+"MacOS"+colours.END)
elif platform == "win32":
    print("Detected operating system: " + colours.GREEN+"Windows"+colours.END)
elif platform == "linux" or platform == "linux2":
    print("Detected operating system: " + colours.RED+"Linux"+colours.END)
else:
    print("Detected operating system: " + colours.RED+"Unknown"+colours.END)

# Checks if Sky Go Adblock is installed

if platform == "darwin": # MacOS

    os.chdir('/')

    hosts_i = open("etc/hosts", "r")
    hosts_orig = hosts_i.read()

    if "# START Sky Go Adblock Domains" in hosts_orig:
        print("Status: " + colours.GREEN + "Installed\n\n\n" + colours.END)
        installed = True
    else:
        print("Status: " + colours.RED + "Not installed\n\n\n" + colours.END)
        installed = False
else:
    print("Operating system is not supported by the adblocking tool.")
    input("\nPress any key to exit.")
    exit()

# Install or uninstall options

if installed == True:
    print("[1] Uninstall")
    print("[2] Exit")

    opt = input()
    if opt == "1":
        uninstall(platform)
    else:
        exit()

else:
    print("[1] Install")
    print("[2] Exit")

    opt = input()
    if opt == "1":
        install(platform)
    else:
        exit()


