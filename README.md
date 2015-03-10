# jefferson
JFFS2 filesystem extraction tool


Dependencies
============

- `cstuct`

```bash
$ sudo pip install cstruct
```

Features
============
- Big/Little Endian support
- `JFFS2_COMPR_ZLIB`, `JFFS2_COMPR_RTIME` and `JFFS2_COMPR_NONE` compression support
- CRC checks - for now only enforced on `hdr_crc`
- Extraction of symlinks, directories and files
- Detection/handling of duplicate inode numbers. Occurs if multiple JFFS2 filesystems are found in one file and causes `jefferson` to treat segments as separate filesystems

Usage
============
```bash
$ jefferson filesystem.img -o outdir
```
