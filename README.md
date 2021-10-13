Projet Box
===============

#### TIC-UNI2

*Pour ce projet nous avons utilisé le langage Python.*

### Préparation
---------------
+ Pour la préparation du dossier de travail je l'ai fait depuis notre fichier python que nous avons nommé **test.py**, d'abord nous avons fait des variables :
 ```
    folder = '/var/lib/box/' 
    folder2 = '/var/lib/box/base/'
```
- Puis j'ai utilisé une library de python **os**
```
    os.mkdir(folder)
    os.mkdir(folder2)
```

+ Ensuite pour la base Debian j'ai fait une variable avec url et une variable pour le nommer puis j'ai téléchargé avec une library de python **urllib.request** :
```
    https = ' https://raw.githubusercontent.com/debuerreotype/docker-debian-artifacts/3503997cf522377bc4e4967c7f0fcbcb18c69fc8/buster/slim/rootfs.tar.xz'``
    tar = 'rootfs.tar.xz
    urllib.request.urlretrieve(https, tar)
```
   - Pour finir j'ai décompresser avec une library python **tarfile** :
``` 
        tar = tarfile.open(tar, "r:xz")
        tar.extractall(folder2)
        tar.close()
```
---------------
### Exécution dans l'environnement
+ Pour cette partie j'ai monté 2 fichier */proc* et */sys* avec la commande mount comme proposé dans le sujet :
```
    os.system('mount -tproc /proc /var/lib/box/base/proc')
    os.system('mount -tproc /proc /var/lib/box/base/sys')
```
- Et j'ai aussi utiliser mknod pour le fichier /dev/random :
```
    os.system('mknod /var/lib/box/base/dev/random c 1 8')
```
+ Ensuite j'ai utilisé chroot comme demander dans le sujet et un chdir pour venir à la racine :
```
    os.chroot(folder2)
    os.chdir('/')
```
- Pour finir j'ai configuré le réseau avec echo et nous avons fait un update ainsi qu'un upgrade pour tester :
```
    os.system("echo 'nameserver 8.8.8.8' > /etc/resolv.conf")
    os.system("apt update")
    os.system("apt upgrade")
```

### Configuration d'un environnement
+ Pour configurer l'environnement j'ai d'abord utilisé la library yaml mais d'abord j'ai installer pip ensuite pyyaml :
```
    os.system("sudo apt install python3-pip")
    os.system('pip3 install pyyaml')
```
 - Ensuite j'ai édité un fichier yml depuis mon fichier python :
```
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
```

 - Pour finir j'ai parser le fichier yml
```
    with open("mongo.yml", 'r') as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)
```

*Les print qui sont dans mon script me servais à faire des vérification.*
