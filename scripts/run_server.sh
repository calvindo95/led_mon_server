#!/bin/sh

if [ -f $LED_MON_SERVER_EXEC ];
then
    $LED_MON_SERVER_EXEC
else
    echo "$LED_MON_SERVER_EXEC not found"
    exit
fi
