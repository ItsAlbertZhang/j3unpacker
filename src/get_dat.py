from pathlib import Path
import os
import zipfile
import shutil


def unzip_patchfile():
    patchdir = Path('./patch')
    ls = os.listdir(patchdir)
    for filename in ls:
        f = patchdir / filename
        if not '.gitkeep' == filename and not f.is_dir() and f.exists():
            unzipdir = f.stem
            key = '-to-1.0.0.'
            p = unzipdir.find(key)
            unzipdir = unzipdir[p-4:p] + '-' + unzipdir[p+len(key):p+len(key)+4]
            unzipdir = patchdir / unzipdir
            with zipfile.ZipFile(f, 'r') as zip_ref:
                zip_ref.extractall(unzipdir)


def movedat():
    datdir = Path('./bin/dat')
    patchdir = Path('./patch')
    ls_patchdir = os.listdir(patchdir)
    # ls_patchdir: ['1000-1001', '1001-1002']
    for patchname in ls_patchdir:
        d = patchdir / patchname
        # d: ./patch/1000-1001
        if d.is_dir():
            d = d / 'updatepack' / 'pakv4'
            # d: ./patch/1000-1001/updatepack/pakv4
            d = d / os.listdir(d)[0]
            ls_d = os.listdir(d)
            # ls_d: ['0', '000', '001']
            for id in ls_d:
                iddir = d / id
                # iddir: ./patch/1000-1001/updatepack/pakv4/0
                if iddir.is_dir():
                    ls_dat = os.listdir(iddir)
                    # ls_dat: ['000.dat', '000.idx', '001.dat', '001.idx', 'Apatch.list'...]
                    for filename in ls_dat:
                        file_moved = iddir / filename
                        # file_moved: ./patch/1000-1001/updatepack/pakv4/0/000.dat
                        # 或: ./patch/1000-1001/updatepack/pakv4/0/000.idx
                        if file_moved.exists() and file_moved.suffix == '.dat':
                            shutil.move(file_moved, datdir / (patchname + '_' + id + '_' + file_moved.name))
                            shutil.move(iddir / (file_moved.stem + '.idx'), datdir / (patchname + '_' + id + '_' + file_moved.stem + '.idx'))


if '__main__' == __name__:
    unzip_patchfile()
    movedat()