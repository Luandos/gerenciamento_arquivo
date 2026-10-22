import datetime
import shutil
import pathlib
import datetime

cont = 0
lista_ext=[]
rglog = pathlib.Path("registro.log")
rglog.touch()
shutil.unpack_archive("organizador.zip", "organizador")
caminho_org = pathlib.Path("organizador")

# criando pastas
for arquivo in caminho_org.iterdir():
    cdir = pathlib.Path(f"pasta/subpasta{arquivo.suffix}")
    print(arquivo.name)
    print(cdir.suffix)
    if arquivo.suffix == cdir.suffix:
        cdir.mkdir(exist_ok=True, parents=True)

# Movendo arquivos
for arquivo in caminho_org.iterdir():
    cfile = pathlib.Path(arquivo)
    cdir = pathlib.Path(f"pasta/subpasta{arquivo.suffix}")
    cf = str(cfile)
    cd = str(cdir)
    if arquivo.suffix == cdir.suffix:
        print("cf =", cf)
        print("cd =", cd)
        print("cfile =", cfile)
        print("cdir =", cdir)
        print("arquvo = ", arquivo.name)
        print("cf in cd =", cf in cd)
        print("Nomezao = ", cdir/arquivo.name )
        if not ((cdir/arquivo.name).exists):
            shutil.move(cfile, cdir)
    cont += 1
    if not arquivo.suffix in lista_ext:
        lista_ext.append(arquivo.suffix)
    reg = open("registro.log")
    with open("registro.log", 'a', encoding='utf-8') as reg:
        hora = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
        reg.write(f"{hora}, {arquivo.name} to {cdir.name} \n")
print(cont)
print(lista_ext)