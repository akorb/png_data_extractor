## What it does

The PNG format is essentially a container combining picture metadata (like resolution), with a payload, i.e., the picture data, which is always a zlib stream.

This tool extracts the payload. The resulting byte stream is usually a zlib stream, at least for a benign PNG picture.

The payload chunks within the PNG are identified by the tag `IDAT`.
The four bytes in front of it define the length of the chunk.

## Use cases

Probably just for experimenting, and CTF challenges.

## Usage

### Extract plain data

```shell
python3 png_data_extractor.py.py picture.png > picture.bin
```

### Extract data and decompress

Uses [zlib-flate](https://www.mankier.com/1/zlib-flate) from the [qpdf](https://github.com/qpdf/qpdf) package.

```shell
python3 png_data_extractor.py.py picture.png | zlib-flate -uncompress > picture.uncompressed.bin
```
