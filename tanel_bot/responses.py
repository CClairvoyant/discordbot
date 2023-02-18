import datetime
import random


def handle_response(message: str) -> str:
    message = message.lower()

    if message == "tammet":
        return ":flushed:"
    if message == "fed":
        return random.choice([":police_officer:",
                              "https://tenor.com/view/f-bi-raid-swat-gif-11500735",
                              "https://tenor.com/view/chicken-fbi-skeptic-chicken-funny-gif-14153035",
                              "https://tenor.com/view/cops-police-sirens-catching-crminals-what-you-gonna-do-gif"
                              "-22472645",
                              "https://tenor.com/view/realkimroro-police-gif-23236998"])
    if any(["eksam" in message,
            "vahetulemus" in message,
            "kontrolltöö" in message,
            "iti0101" in message,
            "sissejuhatus" in message]):
        return "Vahetulemused pannakse siia üles 18 detsember ja neid saab veel kontrollida."
    if "may question" in message:
        return "NO!"
