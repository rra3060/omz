import os
import shutil
import platform

#try:
    #os = platform.system() # Windows
    #os = platform.mac_vers() # macOS
    #os = platform.linux_distribution() # Linux
#except Exception:
    #pass

#if (os in 'Windows' or os in 'windows')
    #Absolute_directory_Windows = 
    #
#if (os in 'Linux' or os in 'linux')
    #Absolute_directory_Linux = 
    #
#if (os in 'Macos' or os in 'macos' or os in 'Darwin')
    #Absolute_directory_Macos = 
    #

!omz_downloader --print_all
model = input()
!omz_downloader --name {model} --precision FP16

default_directory = os.getcwd()

if (default_directory in 'intel' or public):

list_int = os.listdir(path=".")
text_length_int = len(os.listdir(path="."))

for i in range(text_length_int):
    if (list_int[i] != "model"):
        try:
            os.mkdir("model")
            list_int = os.listdir(path=".")
        except Exception:
            pass

os.chdir("model")
model_directory = os.getcwd()
os.chdir(default_directory)

try:
    for i in range (text_length_int):
        if (list_int[i] == "intel"):
            os.chdir("intel")
            path_int = os.getcwd()
    list_int_1 = os.listdir(path=".")
    text_length_int_1 = len(os.listdir(path="."))

    for i in range (text_length_int_1):
        if (list_int_1[i] == model):
            os.chdir(model)
            path_fac = os.getcwd()
    list_fac = os.listdir(path=".")
    text_length_fac = len(os.listdir(path="."))
    for i in range (text_length_fac):
        
        if (list_fac[i] == "FP16"):
            os.chdir("FP16")
            path_fac_FP = os.getcwd()
        
        elif (list_fac[i] == "FP32"):
            os.chdir("FP32")
            path_fac_FP = os.getcwd()
            
    list_fac_mod = os.listdir(path=".")
    text_length_fac_mod = len(os.listdir(path="."))
    shutil.move(model+'.bin',model_directory)
    shutil.move(model+'.xml',model_directory)
    os.chdir(default_directory)
    shutil.rmtree('intel')
except Exception:
    pass

try:
    for i in range (text_length_int):
        if (list_int[i] == "public"):
            os.chdir("public")
            path_int = os.getcwd()
    list_int_1 = os.listdir(path=".")
    text_length_int_1 = len(os.listdir(path="."))

    if (model != "gpt-2"):
        for i in range (text_length_int_1):
            if (list_int_1[i] == model):
                os.chdir(model)
                path_fac = os.getcwd()
        list_fac = os.listdir(path=".")
        text_length_fac = len(os.listdir(path="."))
        
        list_fac_mod = os.listdir(path=".")
        text_length_fac_mod = len(os.listdir(path="."))

        for i in range (text_length_fac_mod):
            move_dir = list_fac[i]
            shutil.move(move_dir, model_directory)
            
        os.chdir(default_directory)
        shutil.rmtree('public')
    else:
        for i in range (text_length_fac):
            move_dir = list_fac[i]
            shutil.move(move_dir, model_directory)
        os.chdir(default_directory)
        shutil.rmtree('public')
except Exception:
    pass
