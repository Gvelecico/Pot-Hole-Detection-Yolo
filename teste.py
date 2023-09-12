import cv2

# Abra o vídeo
video = cv2.VideoCapture('GL011244.mp4')  # Substitua 'seu_video.mp4' pelo caminho do seu arquivo de vídeo

while True:
    ret, frame = video.read()  # Lê o próximo quadro do vídeo

    # Obtenha o tempo atual do vídeo em segundos
    current_time_seconds = video.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

    # Exiba o tempo atual em segundos
    print(f'Tempo atual do vídeo: {current_time_seconds:.2f} segundos')
    
    #if(current_time_seconds > 20):
    #    break
