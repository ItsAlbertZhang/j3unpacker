from pathlib import Path
import os
import shutil

patchdir = Path('./patch')
ls = os.listdir(patchdir)
for filename in ls:
    dir_remove = patchdir / filename
    if dir_remove.is_dir():
        shutil.rmtree(dir_remove)

datdir = Path('./bin/dat')
ls = os.listdir(datdir)
for filename in ls:
    file_remove = datdir / filename
    if file_remove.suffix == '.dat' or file_remove.suffix == '.idx':
        os.remove(file_remove)

outfiledir = Path('./bin/outfile')
ls = os.listdir(outfiledir)
for filename in ls:
    file_remove = outfiledir / filename
    if not file_remove.name == '.gitkeep' and not file_remove.is_dir():
        os.remove(file_remove)