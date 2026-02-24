from colorama import Fore, init
import time
import winsound 

init(autoreset=True)

print(Fore.YELLOW + "=================================")
print(Fore.YELLOW + "======== Pomodoro Timer  ========")
print(Fore.YELLOW + "=================================\n")

# Input section long
menutes = int(input(Fore.GREEN + "⏳ How many minutes do you want to work?: "))
seconds = menutes * 60
bar_length = 20

# to bo honest i found it defiult chatGPT how made it for me 
for i in range(seconds, -1, -1):
    progress = int((seconds - i) / seconds * bar_length)
    bar = "#" * progress + "-" * (bar_length - progress)
    print(Fore.YELLOW + f"[{bar}] {i//60:02d}:{i%60:02d} remaining", end="\r", flush=True)
    time.sleep(1)

print("\n" + Fore.RED + "🍅 Time’s up! Great job! Take a short break ☕")

winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
