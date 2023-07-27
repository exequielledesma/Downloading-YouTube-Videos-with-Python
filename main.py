from pytube import YouTube

url = 'https://www.youtube.com/watch?v=pUgSdI0uXFQ'

video = YouTube(url)

print(f'Título: {video.title}')
print(f'Duración: {video.length} segundos')


stream = video.streams.get_highest_resolution()

stream.download(output_path=(str('/Videos-py')))

print('Descarga completada')
