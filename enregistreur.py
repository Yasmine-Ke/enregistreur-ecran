import mss
import cv2
import time
import numpy as np  # Importation de numpy

# Définir le chemin pour sauvegarder les captures
output_folder = "./captures/"

# Durée de l'enregistrement en secondes
duration = 10

# Capture d'écran avec mss
with mss.mss() as sct:
    # Définir la région de capture (ici, capture complète de l'écran)
    monitor = sct.monitors[0]  # Capture tout l'écran

    # Enregistrer les captures
    start_time = time.time()
    frame_count = 0
    while time.time() - start_time < duration:
        # Capture la capture d'écran
        screenshot = sct.grab(monitor)

        # Convertir l'image en format OpenCV
        img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        # Enregistrer chaque capture
        frame_filename = f"{output_folder}screenshot_{frame_count}.png"
        cv2.imwrite(frame_filename, img)

        # Incrémenter le compteur
        frame_count += 1
        time.sleep(0.1)  # Attente pour limiter la fréquence (ex : capture toutes les 0.1 secondes)

    print(f"Terminé. {frame_count} images sauvegardées.")
