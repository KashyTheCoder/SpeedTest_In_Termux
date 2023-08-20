import speedtest
from colorama import Fore, Style
import pyfiglet
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_termux_screen():
    os.system('clear')

def test_speed():
    if 'TERMUX' in os.environ:
        clear_termux_screen()
    else:
        clear_screen()

    st = speedtest.Speedtest()
    st.get_best_server()

    banner = pyfiglet.figlet_format("Speed Test", font="slant")
    print(Fore.CYAN + banner + Style.RESET_ALL)

    print(Fore.YELLOW + "Testing Download Speed..." + Style.RESET_ALL)
    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    print(Fore.GREEN + f"Download Speed: {download_speed:.2f} Mbps" + Style.RESET_ALL)

    print(Fore.YELLOW + "Testing Upload Speed..." + Style.RESET_ALL)
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps
    print(Fore.GREEN + f"Upload Speed: {upload_speed:.2f} Mbps" + Style.RESET_ALL)

if __name__ == "__main__":
    test_speed()
    input("Press Enter to exit...")
  
