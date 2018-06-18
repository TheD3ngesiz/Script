#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os as kriptox


kriptox.system('clear' if kriptox.name == 'nt' else 'reset')
print("""
1) Sha256 Şifrele 
2) MD5 Şifrele
3) Şifre Kırıcı Scriptleri İndir
4) Makinayı Güncelleştir  ( Update && Upgrade )
5) Source List ' i Güncelle
6) Scriptten çık . (Exit)
""")
main = raw_input('Hangi İşlemi Gerçekleştireceksiniz ? : ')

if main == "1":
	vht = raw_input('Şifrelemek İstediğiniz Sözcük: ')
	cmd = kriptox.system('echo -n "' + vht +'" | sha256sum')
	quit()

if main == "2":
	vh = raw_input('Şifrelemek İstediğiniz Sözcük: ')
	cmd1 = kriptox.system('echo -n "' + vh +'" | md5sum')
	quit()
	
if main == "3":
	dng = raw_input("Devam etmek istediğinden emin misin ? E/h : ")
	if dng == "E":
		print("""
		
		1)PyBozoCrack
		2)FindMyHash
		3)Scripti Kapat Çık
		
		""")
		oa = raw_input("Hangisini İndirmek İstersiniz ? : ")
		if oa == "1":
			kriptox.system("cd Desktop && git clone https://github.com/petedmarsh/pybozo.git")
			kriptox.system('clear' if kriptox.name == 'nt' else 'reset')
			quit()
		
		elif oa == "2":
			kriptox.system("cd Desktop && git clone https://github.com/Talanor/findmyhash.git")
			kriptox.system('clear' if kriptox.name == 'nt' else 'reset')
			quit()
		
		elif oa == "3":
			kriptox.system('clear' if kriptox.name == 'nt' else 'reset')
			quit()

if main == "4":
	je = raw_input("Güncelleştirmek İstediğinizden Emin misiniz ? E/h: ")
	if je == "E":
		cmd4 = kriptox.system("sudo apt-get update && apt-get upgrade")
		kriptox.system('clear' if kriptox.name == 'nt' else 'reset')
		print("Güncelleştirildi !")
		quit()
		
	else:
		print("Yönetici izni gerekiyor . Script kapanıyor ...")
		quit()

if main == "5":
	cmd1 = sistema.system("echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
	quit()

if main == "6":
	quit()
