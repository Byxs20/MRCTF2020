import os
import zipfile


zip_name = "0573.zip"
password = "0573"
zips_path = "./zips"
flag_path = "./flag"

while True:
    zip = zipfile.ZipFile(zip_name, "r")
    file_name = zip.namelist()[0]
    suffix_name = zip.namelist()[0].split(".")[1]
    
    if suffix_name == "zip":
        zip.extractall(zips_path, pwd=password.encode())
    else:
        zip.extractall(flag_path)
        exit()
    
    zip_name = os.path.join(zips_path, file_name)
    password = zip.namelist()[0].split(".")[0]