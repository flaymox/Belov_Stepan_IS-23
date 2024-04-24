class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution
        print(f"Разрешение изображения {self.title} изменено на {self.resolution}")

    def title_upper(self):
        self.title = self.title.upper()
        print(f"Имя файла изменено на верхний регистр: {self.title}")


# Создание нескольких экземпляров класса Image с передачей аргументов
image1 = Image("1920x1080", "image1", "jpg")
image2 = Image("1280x720", "image2", "png")
image3 = Image("800x600", "image3", "jpeg")

# Вызов метода resize для каждого изображения
image1.resize("800x600")
image2.resize("640x480")
image3.resize("1024x768")

# Вызов метода title_upper для каждого изображения
image1.title_upper()
image2.title_upper()
image3.title_upper()
