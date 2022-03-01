import psutil


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


# Measure CPU util
def monitor_cpu_util():
    print("\n CPU UTIL")
    print(psutil.cpu_precent())

# Count working CPU cores


def mointor_cpu_cores():
    print("\n CPU CORES")
    print(psutil.cpu_count())

# Measure CPU frequencies


def monitor_cpu_freq():
    print("\n CPU FREQUENCIES")
    print("{}Mhz".format(psutil.cpu_freq().current))


# Monitor RAM Usage
def monitor_ram():
    print("\n RAM USAGE")
    virtual_memory = psutil.virtual_memory()
    print("Total Memory {} bytes".format(virtual_memory.total))
    print("Available Memory {} bytes".format(virtual_memory.available))
    print("Used Memory {} bytes".format(virtual_memory.used))
    print("Percentage used {}%".format(virtual_memory.percent))

# Monitor disk partitions
def monitor_disk():
    print("\n DISK USAGE")
    print(psutil.disk_partitions())

# Disk utilization
def monitor_disk_usage():
    print("\n DISK USAGE")
    disk_usage = psutil.disk_usage('/')
    print("Total Memory {} bytes".format(disk_usage.total))
    print("Free Memory {} bytes".format(disk_usage.free))
    print("Used Memory {} bytes".format(disk_usage.used))
    print("Percentage used {}%".format(disk_usage.percent))

# Monitor network requests
def monitor_network():
    print("\n NETWORK REQUESTS")
    io_stats = psutil.net_io_counters()
    print("Total Bytes Sent {} ".format(io_stats.bytes_sent))
    print("Total Bytes Received {} ".format(io_stats.bytes_recv))

# Monitor battery usage
def monitor_battery():
    print("\n MONITOR BATTERY")
    battery_info =psutil.sensors_battery()
    print(" Battery Percent: {}".format(battery_info.percent))
    print(" Seconds left: {}".format(battery_info.secsleft))

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
