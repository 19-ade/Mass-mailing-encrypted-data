import os
import subprocess
import sys


def install(package):
    os.system("pip install " + str(package))
    reqs = subprocess.check_output([sys.executable, "-m", "pip", "show", str(package)])

    print(str(reqs) + "\n")
    print("Installed " + package.upper() + "\n")


install("secure-smtplib")
install("PyPDF2")
install("openpyxl")
install("gTTS")
install("playsound")
