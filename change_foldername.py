import os
d = "C:\Dokumenty\Ksiazki\DyskMega"
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        new_path = os.path.join(d, path.replace("%", " "))
        os.rename(full_path, new_path)