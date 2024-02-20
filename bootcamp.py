#bruk av psutil for å hente statistikk om serveren og system. 
#psutil er et library som er laget for lignende bruk slik som det oppgaven ber om 
import psutil

def get_ram_usage():
    # Get RAM usage statistics
    ram = psutil.virtual_memory()
    total_ram = ram.total
    available_ram = ram.available
    used_ram = ram.used
    ram_usage_percent = ram.percent
    return total_ram, available_ram, used_ram, ram_usage_percent

def get_disk_partitions():
    # Get disk partitions and their usage statistics
    disk_partitions = psutil.disk_partitions()
    disk_info = {}
    for partition in disk_partitions:
        partition_usage = psutil.disk_usage(partition.mountpoint)
        disk_info[partition.mountpoint] = {
            'total': partition_usage.total,
            'used': partition_usage.used,
            'free': partition_usage.free,
            'percent': partition_usage.percent
        }
    return disk_info

def get_cpu_usage():
    # Get CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

def main():
    total_ram, available_ram, used_ram, ram_usage_percent = get_ram_usage()
    print("RAM Information:")
    print(f"Total RAM: {total_ram / (1024*1024*1024):.2f} GB")
    print(f"Available RAM: {available_ram / (1024*1024*1024):.2f} GB")
    print(f"Used RAM: {used_ram / (1024*1024*1024):.2f} GB")
    print(f"RAM Usage Percentage: {ram_usage_percent}%\n")
    
    cpu_percent = get_cpu_usage()
    print("CPU Usage Percentage:")
    print(f"Current CPU Usage: {cpu_percent}%\n")
    
    disk_info = get_disk_partitions()
    print("Disk Information:")
    for partition, info in disk_info.items():
        print(f"Partition: {partition}")
        print(f"Total size: {info['total'] / (1024*1024*1024):.2f} GB")
        print(f"Used: {info['used'] / (1024*1024*1024):.2f} GB")
        print(f"Free: {info['free'] / (1024*1024*1024):.2f} GB")
        print(f"Usage Percentage: {info['percent']}%\n")

if __name__ == "__main__":
    main()
