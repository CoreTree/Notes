#!/bin/bash

# Accessing stdout on active process
```bash
process_name="python"
proc_id=$(echo $(ps -aux | grep $process_name | grep -v grep) | cut -d' ' -f 2)
sudo tail -f /proc/$proc_id/fd/1
```
