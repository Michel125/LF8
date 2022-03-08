import psutil
from psutil import virtual_memory


# Measure CPU times


def monitor_cpu_times():
    print("\n CPU TIMES")
    cpu_times = psutil.cpu_times()
    user_time = round(cpu_times.user/3600)
    system_time = round(cpu_times.system/3600)
    idle_time = round(cpu_times.idle/3600)
    print("Time spent on processes by the User: {}".format(user_time))
    print("Time spent on processes by the System: {}".format(system_time))
    print("Time spent on processes by Idle: {}".format(idle_time))

    if user_time == 2:
        print("Hello World")
    
    if system_time == 3:
        print("Hello World")

    if idle_time == 39:
        print("Hello World")


# Measure CPU util


def monitor_cpu_util():
    print("\n CPU UTIL")
    print(psutil.cpu_percent())

    if psutil.cpu_percent() == 0.0:
        print("Hello World")

    
         



# Count working CPU cores


def mointor_cpu_cores():
    print("\n CPU CORES")
    print(psutil.cpu_count())

    if psutil.cpu_count() == 12:
        pass
        
    else:
        print("Error")


# Measure CPU frequencies


def monitor_cpu_freq():
    print("\n CPU FREQUENCIES")
    print("{}Mhz".format(psutil.cpu_freq().current))

    if psutil.cpu_freq().current == 2101.0:
        print("Hello World")


# Monitor RAM Usage


def monitor_ram():
    print("\n RAM USAGE")
    virtual_memory = psutil.virtual_memory()
    total_rammemory = (virtual_memory.total)
    available_rammemory = (virtual_memory.available)
    used_rammemory = (virtual_memory.used)
    percent_rammemory = (virtual_memory.percent)
    print("Total Memory {} bytes".format(total_rammemory))
    print("Available Memory {} bytes".format(available_rammemory))
    print("Used Memory {} bytes".format(used_rammemory))
    print("Percentage used {}%".format(percent_rammemory))

    if total_rammemory == 8164143104:
        print("Hello World")

    if available_rammemory == 1609498624:
        print("Hello World")

    if used_rammemory == 6554644480:
        print("Hello World")

    if percent_rammemory == 80.3:
        print("Hello World")
    
    





# Monitor disk partitions


def monitor_disk():
    print("\n DISK PARTITIONS")
    print(psutil.disk_partitions())

    #Hier existiert kein Threshhold wert für eine if abfrage



# Disk utilization


def monitor_disk_usage():
    print("\n DISK USAGE")
    disk_usage = psutil.disk_usage('/')
    print("Total Memory {} bytes".format(disk_usage.total))
    print("Free Memory {} bytes".format(disk_usage.free))
    print("Used Memory {} bytes".format(disk_usage.used))
    print("Percentage used {}%".format(disk_usage.percent))

    if disk_usage.total == 254721126400:
        print("Hello World")

    if disk_usage.free == 138786320384:
        print("Hello World")

    if disk_usage.used == 115934806016:
        print("Hello World")

    if disk_usage.percent == 45.5:
        print("Hello World")


# Monitor network requests


def monitor_network():
    print("\n NETWORK REQUESTS")
    io_stats = psutil.net_io_counters()
    print("Total Bytes Sent {} ".format(io_stats.bytes_sent))
    print("Total Bytes Received {} ".format(io_stats.bytes_recv))

    if io_stats.bytes_sent == 905211085:
        print("Hello World")

    if io_stats.bytes_recv == 1260587060:
        print("Hello World")


# Monitor battery usage


def monitor_battery():
    print("\n MONITOR BATTERY")
    battery_info =psutil.sensors_battery()
    print(" Battery Percent: {}%".format(battery_info.percent))
    print(" Seconds left: {}".format(battery_info.secsleft))

    if battery_info.percent == 96:
        print("Hello Wolrd")

    if battery_info.secsleft == -2:
        print("Hello World")


# Run all checks


def run_all_checks():
    monitor_cpu_times()
    monitor_cpu_util()
    mointor_cpu_cores()
    monitor_cpu_freq()
    monitor_ram()
    monitor_disk()
    monitor_disk_usage()
    monitor_network()
    monitor_battery()


run_all_checks()


#"if" abfragen sind nicht final (nur als Test)
