from PIL import Image, ImageDraw, ImageFont

def generate_image_pillow(width, height, path):
    """
    Создает изображение с использованием Pillow (PIL) и сохраняет его в файл PNG.
    """
    # 1. Создаем новое изображение
    img = Image.new("RGB", (width, height), "white")  # RGB, размер, цвет фона

    # 2. Создаем объект для рисования
    draw = ImageDraw.Draw(img)

    # 3. Рисуем элементы (примеры):
    # - Прямоугольник:
    draw.rectangle([(50, 50), (150, 100)], fill="blue", outline="black")  # Координаты, заливка, контур

    # - Окружность (эллипс):
    draw.ellipse([(200, 50), (250, 100)], fill="green", outline="black")

    # - Линия:
    draw.line([(50, 150), (150, 200)], fill="red", width=3)  # Координаты начала и конца, цвет, толщина

    # 4. Сохраняем изображение
    img.save(path)
# Пример использования:  # С