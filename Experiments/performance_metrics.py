'''
1) Temperature :

- Two independent layers manage thermals on the Pi

| **Layer**          | **Who controls it**                                | **Where settings live**             | **Example parameter**              | **Purpose**                                                          |
| ------------------ | -------------------------------------------------- | ----------------------------------- | ---------------------------------- | -------------------------------------------------------------------- |
| **Firmware layer** | The **VideoCore GPU firmware** (runs before Linux) | `/boot/config.txt` and `vcgencmd`   | `temp_soft_limit=60`               | Sets **soft throttle limit**, **firmware-level thermal control**     |
| **Kernel layer**   | The **Linux thermal subsystem**                    | `/sys/class/thermal/thermal_zone*/` | `trip_point_*_temp`, `cdev*`, etc. | Controls **Linux-level thermal zones**, **fan**, **cooling devices** |


- There are two temperature sensors in raspberry pi 5, one measures the temperature of CPU via kernel interface while other 
measures the temperature of GPU via firmware interface. 
----------------------------------------------------------------------------------------------------------------------------------------------
- To know what different thermal zones are exposed to linux kernel,

code -> ls /sys/class/thermal/
output -> cooling_device0 thermal_zone0

so this means only one thermal zone (thermal_zone0) is being exposed to the linux kernel while the other one can be accessed 
only using the firmware.
----------------------------------------------------------------------------------------------------------------------------------------------
- To read the CPU temperature (in milidegrees),

code -> cat /sys/class/thermal/thermal_zone0/temp
output -> 44100 
-----------------------------------------------------------------------------------------------------------------------------------------------
- To read the GPU temperature 

code -> vcgencmd measure_temp
output -> temp=46.1'C
-----------------------------------------------------------------------------------------------------------------------------------------------
- There are various parameters associated with each thermal zone such as what cooling devices it will interact with, 
what are different tripping points and what happens after each tripping point is reached, etc. All these settings are
present as files inside each thermal zone folder,

code -> ls /sys/class/thermal/thermal_zone0
output -> available_policies  cdev1_weight      cdev3_weight      k_d     policy             trip_point_0_hyst  trip_point_2_hyst  trip_point_4_hyst
cdev0               cdev2             cdev4             k_i     power              trip_point_0_temp  trip_point_2_temp  trip_point_4_temp
cdev0_trip_point    cdev2_trip_point  cdev4_trip_point  k_po    slope              trip_point_0_type  trip_point_2_type  trip_point_4_type
cdev0_weight        cdev2_weight      cdev4_weight      k_pu    subsystem          trip_point_1_hyst  trip_point_3_hyst  type
cdev1               cdev3             hwmon0            mode    sustainable_power  trip_point_1_temp  trip_point_3_temp  uevent
cdev1_trip_point    cdev3_trip_point  integral_cutoff   offset  temp               trip_point_1_type  trip_point_3_type
---------------------------------------------------------------------------------------------------------------------------------------------------
- Hitting the temperature limits is not harmful to SoC but it will cause the CPU to throttle (decrease in clock frequency). When the core 
temperature is between 80°C and 85°C, the Arm cores will be throttled back. If the temperature exceeds 85°C, the Arm cores and the GPU will 
be throttled back.
'''