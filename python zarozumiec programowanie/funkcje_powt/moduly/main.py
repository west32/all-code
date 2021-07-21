import avg_speed

distance=float(input("ile km przebiegłes/przebiegłaś?"))
time = float(input("w jakim czasie?"))
Avg_speed= avg_speed.calculate_avg_speed(distance,time)
print (f" Twoja srednia szybkość biegu to {Avg_speed:.0f} km/h")
