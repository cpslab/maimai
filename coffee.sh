#!/bin/bash
echo $1
PRE=`cat /home/pi/maimai/coffee_now`
echo $PRE
echo $PRE >> /home/pi/maimai/coffee_history
echo $1 > /home/pi/maimai/coffee_now
