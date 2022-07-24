from genericpath import isdir
from pathlib import Path
import zipfile
import shutil


def unzip_patchfile():
    patchdir = Path('./patch')
    for f in patchdir.iterdir():
        if f.exists() and not f.is_dir() and not '.gitkeep' == f.name:
            unzipdir = f.stem
            key = '-to-1.0.0.'
            p = unzipdir.find(key)
            unzipdir = unzipdir[p-4:p] + '-' + unzipdir[p+len(key):p+len(key)+4]
            unzipdir = patchdir / unzipdir
            with zipfile.ZipFile(f, 'r') as zip_ref:
                zip_ref.extractall(unzipdir)


def movedat():
    path_dat = Path('./bin/dat')
    path_patch = Path('./patch')
    for path_patch_version in path_patch.iterdir():
        # patch_version: ./patch/1000-1001 等
        if path_patch_version.is_dir():
            path_id_parent = path_patch_version / 'updatepack' / 'pakv4'
            # path_id_parent: ./patch/1000-1001/updatepack/pakv4
            path_id_parent = path_id_parent.iterdir().__next__()
            # path_id_parent: ./patch/1000-1001/updatepack/pakv4/1000-1001(1.0.0.1000-1.0.0.1001).update
            for path_id in path_id_parent.iterdir():
                # path_id: ./patch/1000-1001/updatepack/pakv4/1000-1001(1.0.0.1000-1.0.0.1001).update/0 等
                if path_id.is_dir():
                    for path_datfile in path_id.iterdir():
                        # path_datfile: ./patch/1000-1001/updatepack/pakv4/1000-1001(1.0.0.1000-1.0.0.1001).update/0/000.dat 等
                        if path_datfile.exists() and path_datfile.suffix == '.dat':
                            shutil.move(path_datfile, path_dat / (path_patch_version.name + '_' + path_id.name + '_' + path_datfile.name))
                            shutil.move(path_id / (path_datfile.stem + '.idx'), path_dat / (path_patch_version.name + '_' + path_id.name + '_' + path_datfile.stem + '.idx'))


if '__main__' == __name__:
    unzip_patchfile()
    movedat()
