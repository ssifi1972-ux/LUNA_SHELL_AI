# SIFI - Tribocharging simulation for NASA Grounding Challenge
# Simulates astronaut suit charging in PSR shadows
import math

g_moon = 1.62 # m/s2
charge_rate_sunlit = 50 # volts/sec due to tribocharging
photoemission_discharge = 40 # volts/sec in sunlit
charge_rate_psr = 120 # volts/sec in PSR (no photoemission)

def simulate_charge(time_sec, in_psr=False):
    charge = 0
    for t in range(time_sec):
        if in_psr:
            charge += charge_rate_psr
        else:
            charge += charge_rate_sunlit - photoemission_discharge
    return charge

print("Sunlit 1h:", simulate_charge(3600, False), "V")
print("PSR 1h:", simulate_charge(3600, True), "V - DANGER: Arc risk > 10kV")
print("SIFI solution: No human in PSR, robotic collector grounded via 2m rod")
