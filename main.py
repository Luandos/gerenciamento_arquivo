import datetime
import shutil
import pathlib

caminho_org = pathlib.Path("organizador")

# criando pastas
for arquivo in caminho_org.iterdir():
    cdir = pathlib.Path(f"pasta/subpasta{arquivo.suffix}")
    print(arquivo.name)
    print(cdir.suffix)
    if arquivo.suffix == cdir.suffix:
        cdir.mkdir(exist_ok=True, parents=True)

