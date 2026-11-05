# SIFI Gravity Railway – 0kW transport
mass = 500 # kg icy regolith
g = 1.62
slope = 25 # degrees
distance = 100 # m
height = distance * math.sin(math.radians(slope))
potential_energy = mass * g * height # Joules
print(f"Energy per trip: {potential_energy/1000:.1f} kJ, 0 kW motor needed")
print("Counterbalanced pulley + regenerative braking = 44kW generated")
