import cv2
import numpy as np
import matplotlib.pyplot as plt
from utils import equalizacion_local

# Cargar la imagen en escala de grises
img = cv2.imread("Imagen_con_detalles_escondidos.tif", cv2.IMREAD_GRAYSCALE)

# Mostrar la imagen original
plt.imshow(img, cmap="gray")
plt.show()

# Aplicar equalización local con diferentes tamaños de ventana
img_eq_3x3 = equalizacion_local(img, (3, 3))
img_eq_7x7 = equalizacion_local(img, (7, 7))
img_eq_15x15 = equalizacion_local(img, (15, 15))
img_eq_31x31 = equalizacion_local(img, (31, 31))
img_eq_63x63 = equalizacion_local(img, (63, 63))

#Subplots para diferentes tamaños de ventana
fig, axs = plt.subplots(2, 3, figsize=(10, 8), sharex=True, sharey=True)
axs[0, 0].imshow(img, cmap="gray")
axs[0, 0].set_title("Original")
axs[0, 1].imshow(img_eq_3x3, cmap="gray")
axs[0, 1].set_title("Equalización Local 3x3")
axs[0, 2].imshow(img_eq_7x7, cmap="gray")
axs[0, 2].set_title("Equalización Local 7x7")
axs[1, 0].imshow(img_eq_15x15, cmap="gray")
axs[1, 0].set_title("Equalización Local 15x15")
axs[1, 1].imshow(img_eq_31x31, cmap="gray")
axs[1, 1].set_title("Equalización Local 31x31")
axs[1, 2].imshow(img_eq_63x63, cmap="gray")
axs[1, 2].set_title("Equalización Local 63x63")
plt.show()

# Aplicar equalización local con diferentes tamaños de ventana y background=True
img_eq_3x3_bg = equalizacion_local(img, (3, 3), background=True)
img_eq_7x7_bg = equalizacion_local(img, (7, 7), background=True)
img_eq_15x15_bg = equalizacion_local(img, (15, 15), background=True)
img_eq_31x31_bg = equalizacion_local(img, (31, 31), background=True)
img_eq_63x63_bg = equalizacion_local(img, (63, 63), background=True)

#Subplots con binary
fig, axs = plt.subplots(2, 3, figsize=(10, 8), sharex=True, sharey=True)
axs[0, 0].imshow(img, cmap="gray")
axs[0, 0].set_title("Original")
axs[0, 1].imshow(img_eq_3x3_bg, cmap="gray")
axs[0, 1].set_title("Equalización Local 3x3")
axs[0, 2].imshow(img_eq_7x7_bg, cmap="gray")
axs[0, 2].set_title("Equalización Local 7x7")
axs[1, 0].imshow(img_eq_15x15_bg, cmap="gray")
axs[1, 0].set_title("Equalización Local 15x15")
axs[1, 1].imshow(img_eq_31x31_bg, cmap="gray")
axs[1, 1].set_title("Equalización Local 31x31")
axs[1, 2].imshow(img_eq_63x63_bg, cmap="gray")
axs[1, 2].set_title("Equalización Local 63x63")
plt.show()
