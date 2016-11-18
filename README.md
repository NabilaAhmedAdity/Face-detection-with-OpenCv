# Face-detection-with-OpenCv

Here I have applied the haar-like feature to detect human face.

The code is performing the following tasks:

1) Capture frames(images) from a video device(in my case it's webcam).

2) Convert the color image into a gray image.

3) Apply haar-like feature on the gray image. Which return an array of faces in rectangular form.

We got our face portions now the only task is to crop the portions from the original frame.

4) Crop the rectangular boxes from the original frame and save.
