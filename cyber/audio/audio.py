from moviepy import VideoFileClip
import tkinter as tk
from tkinter import filedialog
import librosa
import soundfile as sf
import ffmpeg
from pydub import AudioSegment
from pydub.utils import mediainfo
from moviepy.video.io.ffmpeg_reader import FFMPEG_VideoReader

root = tk.Tk()
root.withdraw()

save_path = '/home/mendoza/Project/public/Informatics/cyber/audio'
ch = 1


while(ch!=0):
    print('\n', save_path)
    ch = int(input('1. Конвертировать видео в другой формат;\n2. Получить данные о видео;\n'
                   '3. Изменить разрешение видео и битрейт;\n4. Конвертировать аудио;\n'
                   '5. Объединить несколько аудиофайлов\n'
                   '6. Поменять битрейт и частоту дискретизации\n'
                   '7. Получить данные об аудиофайле\n'
                   '8. Выбрать папку сохранения;\n'))
    match ch:
        case 1:
            try:
                vid = filedialog.askopenfilename()
                v = VideoFileClip(vid)
                name = v.filename.split('.')[0]
                form = input('Введите формат видео: ')
                match form:
                    case 'mp4':
                        v.write_videofile(f'{name}.{form}', codec='libx265')
                    case 'mov':
                        v.write_videofile(f'{name}.{form}', codec='libx264')
                    case 'mkv':
                        v.write_videofile(f'{name}.{form}', codec='vp9')
                    case 'avi':
                        v.write_videofile(f'{name}.{form}', codec='mpeg4')
                v.close()
            except Exception as e:
                print('Что-то пошло не так ', e)
        case 2:
            try:
                vid = filedialog.askopenfilename()
                v = VideoFileClip(vid)
                meta = v.reader.infos
                print(f'Длина видео: {v.duration} сек.\n'
                    f'FPS: {v.fps}\n'
                    f'Разрешение: {v.size[0]}x{v.size[1]}\n'
                    f'Кол-во кадров: {v.n_frames}\n'
                    f'Полная информация: {meta}')
            except Exception as e:
                print('Что-то пошло не так ', e)
        case 3:
            try:
                vid = filedialog.askopenfilename()
                v = VideoFileClip(vid)
                size = [int(x) for x in input('Введите новый размер: ').split(' ')]
                bitrate = input('Введите битрейт: ')
                resized_video = v.resized((size[0], size[1]))
                resized_video.write_videofile(v.filename, bitrate=bitrate)
            except Exception as e:
                print('Что-то пошло не так: ', e)
        case 4:
            file = filedialog.askopenfilename()
            audio = AudioSegment.from_file(file, format=file.split('.')[1])
            form = input('Введите формат: ')
            name = input('Введите желаемое имя: ')
            audio.export(f'{save_path}/{name}.{form}',format=form)
            '''form = input('Введите формат: ')
            name = input('Введите желаемое имя: ')
            ad, sr = librosa.load(file, sr=None)
            sf.write(f'{save_path}/{name}.{form}', ad, sr, format=form)'''
        case 5:
            files = filedialog.askopenfiles(title='Выбрать аудио файлы...')
            name = input('Введите имя файла: ')
            form = input('Введите формат: ')
            combined = AudioSegment.empty()
            for f in files:
                o = f.name
                s = AudioSegment.from_file(o)
                combined+=s
            combined.export(f'{save_path}/{name}.{form}', format=form)
        case 6:
            file = filedialog.askopenfilename()
            aud = AudioSegment.from_file(file)
            name = input('Введите имя файла: ')
            form = input('Введите формат: ')
            dsc = int(input('Введите частоту дискретизации: '))
            bit = input('Введите битрейт: ')
            aud = (aud.set_frame_rate(dsc))
            aud.export(f'{save_path}/{name}.{form}', format=form, bitrate=bit)
        case 7:
            file = filedialog.askopenfilename()
            aud = AudioSegment.from_file(file)
            info = mediainfo(file)

            print(f'Частота дискретизации: {aud.frame_rate}\n'
                f'Каналы: {aud.channels}\n'
                f'Битрейт: {aud.inf}'
                f'Длительность (мс): {len(aud)}')
        case 8:
            save_path = filedialog.askdirectory(title='Выбрать папку для сохранения')