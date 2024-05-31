from PIL import Image, ImageDraw, ImageFont

# Crear una imagen en blanco
image = Image.new('RGB', (200, 100), color = (73, 109, 137))

# Inicializar el objeto para dibujar
draw = ImageDraw.Draw(image)

# Configurar la fuente (puede que necesites especificar una ruta a una fuente válida en tu sistema)
# font = ImageFont.truetype('arial.ttf', 15)
font = ImageFont.load_default()

# Añadir texto a la imagen
draw.text((10, 10), "Hola, PIL!", font=font, fill=(255, 255, 255))

# Guardar la imagen
image.save('desarrollador.png')
