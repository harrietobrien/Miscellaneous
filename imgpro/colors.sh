#!/bin/bash

# rich text
for color in {1..255}; do
echo -en "\033[38;5;${color}m"
echo -n "${color} "
done
echo
# background
for color in {1..255}; do
echo -en "\033[48;5;${color}m"
echo -n "${color} "
done
tput -S <<<$'sgr0\nel'
echo
