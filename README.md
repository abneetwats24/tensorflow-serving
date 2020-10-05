## RUN TENSORFLOW SERVING DOCKER INSTANCE

```bash
$ sudo docker run -p 8501:8501 --name=pets -v "<path to repo>/app/pets:/models/pets/1" -e MODEL_NAME=pets tensorflow/serving
```

## START FLASK APP

```bash
$ python3 app.py
```