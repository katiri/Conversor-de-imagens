from PIL import Image
import os

extensao = 'webp'

if not os.path.exists(f'convertidos/{extensao}'):
    os.makedirs(f'convertidos/{extensao}')

imagens = os.listdir('imagens')

for i in imagens:
    imagem = Image.open(f'imagens/{i}')
    ext = i.split('.')

    imagem.save(f'convertidos/{extensao}/{i.replace(ext[-1], extensao)}')