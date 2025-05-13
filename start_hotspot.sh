#!/bin/sh
if ! nmcli -t -f NAME con show | grep -q "servo"; then
	nmcli con add type wifi ifname wlan0 con-name servo autoconnect yes ssid servo 
fi
nmcli con modify servo 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared
nmcli con modify servo wifi-sec.key-mgmt wpa-psk
nmcli con modify servo wifi-sec.psk "12345678"
nmcli con up servo
