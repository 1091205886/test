# /bin/python3.8
from nvitop import Device
from nvitop import Device, GpuProcess, NA, colored

devices = Device.all()  # or `Device.cuda.all()` to use CUDA ordinal instead
for device in devices:
    processes = device.processes()  # type: Dict[int, GpuProcess]
    sorted_pids = sorted(processes.keys())

    print(device)
    print(f'  - Fan speed:       {device.fan_speed()}%')
    print(f'  - Temperature:     {device.temperature()}C')
    print(f'  - GPU utilization: {device.gpu_utilization()}%')
    print(f'  - Total memory:    {device.memory_total_human()}')
    print(f'  - Used memory:     {device.memory_used_human()}')
    print(f'  - Free memory:     {device.memory_free_human()}')
    print(f'  - Processes ({len(processes)}): {sorted_pids}')
    if len(processes) > 0:
        processes = GpuProcess.take_snapshots(processes.values(), failsafe=True)
        processes.sort(key=lambda process: (process.username, process.pid))

        print(colored(f'  - Processes ({len(processes)}):', color='blue', attrs=('bold',)))
        fmt = '    {pid:<5}  {username:<8} {cpu:>5}  {host_memory:>8} {time:>8}  {gpu_memory:>8}  {sm:>3}  {command:<}'.format
        print(colored(fmt(pid='PID', username='USERNAME',
                          cpu='CPU%', host_memory='HOST-MEM', time='TIME',
                          gpu_memory='GPU-MEM', sm='SM%',
                          command='COMMAND'),
                      attrs=('bold',)))
        for snapshot in processes:
            print(fmt(pid=snapshot.pid,
                      username=snapshot.username[:7] + ('+' if len(snapshot.username) > 8 else snapshot.username[7:8]),
                      cpu=snapshot.cpu_percent, host_memory=snapshot.host_memory_human,
                      time=snapshot.running_time_human,
                      gpu_memory=(snapshot.gpu_memory_human if snapshot.gpu_memory_human is not NA else 'WDDM:N/A'),
                      sm=snapshot.gpu_sm_utilization,
                      command=snapshot.command))
    print('-' * 120)
