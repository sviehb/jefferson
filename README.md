## Jefferson

JFFS2 filesystem extraction tool

### Installation

Follow these steps on Debian based systems (Debian, Ubuntu, Kali, ...) to perform a system-wide installation of jefferon:

```bash
git clone https://github.com/sviehb/jefferson.git
cd jefferson
sudo apt update
sudo apt python3-pip liblzo2-dev
sudo python3 -m pip install -r requirements.txt
sudo python3 setup.py install
```


### Features

- big-endian and little-endian support with auto-detection
- zlib, rtime, LZMA, and LZO compression support
- CRC checks - for now only enforced on `hdr_crc`
- extraction of symlinks, directories, files, and device nodes
- detection/handling of duplicate inode numbers. Occurs if multiple JFFS2 filesystems are found in one file and causes `jefferson` to treat segments as separate filesystems

### Usage

```bash
$ jefferson filesystem.img -d outdir
```
