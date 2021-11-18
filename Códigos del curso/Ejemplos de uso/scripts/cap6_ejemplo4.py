__author__ = 'febel'

duracion = {"horas": 0, "minutos": 0, "segundos": 0}


def hms_to_sec(duracion):
    total = duracion["horas"] * 3600 + duracion["minutos"] * 60 + duracion["segundos"]
    return total


def sec_to_hms(numseg):
    duracion["horas"] = numseg / 3600
    numseg = numseg % 3600
    duracion["minutos"] = numseg / 60
    duracion["segundos"] = numseg % 60
    return duracion


num_segundos = 39450
horas = sec_to_hms(num_segundos)
print(horas["horas"], ":", horas["minutos"], ":", horas["segundos"])

