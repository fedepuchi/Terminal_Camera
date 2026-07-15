import sys
import time 
import cv2

camara = cv2.VideoCapture(0)
CHARS = " .:-=+*#%@"
DOWNSCALE = 8

if not camara.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Preparar la terminal
sys.stdout.write('\033[?25l') 
sys.stdout.write('\033[2J')   

try:
    while True:
        success, frame = camara.read()
        if not success:
            print("Error: No se pudo leer el frame.")
            break
            
        hight, width, _ = frame.shape
        frame_ascii = ""
        
        for y in range(0, hight, DOWNSCALE * 2):
            fila_ascii = []
            for x in range(0, width, DOWNSCALE):
                # Usando tu lógica matemática original
                b, g, r = frame[y, x]
                brightness = (int(b) + int(g) + int(r)) // 3
                char_index = brightness * (len(CHARS) - 1) // 255
                
                fila_ascii.append(CHARS[char_index])
            
            # Unir la fila y agregar salto de línea
            frame_ascii += "".join(fila_ascii) + "\n"
            
        # Imprimir todo el frame de golpe
        sys.stdout.write('\033[H' + frame_ascii)
        sys.stdout.flush()
        
        time.sleep(0.03) 
        
except KeyboardInterrupt:
    pass
finally:
    # Limpiar al salir (Ctrl+C)
    sys.stdout.write('\033[?25h') 
    camara.release()