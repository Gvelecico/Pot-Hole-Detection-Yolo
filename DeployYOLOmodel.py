import torch
import cv2
from time import time
import cv2
import LocationVideo
import os
import math
import LocationsSQL

dictionary_location = {}

#Nome do arquivo Json gerado pelo site
#https://goprotelemetryextractor.com/free/
nameVideo = 'GL011255'
nameModelo = 'best'

locationsSQL = LocationsSQL()
locationVideo = LocationVideo.LocationVideo(nameVideo)

locationVideo.formatJson()

model = torch.hub.load('ultralytics/yolov5', 'custom', path= os.path.dirname(os.path.realpath(__file__)) + '\\modelo\\' + nameModelo + '.pt')

cap = cv2.VideoCapture(os.path.dirname(os.path.realpath(__file__)) + '\\videos\\' + nameVideo + '.mp4')

target_label = 'pot-holes'

while True:
    
    ret, frame = cap.read()
    
    if not ret:
        break

    # Realizar a detecção de objetos no frame
    results = model(frame)

    for result in results.names:
        # Verificar se o rótulo de interesse está presente nos resultados
        if target_label == results.names[result]:
            labels = results.names[result]
            if(len(results.pred[result].detach().cpu().numpy()) > 0):
                
                    # Identifica caso a acurácia seja > 70% 
                    if results.pred[result].detach().cpu().numpy()[0][4] > 0.7:
                        
                        # Busca os segundos do vídeo 
                        second = math.ceil(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0)
                        
                        # Adiciona no dicionário a latitude e longitude
                        dictionary_location[second] = locationVideo.getLocationBySecond(second)

    # Processar e exibir os resultados no frame
    output_frame = results.render()[0]

    # Exibir o frame com as detecções
    cv2.imshow('YOLOv5 Object Detection', output_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(dictionary_location)