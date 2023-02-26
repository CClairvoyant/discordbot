import datetime
import os


def entry(server, category, channel, log):
    if not os.path.exists(f"{os.getcwd()}/chat_logs/{server}" + f"/{category}" * bool(category)):
        os.makedirs(f"{os.getcwd()}/chat_logs/{server}" + f"/{category}" * bool(category))

    with open(f"{os.getcwd()}/chat_logs/{server}" + f"/{category}" * bool(category) + f"/{channel}.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log + "\n")

    print(f"[{server} | {category} | #{channel}]"
          + f"\n[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] " + log)
