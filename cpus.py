import psutil

pid_cpu_dict = {} # {pid:cpu_percent,...}
for p in psutil.pids():
    process = psutil.Process(p)
    try:
        cpu_per = process.cpu_percent(interval=1)
    except psutil.AccessDenied:
        continue
    # pids.append({p:cpu_per})
    if cpu_per > 0.0:
        if cpu_per not in pid_cpu_dict.keys():
            pid_cpu_dict[cpu_per] = [p]
        else:
            pid_cpu_dict[cpu_per].append(p)

print(pid_cpu_dict)

max_cpu_per = 0.0

for k in pid_cpu_dict.keys():
    if k > max_cpu_per:
        max_cpu_per = k

for process in pid_cpu_dict[max_cpu_per]:
    print("The busiest process's name is: %s" % (psutil.Process(process).name()))
