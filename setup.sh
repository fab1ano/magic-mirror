#!/bin/bash

set -e

sudo apt install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox python3-pip chromium-browser xdotool

pip3 install -r requirements.txt

sudo mkdir -p /var/www/

sudo cp -r app /var/www/

# Prepare bash_profile
if test -f ~/.bash_profile && grep -q 'MagicMirror' /home/pi/.bash_profile; then
	echo 'I seems like ~/.bash_profile already contains the setup. Skipping configuration of bash_profile.'
else
	echo -e '# MagicMirror\n[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && startx -- -nocursor' >> /home/pi/.bash_profile
fi

# Configure openbox
if grep -q 'MagicMirror' '/etc/xdg/openbox/autostart'; then
	echo 'I seems like openbox is already configured. Skipping configuration of openbox.'
else
	cat 'openbox.autostart' | sudo tee -a '/etc/xdg/openbox/autostart' > /dev/null
fi

cp 'scripts/reload.sh' '/home/pi/.reload.sh'
