import requests
from django.core.files.storage import Storage
from django.conf import settings

class ImageKitStorage(Storage):
    upload_url = "https://upload.imagekit.io/api/v1/files/upload"

    def _save(self, name, content):
        # Leer el archivo en memoria
        file_bytes = content.read()

        # Construir payload para ImageKit
        files = {
            "file": (name, file_bytes),
        }
        data = {
            "fileName": name,
            "folder": settings.IMAGEKIT_FOLDER,
        }

        # Llamar a la API
        response = requests.post(
            self.upload_url,
            files=files,
            data=data,
            auth=(settings.IMAGEKIT_PRIVATE_KEY, ""),
        )

        if response.status_code != 200:
            raise Exception("Error subiendo a ImageKit: " + response.text)

        result = response.json()

        # Regresar la URL completa del archivo que Django almacenará
        return result["url"]

    def url(self, name):
        # Como name es la URL completa, la devolvemos tal cual
        return name

    def exists(self, name):
        # Siempre false porque ImageKit gestiona versiones
        return False
