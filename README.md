magic mirror
============

Simple flask app to provide a dashboard interface for a magic mirror.

![Screenshot](./imgs/screenshot.png "Screenshot")

## Setup

The best way to start is with a plain Raspberry Pi OS lite.
Enable auto login from commandline for the user `pi` in `sudo raspi-config`.
Also, you might want to adjust the time zone.

Next, clone this repository and add your openweather API key and city in [`weather.py`](app/weather.py).

Then, launch the setup script:
```bash
$ ./setup.sh
```

And add these lines to `/etc/crontab`:
```
# Turn monitor on
0 5     * * 1-5 root /usr/bin/vcgencmd display_power 1
0 6     * * 0,6 root /usr/bin/vcgencmd display_power 1

# Turn monitor off
0 22    * * * root /usr/bin/vcgencmd display_power 0

# Reload page every day
55 4    * * * pi /home/pi/.reload.sh
```

Probably you want to adjust the times for turning the monitor on and off.

## Impression

Here is a sample image of my mirror that I assembled a while ago.
It is mainly inspired by Dylan Pierce's [MirrorMirror](https://metro.co.uk/2015/12/30/tech-genius-builds-magic-mirror-for-girlfriend-which-compliments-her-and-gives-weather-updates-5591422/) project.

<img src="imgs/mirror.jpg" width="250"/>
