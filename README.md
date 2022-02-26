# jefferson
JFFS2 filesystem extraction tool

Installation
============
```bash
$ sudo python3 setup.py install
```


Dependencies
============
- `cstruct`

```bash
$ sudo pip3 install -r requirements.txt
```

Features
============
- Big/Little Endian support
- zlib, rtime, LZMA, and LZO compression support
- CRC checks - for now only enforced on `hdr_crc`
- Extraction of symlinks, directories, files, and device nodes
- Detection/handling of duplicate inode numbers. Occurs if multiple JFFS2 filesystems are found in one file and causes `jefferson` to treat segments as separate filesystems

Usage
============
```bash
$ jefferson filesystem.img -d outdir
```
