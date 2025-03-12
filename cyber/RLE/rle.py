import argparse
import os

def rle_compress(data):
    compressed = []
    i = 0
    n = len(data)
    
    while i < n:
        if i + 1 < n and data[i] == data[i + 1]:
            count = 1
            while i + count < n and data[i] == data[i + count] and count < 127:
                count += 1
            compressed.append(0b10000000 | count)
            compressed.append(data[i])
            i += count
        else:
            count = 1
            while i + count < n and data[i + count] != data[i + count - 1] and count < 127:
                count += 1
            compressed.append(count)
            compressed.extend(data[i:i + count])
            i += count
    
    return bytes(compressed)


def rle_decompress(data):
    decompressed = []
    i = 0
    n = len(data)
    
    while i < n:
        count = data[i] & 0x7F
        if data[i] & 0x80:
            value = data[i + 1]
            decompressed.extend([value] * count)
            i += 2
        else:
            decompressed.extend(data[i + 1:i + 1 + count])
            i += 1 + count
    
    return bytes(decompressed)


def compress_file(input_filename, output_filename):
    with open(input_filename, 'rb') as f:
        data = f.read()
    
    compressed_data = rle_compress(data)
    
    with open(output_filename, 'wb') as f:
        f.write(compressed_data)

    print(f"Файл {input_filename} успешно сжат в {output_filename}.")


def decompress_file(input_filename, output_filename):
    with open(input_filename, 'rb') as f:
        data = f.read()
    
    decompressed_data = rle_decompress(data)
    
    with open(output_filename, 'wb') as f:
        f.write(decompressed_data)

    print(f"Файл {input_filename} успешно разжат в {output_filename}.")


def main():
    parser = argparse.ArgumentParser(description="RLE Compressor/Decompressor")
    subparsers = parser.add_subparsers(dest='command')

    compress_parser = subparsers.add_parser('compress', help="Сжать файл")
    compress_parser.add_argument('input_file', help="Входной файл для сжатия")
    compress_parser.add_argument('output_file', help="Выходной файл для сжатия")

    decompress_parser = subparsers.add_parser('decompress', help="Разжать файл")
    decompress_parser.add_argument('input_file', help="Входной файл для разжатия")
    decompress_parser.add_argument('output_file', help="Выходной файл для разжатия")

    args = parser.parse_args()

    if args.command == 'compress':
        compress_file(args.input_file, args.output_file)
    elif args.command == 'decompress':
        decompress_file(args.input_file, args.output_file)
    else:
        print("Неизвестная команда. Используйте 'compress' или 'decompress'. Пример: python rle.py compress info.md info.rle | python rle.py decompress info.rle info.md")

if __name__ == '__main__':
    main()
