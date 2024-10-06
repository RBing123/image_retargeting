# Using saliency map to image resize
## Saliency calculation with python
Code from [Graph-Based Visual saliency](https://github.com/shreelock/gbvs)
### 0. Setup environment
```shell
$ pip install -r requirements.txt
```
### 1. modify image via change path
In demo.py file, you can change the image, which need to be placed in `/images/` and change the path in the demo.py
```python
imname = "./images/{image.jpg}"
```
### 2. Run the file
Run `demo.py` file in terminal and the `saliency image` will be stored in `/output/`
```shell
$ python demo.py
```

## Optimization
Paper from [Patch-Based Image Warping for Content-Aware Retargeting](http://graphics.csie.ncku.edu.tw/Tony/papers/IEEE_Multimedia_resizing_2013_Feb.pdf)
## 0. Setup environment
* Ubuntu 22.04
* OpenCV and OpenCV_contrib
* Cplex
### (a) install Opencv and Opencv_contrib
Download [OpenCV 3.4.13](https://github.com/opencv/opencv/archive/3.4.13.zip)
Download [OpenCV_contrib 3.4.13](https://github.com/opencv/opencv_contrib/archive/3.4.13.zip)
Place the `Patch` file at the corresponding path, when cmake error occurs
### (b) install Cplex
Download [cplex](https://academic.ibm.com/a2mt/downloads/data_science#/)
## 
