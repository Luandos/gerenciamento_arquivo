import shutil
from pathlib import Path
from datetime import datetime

pasta_organizada = Path("pastas_organizados")
reg_log = Path("registro.log")
arquivos_qtd = 0
ext_encontradas = list()

for arquivo in Path('organizador').iterdir():
    
    extensao = arquivo.suffix[1:]
    if extensao not in ext_encontradas:
        ext_encontradas.append(extensao)

    subpasta = pasta_organizada/extensao
    if not subpasta.exists():
        subpasta.mkdir(exist_ok=True, parents=True)
        
    shutil.copy(arquivo, subpasta/arquivo.name)
    with open(reg_log, 'a', encoding='utf-8') as log:
        agora = datetime.now()
        log.write(agora.strftime(f"%d/%m/%Y %H:%M:%S Movido o arquivo {arquivo.name} para a pasta {subpasta}\n"))
    arquivos_qtd += 1
print(f"{arquivos_qtd} arquivos foram organizados")
print("Extensões encontradas:")
for extensao in ext_encontradas:
    print(extensao)