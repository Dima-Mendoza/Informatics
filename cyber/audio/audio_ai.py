#!/usr/bin/env python3
import argparse
import os
import sys
import ffmpeg
from pydub import AudioSegment


def convert_video(input_path, output_path, resolution=None, bitrate=None, codec=None):
    """
    Конвертирует видеофайл в другой формат, с опциональными параметрами:
    - resolution: строка вида "WIDTHxHEIGHT", например "1280x720"
    - bitrate: строка вида "2M", "500k" и т.д.
    - codec: строка, например "h264", "hevc" (h265), "vp9"
    """
    if not os.path.isfile(input_path):
        print(f"Ошибка: входной файл {input_path} не найден.")
        return

    try:
        stream = ffmpeg.input(input_path)

        # Устанавливаем разрешение, если передано
        if resolution:
            width, height = resolution.split('x')
            stream = stream.filter('scale', width, height)

        # Устанавливаем кодек, если передан
        if codec:
            codec_map = {
                'h264': 'libx264',
                'h265': 'libx265',
                'hevc': 'libx265',
                'vp9': 'libvpx-vp9'
            }
            ffmpeg_codec = codec_map.get(codec.lower())
            if not ffmpeg_codec:
                print(f"Предупреждение: неизвестный кодек '{codec}', будет выбран по умолчанию.")
                ffmpeg_codec = None
        else:
            ffmpeg_codec = None

        # Собираем параметры вывода
        output_kwargs = {}
        if bitrate:
            output_kwargs['video_bitrate'] = bitrate
        if ffmpeg_codec:
            output_kwargs['vcodec'] = ffmpeg_codec

        # Запускаем конвертацию
        (
            ffmpeg
            .output(stream, output_path, **output_kwargs)
            .overwrite_output()
            .run(quiet=False)
        )
        print(f"Успешно: видео сохранено как {output_path}")

    except ffmpeg.Error as e:
        print("Ошибка при конвертации видео:", e.stderr.decode('utf8', errors='ignore'))
        sys.exit(1)


def convert_audio(input_path, output_path, bitrate=None, sample_rate=None):
    """
    Конвертирует аудиофайл в другой формат, с опциональными параметрами:
    - bitrate: строка вида "192k", "320k" и т.д.
    - sample_rate: частота дискретизации, например 44100, 48000 и т.д.
    """
    if not os.path.isfile(input_path):
        print(f"Ошибка: входной файл {input_path} не найден.")
        return

    try:
        audio = AudioSegment.from_file(input_path)
        export_kwargs = {}
        if bitrate:
            export_kwargs['bitrate'] = bitrate
        if sample_rate:
            export_kwargs['parameters'] = ["-ar", str(sample_rate)]
        audio.export(output_path, format=os.path.splitext(output_path)[1][1:], **export_kwargs)
        print(f"Успешно: аудио сохранено как {output_path}")

    except Exception as e:
        print("Ошибка при конвертации аудио:", str(e))
        sys.exit(1)


def extract_audio(input_path, output_path):
    """
    Извлекает аудиодорожку из видеофайла и сохраняет её в указанный аудиофайл.
    """
    if not os.path.isfile(input_path):
        print(f"Ошибка: входной файл {input_path} не найден.")
        return

    try:
        (
            ffmpeg
            .input(input_path)
            .output(output_path, vn=None, acodec='copy')
            .overwrite_output()
            .run(quiet=False)
        )
        print(f"Успешно: аудио извлечено в {output_path}")
    except ffmpeg.Error as e:
        print("Ошибка при извлечении аудио:", e.stderr.decode('utf8', errors='ignore'))
        sys.exit(1)


def merge_audio(input_files, output_path):
    """
    Объединяет несколько аудиофайлов (input_files: список путей) в один файл.
    Выходной формат определяется расширением output_path.
    """
    for f in input_files:
        if not os.path.isfile(f):
            print(f"Ошибка: аудиофайл {f} не найден.")
            return

    try:
        combined = AudioSegment.empty()
        for fpath in input_files:
            segment = AudioSegment.from_file(fpath)
            combined += segment
        combined.export(output_path, format=os.path.splitext(output_path)[1][1:])
        print(f"Успешно: объединённый аудио-файл сохранён как {output_path}")
    except Exception as e:
        print("Ошибка при объединении аудио:", str(e))
        sys.exit(1)


def info(input_path):
    """
    Выводит метаданные (кодеки, длительность, битрейт) для видео или аудио.
    """
    if not os.path.isfile(input_path):
        print(f"Ошибка: файл {input_path} не найден.")
        return

    try:
        probe = ffmpeg.probe(input_path)
        format_info = probe.get('format', {})
        print("=== Общая информация ===")
        print(f"Файл: {input_path}")
        print(f"Формат: {format_info.get('format_long_name', 'N/A')}")
        print(f"Длительность: {format_info.get('duration', 'N/A')} сек")
        print(f"Размер: {format_info.get('size', 'N/A')} байт")
        print(f"Битрейт: {format_info.get('bit_rate', 'N/A')} бит/с")
        print()
        print("=== Потоки ===")
        for stream in probe.get('streams', []):
            idx = stream.get('index')
            stype = stream.get('codec_type')
            codec = stream.get('codec_long_name')
            bitrate = stream.get('bit_rate', 'N/A')
            width = stream.get('width', 'N/A')
            height = stream.get('height', 'N/A')
            samplerate = stream.get('sample_rate', 'N/A')
            channels = stream.get('channels', 'N/A')
            print(f"[Stream #{idx}] Тип: {stype}")
            print(f"  Кодек: {codec}")
            if stype == 'video':
                print(f"  Разрешение: {width}x{height}")
                print(f"  Битрейт (прибл.): {bitrate}")
            elif stype == 'audio':
                print(f"  Частота дискрет.: {samplerate}")
                print(f"  Каналы: {channels}")
                print(f"  Битрейт (прибл.): {bitrate}")
            print()
    except ffmpeg.Error as e:
        print("Ошибка при получении информации:", e.stderr.decode('utf8', errors='ignore'))
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Конвертер медиафайлов (видео и аудио) через командную строку."
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Команда convert (для видео)
    convert_parser = subparsers.add_parser('convert', help="Конвертировать видеофайл")
    convert_parser.add_argument('input_file', help="Входной видеофайл")
    convert_parser.add_argument('output_file', help="Выходной видеофайл")
    convert_parser.add_argument('--resolution', help="Новое разрешение, например 1280x720", required=False)
    convert_parser.add_argument('--bitrate', help="Битрейт, например 2M", required=False)
    convert_parser.add_argument('--codec', help="Кодек: h264, h265 (hevc), vp9", required=False)

    # Команда convert-audio (для аудио)
    conv_audio_parser = subparsers.add_parser('convert-audio', help="Конвертировать аудиофайл")
    conv_audio_parser.add_argument('input_file', help="Входной аудиофайл")
    conv_audio_parser.add_argument('output_file', help="Выходной аудиофайл")
    conv_audio_parser.add_argument('--bitrate', help="Битрейт, например 192k", required=False)
    conv_audio_parser.add_argument('--sample-rate', help="Частота дискретизации, например 44100", type=int, required=False)

    # Команда extract-audio (извлечение аудио из видео)
    extract_parser = subparsers.add_parser('extract-audio', help="Извлечь аудио из видео")
    extract_parser.add_argument('input_file', help="Входной видеофайл")
    extract_parser.add_argument('output_file', help="Выходной аудиофайл")

    # Команда merge-audio (объединить несколько аудиофайлов)
    merge_parser = subparsers.add_parser('merge-audio', help="Объединить несколько аудиофайлов")
    merge_parser.add_argument('output_file', help="Выходной аудиофайл")
    merge_parser.add_argument('input_files', nargs='+', help="Список входных аудиофайлов для объединения")

    # Команда info (метаданные)
    info_parser = subparsers.add_parser('info', help="Показать информацию о медиафайле")
    info_parser.add_argument('input_file', help="Файл для анализа")

    args = parser.parse_args()

    if args.command == 'convert':
        convert_video(
            args.input_file,
            args.output_file,
            resolution=args.resolution,
            bitrate=args.bitrate,
            codec=args.codec
        )
    elif args.command == 'convert-audio':
        convert_audio(
            args.input_file,
            args.output_file,
            bitrate=args.bitrate,
            sample_rate=args.sample_rate
        )
    elif args.command == 'extract-audio':
        extract_audio(args.input_file, args.output_file)
    elif args.command == 'merge-audio':
        merge_audio(args.input_files, args.output_file)
    elif args.command == 'info':
        info(args.input_file)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
