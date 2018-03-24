# -*- coding: utf-8 -*-
import os
import re
import pytube
import subprocess


def printSeparator():
    print("")
    print("  .--.      .--.      .--.      .--.      .--.      .--.      .--.      .--. ")
    print(":::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\ ")
    print("'      `--'      `--'      `--'      `--'      `--'      `--'      `--'      `- ")
    print("")


def finishArt():
    print("Y ya estaría, amigos. Fácil, sencillo, y para toda la familia")
    print("¡Hasta la próxima!\n")


def startDownloadArt():
    print("(/•-•)/ Vídeo descargado \(•-•\)\n")
    print(" .''.    .'', ")
    print(" |  |   /  / ")
    print(" |  |  /  / ")
    print(" |  | /  / ")
    print(" |  |/  ;-._  ")
    print(" }  ` _/  / ; ")
    print(" |  /` ) /  / ")
    print(" | /  /_/\_/\ ")
    print(" |/  /      | ")
    print(" (  ' \ '-  | ")
    print("  \    `.  / ")
    print("   |      | ")
    print("   |      | ")
    print("\nVamos a cortarlo... ( •_•)   ( •_•)>⌐■-■   (⌐■_■)")


def getTimestampsArt():
    print("                                   ,   /\   ,                                    ")
    print("                                  / '-'  '-' \                                   ")
    print("                                  |  GUARDIA |                                   ")
    print("                                  |   CIVIL  |                                   ")
    print("                                  |   .--.   |                                   ")
    print("                                  |  ( 42 )  |                                   ")
    print("                                  \   '--'   /                                   ")
    print("                                   '--.  .--'                                    ")
    print("                                       \/                                        ")
    print("===================================== AVISO =====================================")
    print("|| La 'veracidad' de las marcas NO serán comprobadas. Es decir, que el usuario ||")
    print("|| es último responsable, y único, de introducirlas en el orden correcto       ||")
    print("||                                                                             ||")
    print("|| En NINGÚN momento se realizará ningún tipo de comprobación para saber si la ||")
    print("|| última marca introducida es menor que otra anterior y problemas similares.  ||")
    print("||                                                                             ||")
    print("|| Esta advertencia aplica también a la duración total del vídeo               ||")
    print("===================================== AVISO =====================================\n")


def evaluateInput(input):
    validInput = False
    itemMatchsHour = re.match("^[0-9]{2}:[0-9]{2}:[0-9]{2}$", input, 0)
    if itemMatchsHour:
        validInput = True
    return validInput


def getAllAudios(dir):
    ffmpegdir = "ffmpeg"
    l = os.listdir(dir)
    li = [x.split('.')[0] for x in l]
    ab = "160k"
    ac = "2"
    ar = "44100"
    for file in li:
        i = dir + "/" + file + ".mp4"
        vnwav = dir + "/" + file + ".wav"
        vnmp = dir + "/" + file + ".mp3"
        cmdwav = [ffmpegdir + "/ffmpeg.exe", "-i", i,
                  "-ab", ab, "-ac", ac, "-ar", ar, "-vn", vnwav]
        FNULL = open(os.devnull, 'w')
        subprocess.run(cmdwav, stdout=FNULL, stderr=subprocess.STDOUT)
        FNULL.close()
        cmdmp = [ffmpegdir + "/ffmpeg.exe", "-i", i,
                 "-ab", ab, "-ac", ac, "-ar", ar, "-vn", vnmp]
        FNULL = open(os.devnull, 'w')
        subprocess.run(cmdmp, stdout=FNULL, stderr=subprocess.STDOUT)
        FNULL.close()
    print("...y ya está, máquina")
    fullList = os.listdir(dir)
    for file in fullList:
        os.rename(str(dir + "/" + file),
                  str(dir + "/" + file.replace("_", " ")))


def clearDir(dir):
    os.remove(dir + "/timestamps.txt")
    os.remove(dir + "/timestampsAux.txt")
    os.remove(dir + "/names.txt")
    os.remove(dir + "/cuts.txt")
    os.remove(dir + "/original.mp4")
    print("Vale, pues el corte ya estaría, ahora habría que extraer los audios.")
    print("Se van a pasar a .wav y a .mp3, a lo mejor tarda un rato.")


def getParts(dir):
    ffmpegdir = "ffmpeg"
    with open(dir + "/cuts.txt") as f:
        all = f.readlines()
        first = all[:int(len(all) / 2)]
        second = all[int(len(all) / 2):]
        for line in first:
            filename, start, end = line.strip().split(' ')
            cmd = [ffmpegdir + "/ffmpeg.exe", "-i", dir + "/original.mp4",
                   "-ss", start, "-to", end, "-c", "copy", filename]
            FNULL = open(os.devnull, 'w')
            subprocess.run(cmd, stdout=FNULL, stderr=subprocess.STDOUT)
            FNULL.close()
        for line in second:
            filename, start, end = line.strip().split(' ')
            cmd = [ffmpegdir + "/ffmpeg.exe", "-i", dir + "/original.mp4",
                   "-ss", start, "-to", end, "-c", "copy", filename]
            FNULL = open(os.devnull, 'w')
            subprocess.run(cmd, stdout=FNULL, stderr=subprocess.STDOUT)
            FNULL.close()


def cutIntoPieces(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        if ".mp4" in filename:
            os.rename(str(dir + "/" + filename), dir + "/original.mp4")
    listNames = list(open(dir + "/names.txt"))
    listTimestamps = list(open(dir + "/timestampsAux.txt"))
    cf = dir + "/cuts.txt"
    cortesFile = open(cf, "w")
    x = 0
    while x < len(listNames):
        tmp = dir + "/" + \
            listNames[x].strip() + " " + listTimestamps[x].strip() + \
            " " + listTimestamps[x + 1].strip()
        cortesFile.write(tmp + "\n")
        x += 1
    cortesFile.close()


def startDownload(url, dir):
    yt = pytube.YouTube(url)
    options = yt.get_videos()
    x = 0
    for o in options:
        print(str(x) + ". " + str(o))
        x += 1
    condition = True
    while (condition):
        num_input = int(input("\nEscribe el número de la opción deseada: "))
        o = options[num_input]
        if ".mp4" in str(o):
            condition = False
        else:
            print("\n¯\_(•_•)_/¯ Esa opción no es .mp4, amigo, tal vez te has equivocado, inténtalo otra vez ¯\_(•_•)_/¯")
    vid = options[num_input]
    print("Vamos a ello... por favor, espera")
    vid.download(dir)
    printSeparator()
    startDownloadArt()


def getTimestampNames(dir):
    fi = dir + "/timestamps.txt"
    with open(fi) as f:
        lines = f.read().splitlines()
    f = dir + "/names.txt"
    namesFile = open(f, "w")
    x = 0
    printSeparator()
    print("Hay que introducir " + str((len(lines) + 1)) +
          " nombres, para todas las partes del vídeo")
    if len(lines) > 0:
        while x <= len(lines):
            print("")
            if x == 0:
                print("Desde el principio hasta " + lines[x])
            else:
                if x == len(lines):
                    print("De " + lines[x - 1] + " hasta el final")
                else:
                    print("De " + lines[x - 1] + " a " + lines[x])
            x += 1
            name = input("¿Nombre del fragmento?: ")
            name = name.replace(" ", "_")
            namesFile.write(name + ".mp4" + "\n")
    else:
        print("\nUn momento... ¿Cómo que un solo nombre?")
        print("Eso es que no has puesto marcas de tiempo.")
        print("\nLo siento, pero no voy a descargar el vídeo como tal, en una sola parte.")
        print("Para eso ya hay miles de opciones, máquina. (⌐■_■)")
        return 0
    namesFile.close()
    return 1


def getTimestamps(dir):
    f = dir + "/timestamps.txt"
    fa = dir + "/timestampsAux.txt"
    timestampsFile = open(f, "w")
    timestampsFileAux = open(fa, "w")
    timestampsFileAux.write("00:00:00\n")
    getTimestampsArt()
    exitLoop = True
    while(exitLoop):
        inputValue = input(
            "Marca de tiempo en formato 'hh:mm:ss' // 'x' para salir: ")
        if inputValue == "x":
            exitLoop = False
            exitDuration = True
            while(exitDuration):
                duration = input("\nDuración total en formato 'hh:mm:ss': ")
                if evaluateInput(duration):
                    timestampsFileAux.write(duration)
                    exitDuration = False
                else:
                    print("Formato inválido, asegúrate de cumplir este: 'hh:mm:ss'\n")
        else:
            if evaluateInput(inputValue):
                timestampsFile.write(inputValue + "\n")
                timestampsFileAux.write(inputValue + "\n")
                print("Marca '" + inputValue + "' introducida\n")
            else:
                print("Formato inválido, asegúrate de cumplir este: 'hh:mm:ss'\n")
    timestampsFile.close()
    timestampsFileAux.close()


printSeparator()
id = input("Completa la url con el ID del vídeo: https://www.youtube.com/watch?v=")
url = "https://www.youtube.com/watch?v=" + id

dirExists = True
while (dirExists):
    dir_filename = input("\nNombre del directorio contenedor: ")
    dir_filename = dir_filename.replace(" ", "_")
    if os.path.exists(dir_filename):
        print(" ¯\(°_o)/¯ Buen intento pero esa carpeta ya existe, fiera")
    else:
        dirExists = False


os.makedirs(dir_filename)
print("Directorio '" + dir_filename + "' creado")
printSeparator()

getTimestamps(dir_filename)
num = getTimestampNames(dir_filename)
if num == 1:
    printSeparator()

    startDownload(url, dir_filename)
    printSeparator()

    cutIntoPieces(dir_filename)
    getParts(dir_filename)
    clearDir(dir_filename)

    getAllAudios(dir_filename)
    printSeparator()
    finishArt()
