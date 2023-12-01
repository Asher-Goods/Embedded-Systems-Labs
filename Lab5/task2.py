import time

while True:
    try:
        with open("/proc/stat", "r") as inputFile:
            line = inputFile.readline()
            name = []
            user, nice, system, idle, iowait, irq, softirq, steal, dummy1, dummy2 = ([] for _ in range(10))

            for _ in range(4):
                values = inputFile.readline().split()
                name.append(values[0])
                user.append(int(values[1]))
                nice.append(int(values[2]))
                system.append(int(values[3]))
                idle.append(int(values[4]))
                iowait.append(int(values[5]))
                irq.append(int(values[6]))
                softirq.append(int(values[7]))
                steal.append(int(values[8]))
                dummy1.append(int(values[9]))
                dummy2.append(int(values[10]))

        t_total1, t_usage1, t_idle1 = ([] for _ in range(3))

        for i in range(4):
            t_total1.append(user[i] + nice[i] + system[i] + idle[i] + iowait[i] + irq[i] + softirq[i] + steal[i])
            t_idle1.append(idle[i] + iowait[i])
            t_usage1.append(t_total1[i] - t_idle1[i])

        time.sleep(1)

        with open("/proc/stat", "r") as inputFile:
            line = inputFile.readline()

            for i in range(4):
                values = inputFile.readline().split()
                user[i] = int(values[1])
                nice[i] = int(values[2])
                system[i] = int(values[3])
                idle[i] = int(values[4])
                iowait[i] = int(values[5])
                irq[i] = int(values[6])
                softirq[i] = int(values[7])
                steal[i] = int(values[8])
                dummy1[i] = int(values[9])
                dummy2[i] = int(values[10])

        t_total2, t_usage2, t_idle2 = ([] for _ in range(3))

        for i in range(4):
            t_total2.append(user[i] + nice[i] + system[i] + idle[i] + iowait[i] + irq[i] + softirq[i] + steal[i])
            t_idle2.append(idle[i] + iowait[i])
            t_usage2.append(t_total2[i] - t_idle2[i])

        delta_total, delta_usage, freq_choice, desiredFreq, nextFreq = ([] for _ in range(5))
        util = [0] * 4

        for i in range(4):
            delta_total.append(t_total2[i] - t_total1[i])
            delta_usage.append(t_usage2[i] - t_usage1[i])
            util[i] = (delta_usage[i] / delta_total[i]) * 100
            print(f"CPU{i}:{util[i]}%")

        maxUtil = max(util)
        print(f"max util: {maxUtil}%")

        desiredFreq = int(1.25 * 15000 * maxUtil)

        if 600000 <= desiredFreq <= 15000000:  # Ensure desiredFreq is within a valid range
            with open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed", "w") as outfile:
                outfile.write(str(desiredFreq))
                print(f"Setting frequency to: {desiredFreq}")
        else:
            print(f"Invalid frequency value: {desiredFreq}")

    except IOError as e:
        print(f"Error: {e}")
        time.sleep(1)  # Add a short delay before retrying in case of a file access issue
