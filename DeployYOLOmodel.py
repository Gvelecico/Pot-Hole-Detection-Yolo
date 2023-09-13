import torch
import numpy as np
import cv2
import pafy
from time import time
import yolov5
import cv2
import torch
import LocationVideo


#Nome do arquivo Json gerado pelo site
#https://goprotelemetryextractor.com/free/
#nameJsonVideo = 'C:\\Users\zgvele\\Desktop\\TCC\\videos\json\\GL011244_1_GPS5.json'

#locationVideo = LocationVideo.LocationVideo(nameJsonVideo)

#locationVideo.formatJson()
# Para buscar a localização usar a função: locationVideo.getLocation('0:0:30')

model = torch.hub.load('ultralytics/yolov5', 'custom', path= 'C:\\Users\\gvele\\Desktop\\TCC\Modelo de IA\\best.pt')

cap = cv2.VideoCapture('C:\\Users\\gvele\\Desktop\TCC\\videos\\video02.mp4')

target_label = 'pot-holes'

start_times = []  # Inicializar uma lista para armazenar os tempos

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar a detecção de objetos no frame
    results = model(frame)

    # Verificar se o rótulo de interesse está presente nos resultados
    if target_label in results.names:
        current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 60000.0  # Converter para minutos
        print(current_time)
        labels = results.names[target_label]
        for label, confidence, bbox in zip(*results.pred[target_label][0].detach().cpu().numpy()):
            if confidence > 0.5:  # Ajuste o limiar de confiança conforme necessário
                start_times.append(current_time)

    # Processar e exibir os resultados no frame
    output_frame = results.render()[0]

    # Exibir o frame com as detecções
    cv2.imshow('YOLOv5 Object Detection', output_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



if start_times:
    print(f"O rótulo '{target_label}' foi detectado nos seguintes minutos:")
    for time in start_times:
        print(f"{time:.2f} minutos")
else:
    print(f"O rótulo '{target_label}' não foi detectado no vídeo.")
