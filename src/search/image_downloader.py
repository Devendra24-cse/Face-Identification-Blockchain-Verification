import cv2
import numpy as np
import requests


class ImageDownloader:
    def download(self, image_url):
        """
        Download an image from a URL
        and convert it into an OpenCV image.
        """

        response = requests.get(
            image_url,
            timeout=10
        )

        response.raise_for_status()

        image_array = np.frombuffer(
            response.content,
            dtype=np.uint8
        )

        image = cv2.imdecode(
            image_array,
            cv2.IMREAD_COLOR
        )

        if image is None:
            raise ValueError(
                "Could not decode downloaded image."
            )

        return image