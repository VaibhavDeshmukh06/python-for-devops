import psutil

def get_threshold():

    cpu_threshold_value = int(input("Enter CPU threshold in % (0-100): "))
    disk_thrshold_value = int(input("Enter DISK threshold in % (0-100): "))
    memory_threshold_value = int(input("Enter MEM threshold in % (0-100): "))

    current_cpu = psutil.cpu_percent(interval=1)
    current_disk = psutil.disk_usage("/").percent
    current_memory = psutil.virtual_memory().percent

    cpu_status = "OK" if current_cpu <= cpu_threshold_value else "ALERT"
    disk_status = "OK" if current_disk <= disk_thrshold_value else "ALERT"
    mem_status = "OK" if current_memory <= memory_threshold_value else "ALERT"

    print(f"CPU: {current_cpu}% , THRESHOLD: {cpu_threshold_value}% , STATUS: {cpu_status}")
    print(f"DISK: {current_disk}% , THRESHOLD: {disk_thrshold_value}% , STATUS: {disk_status}")
    print(f"CPU: {current_memory}% , THRESHOLD: {memory_threshold_value}% , STATUS: {mem_status}")


get_threshold()


