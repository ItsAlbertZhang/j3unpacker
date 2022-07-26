from pathlib import Path
import zstd


def data_handle(path_dat: Path, path_idx: Path):
    path_outfiledir = Path('./bin/outfile')
    print(path_dat)
    dat = open(path_dat, 'rb')
    idx = open(path_idx, 'rb')
    # 确定dat文件中含有的文件数量
    idx.seek(0, 2)
    filenum = int((idx.tell() - 0x10) / 0x1F)
    idx.seek(0, 0)
    # 开始处理 idx 文件
    for i in range(filenum):
        idx.seek(0x10 + i * 0x1F, 0)
        dat_offset = int.from_bytes(idx.read(8), 'little')
        dat_size = int.from_bytes(idx.read(4), 'little')
        dat_type = int.from_bytes(idx.read(2), 'little')
        dat_check = idx.read(17)
        print(dat_offset, dat_size, dat_type, dat_check)
        dat.seek(dat_offset, 0)
        dat.seek(0x17, 1)
        data = dat.read(dat_size)
        try:
            # plaintext = zstd.ZSTD_uncompress(data)
            plaintext = zstd.ZSTD_uncompress(data).decode('gbk').encode('utf-8')
            path_outfile = path_outfiledir / (f'{path_dat.stem}_{"{:08X}".format(dat_offset)}')
            with open(path_outfile, 'wb') as f_out:
                f_out.write(plaintext)
        except:
            pass


def get_outfile():
    path_datdir = Path('./bin/dat')
    for path_datfile in path_datdir.iterdir():
        if path_datfile.suffix == '.dat':
            path_idxfile = path_datfile.with_suffix('.idx')
            if path_datfile.exists() and path_idxfile.exists():
                data_handle(path_datfile, path_idxfile)


if '__main__' == __name__:
    get_outfile()
