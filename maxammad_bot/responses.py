import datetime
import random


def handle_response(message: str) -> str:
    message = message.lower()
    response: str

    if "vaband" in message:
        return "Väga väga palun vabandust ma rohkem selles ära kirjuta ma luban sind."

    if "diskmat" in message:
        return "Tere! Selle aine mul on kõik korras ja ma läbitud eelmisel semestril diskreetne " \
               "matemaatika aine Harri Lensile ja mul on hinne 1 kõik korras läbitud kursuse. " \
               "Kellele on vaja abi kirjutada mulle privaat sõnume."

    if "max" in message:
        return "Hello, may question?"

    if "ping" in message or "tag" in message:
        return "&reply&Vabandust &ping&, rohkem ära teen tagidega"

    if "ära " in message or "Ära " in message:
        return "hästi ei teha rohkem vabandust palun"

    if "deklareer" in message:
        return "Tere,kõigile ma selle aine deklareerida sellel semestril. Mul on selline küsimus, " \
               "mis on vaja selle aine teha missuguseid ülesandeid kodune töö või mida? " \
               "Ma ei saa aru natuke selles aines. Ja arvestustöö toimub ülikoolis või kodus? Vabandust, palun kõigist."

    if "aine" in message or "kursus" in message:
        return random.choice(["Ma eelmisel aastal ära deklareeritud selle hulgad ained. "
                              "Ma deklareerisin sellel semestril,vabandust palun. "
                              "Okei, ma saan aru sulle &ping&, et ma loen sellel aastal sellel "
                              "semestril slaidide lingis ja õppida pähe ka, sest et varsti on esimene "
                              "kontrolltöö ja on vaja teen suurepärane ja viskada miinimumi punkti või rohkem, "
                              "kui ma saan.",
                              "See aine ma juba läbitud eelmisel aastal sügisel ja mulle hinne on 1. "
                              "Mul on korras, ma saan abistada kui on abi?",
                              "Tere vabandust mis see aine on? &ping&"])

    if "avatud ülikool" in message:
        return "Saan aru, aga ma õpin Avatud Ülikooli noh gruppis IADB jah see on õgige vabandust &ping&"

    if "privaat" in message or "sõber" in message:
        return random.choice(["Privaatsõnume? Vabandust.",
                              "Tere! Selle aine mul on kõik korras ja ma läbitud eelmisel semestril diskreetne matemaatika aine Harri Lensile ja mul on hinne 1 kõik korras läbitud kursuse. Kellele on vaja abi kirjutada mulle privaat sõnume."])
