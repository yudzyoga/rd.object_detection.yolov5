# pull yolov5 image
FROM ultralytics/yolov5:v4.0

# change dir
WORKDIR /usr/src/app

# mkdir for dataset
RUN mkdir -p /usr/src/app/dataset

# Copy contents
COPY ./dataset /usr/src/app/dataset
COPY ./configs/custom.yaml /usr/src/app/data
COPY ./configs/yolov5l_custom.yaml /usr/src/app/models
COPY ./configs/helper.py /usr/src/app/utils
COPY ./configs/how-to-use.ipynb /usr/src/app/
COPY ./configs/train.py /usr/src/app/train.py

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
