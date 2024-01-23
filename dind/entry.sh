#!/bin/bash

function wait_for_process () {
    local max_time_wait=30
    local process_name="$1"
    local waited_sec=0
    while ! pgrep "$process_name" >/dev/null && ((waited_sec < max_time_wait)); do
        echo "Process $process_name is not running yet. Retrying in 1 seconds"
        echo "Waited $waited_sec seconds of $max_time_wait seconds"
        sleep 1
        ((waited_sec=waited_sec+1))
        if ((waited_sec >= max_time_wait)); then
            return 1
        fi
    done
    return 0
}

echo "Starting supervisor"
/usr/bin/supervisord -n >> /dev/null 2>&1 &

echo "Waiting for processes to be running"
processes=(dockerd)

for process in "${processes[@]}"; do
    wait_for_process "$process"
    if [ $? -ne 0 ]; then
        echo "$process is not running after max time"
        exit 1
    else 
        echo "$process is running"
    fi
done

sleep infinity

# Wait processes to be running
"$@"
