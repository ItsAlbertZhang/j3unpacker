from pathlib import Path
import shutil

patchdir = Path('./patch')
for dir_remove in patchdir.iterdir():
    if dir_remove.is_dir():
        shutil.rmtree(dir_remove)

datdir = Path('./bin/dat')
for file_remove in datdir.iterdir():
    if file_remove.suffix == '.dat' or file_remove.suffix == '.idx':
        file_remove.unlink()

outfiledir = Path('./bin/outfile')
for file_remove in outfiledir.iterdir():
    if not file_remove.name == '.gitkeep' and not file_remove.is_dir():
        file_remove.unlink()