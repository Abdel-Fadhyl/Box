import os
import tarfile
import urllib.request
import shutil
import sys

os.system("sudo apt install python3-pip")
os.system('pip3 install pyyaml')

import yaml

#Editer le fichier yml
fichier = open("mongo.yml", "a")
fichier.write("name: mongodb")
fichier.write("\nrepositories:")
fichier.write("\n - key: 'https://www.mongodb.org/static/pgp/server-4.4.asc%22'")
fichier.write("\n   repository: 'deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main'")
fichier.write("\nrequirements:")
fichier.write("\n - mongodb-org")
fichier.write("\nrun: |")
fichier.write("\n mongod $ARGS")
fichier.close()

#Parsing
with open("mongo.yml", 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)

os.system("sudo apt-get install software-properties-common")

#Variable
https = 'https://raw.githubusercontent.com/debuerreotype/docker-debian-artifacts/3503997cf522377bc4e4967c7f0fcbcb18c69fc8/buster/slim/rootfs.tar.xz'
folder = '/var/lib/box/'
folder2 = '/var/lib/box/base/'
folderV3 = '/var/lib/box/base/bin'
folderV4 = '/var/lib/box/base/sys/acpi'
folderV5 = '/var/lib/box/base/proc/acpi'
tar = 'rootfs.tar.xz'

#Création des dossiers
os.mkdir(folder)
os.mkdir(folder2)

#Vérifier que les dossiers on bien été monter
if os.path.exists(folder2):
 print ("Folder is created")
else:
 print ("Folder is not created")

#téléchargement du liens
urllib.request.urlretrieve(https, tar)

#Vérifier le téléchargement
if os.path.exists(tar):
 print ("Download okay")
else:
 print ("Download not okay")

#Décompressement du fichier tar
tar = tarfile.open(tar, "r:xz")
tar.extractall(folder2)
tar.close()

#Vérifier du décompressement
if os.path.exists(folderV3):
 print ("The tar folder is unpacked")
else:
 print ("The tar folder isn't unpacked")

#Monter le dossier proc
os.system('mount -tproc /proc /var/lib/box/base/proc')
#Vérification du dossier proc
if os.path.exists(folderV5):
 print ("The file proc is up")
else:
 print ("The file proc isn't up")

#Monter le dossier sys
os.system('mount -tproc /sys /var/lib/box/base/sys')

#Vérification du dossier sys
if os.path.exists(folderV4):
 print ("The file sys is up")
else:
 print ("The file sys isn't up")

#Monter le fichier random
os.system('mknod /var/lib/box/base/dev/random c 1 8')

#Pour faire un chroot
os.chroot(folder2)

#Pour être à la racine
os.chdir('/')

#Configuration du réseau
os.system("echo 'nameserver 8.8.8.8' > /etc/resolv.conf")

#test du update
os.system("apt update")
os.system("apt upgrade")
