
import os
import time
import subprocess

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def ketik(teks, delay=0.015):
    for huruf in teks:
        print(huruf, end="", flush=True)
        time.sleep(delay)
    print()

def bicara(teks):
    try:
        subprocess.run(
            ["termux-tts-speak", teks],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except:
        print(YELLOW + "[Suara tidak tersedia]" + RESET)

def tanya(nomor, pertanyaan, pilihan):
    print(f"\n{CYAN}{BOLD}{nomor}{RESET}")
    ketik(pertanyaan)

    for p in pilihan:
        print(GREEN + p + RESET)

    bicara(nomor + ". " + pertanyaan)

    while True:
        jawab = input(
            "\nEnter untuk menjawab / R untuk ulang suara: "
        ).strip().upper()

        if jawab == "R":
            bicara(nomor + ". " + pertanyaan)
            continue

        if jawab in ["A", "B", "C"]:
            return jawab

        print(RED + "Pilihan tidak valid!" + RESET)


clear()

print(GREEN + BOLD + """
╔════════════════════════════════════╗
║        VERY HACKER TEST v4.0       ║
║            SYSTEM ONLINE           ║
║          VOICE SYSTEM ON           ║
╚════════════════════════════════════╝
""" + RESET)

nama = input("Masukkan nama kamu: ")

ketik(f"\nSelamat datang, {nama}!")
bicara("Selamat datang " + nama)
ketik("Memulai tes kemampuan...\n")

jawaban = {}

jawaban[1] = tanya(
    "SOAL 1",
    "Apakah kamu pintar hack?",
    [
        "A. Bisa sedikit",
        "B. Diajarkan oleh Nazran",
        "C. Gak bisa"
    ]
)

jawaban[2] = tanya(
    "SOAL 2",
    "Kenapa kamu bisa menjalankan Python?",
    [
        "A. Cuma coba-coba pakai AI",
        "B. Aku salin kode orang",
        "C. Buat sendiri"
    ]
)

jawaban[3] = tanya(
    "SOAL 3",
    "Coba baca tulisan ASCII ini:",
    [
        "83 101 108 97 109 97 116 32",
        "107 97 109 117 32 109 101 110 97 110 103 33 33 33",
        "A. Bisa",
        "B. Gak bisa",
        "C. Error bang"
    ]
)

if jawaban[3] == "A":

    print(YELLOW + BOLD + "\n🔥 SOAL BONUS TERBUKA! 🔥" + RESET)

    soal_bonus = "Apa arti dari kode ASCII di atas? Ketik jawabanmu sendiri!"

    ketik(soal_bonus)
    bicara("Soal bonus. " + soal_bonus)

    jawaban_benar = "selamat kamu menang!!!"

    while True:
        bonus = input("\nJawaban kamu: ").strip().lower()

        if bonus == jawaban_benar:
            print(GREEN + "\n✓ JAWABAN BENAR!" + RESET)
            bicara("Jawaban benar. Akses diberikan.")
            break
        else:
            print(RED + "\n✗ SALAH CIK! ✗" + RESET)
            print(YELLOW + "LU HARUS BENER KALO MAU SELESAI!" + RESET)
            bicara("Jawaban salah. Coba lagi.")

else:
    print(YELLOW + "\nBONUS DILEWATI!" + RESET)

time.sleep(1)
clear()

print(GREEN + BOLD + """
╔════════════════════════════════════╗
║             HASIL TES              ║
║          VERY HACKER TEST          ║
╚════════════════════════════════════╝
""" + RESET)

print("Nama:", nama)

for nomor, jawaban_user in jawaban.items():
    print(f"Soal {nomor}: {jawaban_user}")

if jawaban[3] == "A":
    print("Soal Bonus: BENAR")

ascii_text = [
    83, 101, 108, 97, 109, 97, 116,
    32, 107, 97, 109, 117, 32, 109,
    101, 110, 97, 110, 103, 33, 33, 33
]

hasil = "".join(chr(x) for x in ascii_text)

print("\n" + CYAN + "HASIL DECODE ASCII:" + RESET)
print(GREEN + BOLD + hasil + RESET)

print("\n" + GREEN + "TES SELESAI! TERIMA KASIH SUDAH BERMAIN." + RESET)
print(CYAN + "VERY HACKER TEST v4.0" + RESET)

bicara("Tes selesai. Terima kasih sudah bermain.")
