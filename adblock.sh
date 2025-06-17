#!/bin/bash

echo -e "\n - Sky Go Adblock -\n"

# Check OS
OS="$(uname)"
if [ "$OS" == "Darwin" ]; then
    echo "Detected operating system: macOS"
else
    echo "Operating system is not supported by the adblocking tool."
    read -n 1 -s -r -p "Press any key to exit."
    exit 1
fi

# Check installation status
if grep -q "# START Sky Go Adblock Domains" /private/etc/hosts; then
    echo -e "Status: Installed\n"
    INSTALLED=true
else
    echo -e "Status: Not installed\n"
    INSTALLED=false
fi

# Install function
install() {
    echo "Applying to hosts file..."
    {
        echo "# START Sky Go Adblock Domains"
        echo "0.0.0.0 skyads.ott.skymedia.co.uk"
        echo "0.0.0.0 604fc.v.fwmrm.net"
        echo "# END Sky Go Adblock Domains"
    } | sudo tee -a /private/etc/hosts > /dev/null
    echo "Applied ✅"
    read -n 1 -s -r -p "Press any key to exit."
}

# Uninstall function
uninstall() {
    echo "Restoring hosts file..."

    # Check if backup exists
    if [ ! -f "etc/hosts" ]; then
        echo "Backup hosts file not found at etc/hosts."
        echo "Creating backup from current /private/etc/hosts..."
        mkdir -p etc
        sudo cp /private/etc/hosts etc/hosts
        echo "Backup created at etc/hosts ✅"
    fi

    CLEANED=$(sed '/# START Sky Go Adblock Domains/,/# END Sky Go Adblock Domains/d' etc/hosts)

    echo "" | sudo tee /private/etc/hosts > /dev/null

    while IFS= read -r line; do
        [ -n "$line" ] && echo "$line" | sudo tee -a /private/etc/hosts > /dev/null
    done <<< "$CLEANED"

    echo "Restored ✅"
    read -n 1 -s -r -p "Press any key to exit."
}


# Prompt user
if [ "$INSTALLED" = true ]; then
    echo "[1] Uninstall"
    echo "[2] Exit"
    read -r opt
    if [ "$opt" = "1" ]; then
        uninstall
    fi
else
    echo "[1] Install"
    echo "[2] Exit"
    read -r opt
    if [ "$opt" = "1" ]; then
        install
    fi
fi
