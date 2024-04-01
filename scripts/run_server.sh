#!/bin/sh

if [ -f $LED_MON_SERVER_EXEC ];
then
    python3 $LED_MON_SERVER_EXEC
else
    echo "$LED_MON_SERVER_EXEC not found"
    exit
fi
