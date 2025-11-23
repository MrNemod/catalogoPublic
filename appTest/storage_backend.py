import io
import requests
from PIL import Image
from django.core.files.storage import Storage
from django.conf import settings

class ImageKitStorage(Storage):
    upload_url = "https://upload.imagekit.io/api/v1/files/upload"

    def _save(self, name, content):

        # 🔹 Abrir la imagen original con Pillow
        image = Image.open(content)

        # 🔹 Convertir a WebP en memoria
        buffer = io.BytesIO()
        image.save(buffer, format="WEBP", quality=60)
        buffer.seek(0)

        # 🔹 Cambiar extensión del archivo
        new_name = name.rsplit(".", 1)[0] + ".webp"

        # Payload a ImageKit
        files = {
            "file": (new_name, buffer.getvalue()),
        }
        data = {
            "fileName": new_name,
            "folder": settings.IMAGEKIT_FOLDER,
        }

        # Subir a ImageKit
        response = requests.post(
            self.upload_url,
            files=files,
            data=data,
            auth=(settings.IMAGEKIT_PRIVATE_KEY, ""),
        )

        if response.status_code != 200:
            raise Exception("Error subiendo a ImageKit: " + response.text)

        result = response.json()

        # Regresar la URL del archivo WebP
        return result["url"]

    def url(self, name):
        return name

    def exists(self, name):
        return False
