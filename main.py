import datetime
import shutil
import pathlib

caminho_org = pathlib.Path("organizador")
for arquivo in caminho_org.iterdir():
    print(arquivo.name)