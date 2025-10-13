1) To print something

    echo "what you want to print"
    echo "sameer"

2) To list files and folders inside a folder

    ls (folder path)
    ls /sys/class/thermal/ 
    output -> different thermal zones that can be read by linux kernel

3) To read the text written in a file

    cat (file path)
    cat /sys/class/thermal/thermal_zone0/temp 
    output -> the current CPU temperature

4) To print something as well as run some command

    echo "what you want to print $(what you want to run as an inline command)"
    echo "CPU temperature: $(cat /sys/class/thermal/thermal_zone0/temp)"
    output -> CPU temperature reading in milidegrees

5) To perform some operation on the read text

    echo "what you read as input | awk '{what you want to do on each field of each line of input}'"
    echo "CPU temperature: $(cat /sys/class/thermal/thermal_zone0/temp | awk '{print $1/1000}')"
    output -> CPU temperature in milidegrees