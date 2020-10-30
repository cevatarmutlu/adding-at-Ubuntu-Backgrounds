#!/bin/bash
cp "files/new_focal-wallpapers.xml" "/usr/share/gnome-background-properties/focal-wallpapers.xml"
cp "files/new_focal.xml" "/usr/share/backgrounds/contest/focal.xml"
rm -rf "files/"
rm -rf "$1"