#!/bin/sh

#Configuracion de teclado español
setxkbmap latam &

#iconos del sistema
udiskie -t &

nm-applet &

blueman-applet &

volumeicon &

cbatticon -u 5 &

#Para colocar el wallpaper
nitrogen --restore &

optimus-manager-qt &

sh .screenlayout/pantallas_trabajo.sh

caffeine -a
