## Jefferson

JFFS2 filesystem extraction tool.

### Installation

You can install Jefferson from PyPi with the following command:

```
pip install --user jefferson
```

### Usage

```sh
jefferson filesystem.img -d outdir
```

### Features

- big-endian and little-endian support with auto-detection
- zlib, rtime, LZMA, and LZO compression support
- CRC checks - for now only enforced on `hdr_crc`
- extraction of symlinks, directories, files, and device nodes
- detection/handling of duplicate inode numbers. Occurs if multiple JFFS2 filesystems are found in one file and causes `jefferson` to treat segments as separate filesystems

### Development

The package is maintained with Poetry. If you want to contribute, we recommend you follow these steps:

```sh
git clone https://github.com/onekey-sec/jefferson.git
cd jefferson
poetry install
poetry run jefferson
```

You can install Poetry by following this [guide](https://python-poetry.org/dos/#installation)
