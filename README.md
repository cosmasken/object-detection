### Python Object Detection

This is a tiny script that uses opencv to detect different objects in an image.

It outputs the type of object detected, the boundary box that surrounds the object and the confidence level.

This can form the basis of detecting if an image has a clear object of a person e.g a profile picture.

As an example, you can reject any image with a confidence level lower than 0.9 and with more than one person or objects.

## Getting the environment ready

Install Anaconda for managing the python environment:
```
https://www.anaconda.com/distribution/
```

Create a new python environment (Preferably the latest python):
```
conda create -n gundua python=3.11.0
```

Activate the environment:
```
condo activate gundua
```

Install tensorflow and opencv (This step can hang sometimes. If it does use conda search and specify the exact version when installing):
```
conda install tensorflow opencv
```

Install cvlib:
```
pip install cvlib
```

Run the script:
```
python detect.py
```

