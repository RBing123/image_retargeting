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
Place the `Patch` file at the corresponding path, when cmake error occurs.

cd to switch to the opencv directory, create a build folder, and switch to the build directory
```bash!
cd opencv/
mkdir -p && cd build
```
under ==~/opencv/build/== to build cmake
```cmake!
cmake -D CMAKE_BUILD_TYPE=Release -D OPENCV_GENERATE_PKGCONFIG=ON -D WITH_FFMPEG=ON .. 
```
compile the cmake under ==~/opencv/build/==
```pseudocode!
$ make -j8
```
When performing cmake earlier, the opencv4.pc configuration file has been generated. The installation path of this file is: ==/usr/local/lib/pkgconfig/opencv4.pc==
 
Use the command in the build directory to check
```pseudocode!
$ sudo find / -iname opencv4.pc
```
We need to add the path of opencv4.pc to the environment variable PKG_CONFIG_PATH and create a script file named pkgconfig.sh.
```bash!
$ cd
$ sudo gedit /etc/profile.d/pkgconfig.sh
```
Add the following line of statement to the pkgconfig.sh file, save it and close it.
```pseudocode!
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
```
Then refresh the environment variables to make them effective.
```pseudocode!
$ source /etc/profile
```
We need to add the installation directory of OpenCV's libs to the dynamic library loading configuration file, so that various library files of OpenCV can be found during compilation. Create opencv4.conf below.
```pseudocode!
$ sudo gedit /etc/ld.so.conf.d/opencv4.conf
```
Add the following program to the file
```pseudocode!
/usr/local/lib
```
Refresh the dynamic library environment
```pseudocode!
$ sudo ldconfig
```

After configuring the environment variable PKG_CONFIG_PATH, you can use the pkg-config command to view and manage the opencv configuration file (that is, opencv4.pc)
```pseudocode!
$ pkg-config --cflags opencv4
```
```pseudocode!
$ pkg-config --libs opencv4
```
### (b) install Cplex
Download [cplex](https://academic.ibm.com/a2mt/downloads/data_science#/)
## 
