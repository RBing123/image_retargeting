# Using saliency map to image resize
## Saliency calculation
Code from [Graph-Based Visual saliency](https://github.com/shreelock/gbvs)
### 0. Setup environment
```c
pip install -r requirements.txt
```
### 1. modify image via change path
In demo.py file, you can change the image, which 
```python
imname = "./images/{image.jpg}"
```
### 2. Run the file
Run `demo.py` file in terminal and the `saliency image` will be stored in `/output/`
```bash
$ python demo.py
```

