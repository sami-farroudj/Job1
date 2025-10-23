def time_to_text(minutes):
    heures = minutes // 60
    resmin = minutes % 60
    print(f'{heures} heure(s)et {resmin} minute(s)')
    

time_to_text(150)
