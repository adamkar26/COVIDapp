from tensorflow import keras
import os
from django.conf import settings
import numpy as np
from skimage.io import imread
from tensorflow.keras.preprocessing import image
from skimage.exposure import equalize_hist
from skimage.color import rgb2gray, gray2rgb


class DeppLearning:

    def __init__(self, model):
        self.path = os.path.join(settings.BASE_DIR, model)
        self.model = keras.models.load_model(self.path)

    def diagnose(self, path_to_file):
        path_to_file = path_to_file[1:]
        path = os.path.join(settings.BASE_DIR, path_to_file)
        img = image.load_img(path, target_size = (224, 224))
        img = image.img_to_array(img, dtype=np.uint8)
        img = rgb2gray(img)
        img_his = equalize_hist(img)
        img_his = gray2rgb(img_his)
        img_his = img_his * 255
        img_his = np.array([keras.applications.resnet50.preprocess_input(img_his)])

        return self.model.predict(img_his)




