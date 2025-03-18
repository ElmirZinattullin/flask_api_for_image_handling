import os
from config import RESULT_FOLDER

from .photo_generate import generate_image_pillow



class ModelAI:

    def __init__(self, weights_path):
        with open(weights_path) as weights_file:
            weighs = weights_file.read()
        self.weighs = weighs

    def _save_photo(self, photo, api_session:str):
        """Сохраняем фото в определенной папке которую потом раздадим через веб сервер или апишку"""
        filename = f"{api_session}.jpg"
        path = RESULT_FOLDER / filename
        generate_image_pillow(300, 300, path)
        return filename

    def _photo_handler(self, photo):
        """Обработка и получение реультата"""



        return "some_photo", {"caries": "4", "zubov": "3"}

    def get_result(self, api_session, input_photo) -> tuple[dict, str]:
        """функция для обработке фото и получения результат
            :return: JSON объект - словарь с текстовыми объектами

            можете воспользоваться pydantic

        """
        result_photo, result_data = self._photo_handler(input_photo)
        result_image_path = self._save_photo(result_photo, api_session)
        # result = {"result_data": result_data, "result_image": result_image_path}
        return result_data, result_image_path