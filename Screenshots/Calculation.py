import math
Small_g = 9.81
Initial_velocity = 0.0
Specific_impulse = float(input("Enter the specific impulse in seconds: "))
Mass_of_Structure = float(input("Enter the mass of the structure in kgs: "))
Initial_fuel = float(input("Enter the value of initial fuel in the rocket (in kgs) : "))
Final_fuel = float(input("Enter the value of the remaining fuel in the rocket (in kgs) : "))
Time_elapsed = float(input("Enter the time elapsed since launch in seconds: "))

def calculate_velocity(small_g,specific_impulse,mass_of_Structure,Initial_mass,Final_fuel,Time_elapsed):
    Initial_mass = mass_of_Structure + Initial_fuel
    Final_mass = mass_of_Structure + Final_fuel

    Change_in_velocity = specific_impulse*small_g*math.log(Initial_mass/Final_mass)
    #This is the Tsiolkovsky formula
    Instantaneous_Velocity = Initial_velocity + Change_in_velocity
    return Instantaneous_Velocity

Acceleration_factor = 5.0
def calculate_altitude(time,Acceleration_factor):
    altitude = 0.5*Acceleration_factor*Small_g*time**2
    return altitude

Standard_temperature = 288.15
Lapse_rate = 0.0065

def calculate_temperature(Current_altitude, Standard_temperature, Lapse_rate,):
    temperature = Standard_temperature-(Lapse_rate*Current_altitude)
    return temperature

Current_velocity = calculate_velocity(Specific_impulse,Small_g,Mass_of_Structure,Initial_fuel,Final_fuel)
current_altitude = calculate_altitude(Time_elapsed,Acceleration_factor)
current_temperature = calculate_temperature(current_altitude,Standard_temperature,Lapse_rate)

print("\nRESULTS AT t = {:.1f}s".format(Time_elapsed))
print("Velocity:{:.2f}m/s".format(Current_velocity))
print("Altitude:{:.2f}meters".format(current_altitude))
print("Temperature:{:.2f}Kelvin".format(current_temperature))

