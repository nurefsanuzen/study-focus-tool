import time
import os
from datetime import datetime

blocked_apps = ["chrome", "spotify", "discord"]
log_file = "focus_log.txt"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pomodoro_timer(work_minutes=25, break_minutes=5):
    print(f"\nÇalışma süresi başladı: {work_minutes} dakika")
    time.sleep(work_minutes * 60)

    print("\nMolaya çıktın! 5 dakika ara ver.")
    time.sleep(break_minutes * 60)

def block_apps():
    print("\nDikkat dağıtan uygulamalar kapatılıyor...")
    for app in blocked_apps:
        try:
            os.system(f"taskkill /f /im {app}.exe" if os.name == "nt" else f"pkill {app}")
        except:
            pass
    print("Uygulamalar kapatıldı.")

def log_session(minutes):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {minutes} dakika odaklanıldı\n")

def daily_report():
    if not os.path.exists(log_file):
        print("\nHenüz kayıt bulunamadı.")
        return

    print("\n--- Günlük Odaklanma Raporu ---")
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())

def menu():
    print("=== Study Focus Tool ===")
    print("1 - Pomodoro başlat (25 dk)")
    print("2 - Uygulamaları engelle")
    print("3 - Günlük raporu göster")
    print("4 - Çıkış")

while True:
    menu()
    choice = input("Seçiminizi girin (1-4): ")

    if choice == "1":
        clear_screen()
        pomodoro_timer()
        log_session(25)
    elif choice == "2":
        clear_screen()
        block_apps()
    elif choice == "3":
        clear_screen()
        daily_report()
    elif choice == "4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim!")
