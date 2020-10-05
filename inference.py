import tensorflow as tf
import numpy as np
import json
import requests

SIZE=128
MODEL_URI = 'http://localhost:8501/v1/models/pets:predict'
CLASSES = ['CAT','DOG']
def get_pred(image_path):
    img = tf.keras.preprocessing.image.load_img(
        image_path, target_size=(SIZE,SIZE)
    )

    img = tf.keras.preprocessing.image.img_to_array(img)
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    img = np.expand_dims(img,axis=0)

    data = json.dumps({
        'instances':img.tolist()
    })

    response = requests.post(MODEL_URI, data=data.encode())
    result = json.loads(response.text)
    prediction = np.squeeze(result['predictions'][0])
    _class_name = CLASSES[int(prediction > 0.5)]
    return _class_name
