## YOLOv5 Custom Training

### To build the Dockerfile
sudo docker image build -t yolov5_cups .

### To run the the docker container
sudo docker container run -it --rm --gpus all --name yolov5_cups4 -v $(pwd)/result:/usr/src/app/runs -p 8888:8888 yolov5_cups


