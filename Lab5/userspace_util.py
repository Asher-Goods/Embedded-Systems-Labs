import psutil
import time
import subprocess

def get_cpu_utilization():
    return psutil.cpu_percent(interval=1)

def calculate_next_frequency(cpu_utilization):
    # Implement your frequency calculation logic based on coefficients
    # described in the lkml email
    # This is a placeholder, you need to adjust it accordingly
    return int(cpu_utilization * 100000)

def set_cpu_frequency(frequency):
    subprocess.run(["sudo", "bash", "-c", f"echo {frequency} > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed"])

def main():
    while True:
        cpu_utilization = get_cpu_utilization()
        next_frequency = calculate_next_frequency(cpu_utilization)

        # Get available frequencies
        available_frequencies = [int(f) for f in open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies").read().split()]

        # Find nearest available frequency
        nearest_frequency = min(available_frequencies, key=lambda x: abs(x - next_frequency))

        # Set CPU frequency
        set_cpu_frequency(nearest_frequency)

        print(f"CPU Utilization: {cpu_utilization}%, Next Frequency: {nearest_frequency} Hz")
        time.sleep(5)

if __name__ == "__main__":
    main()
