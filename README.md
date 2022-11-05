# Supermarket-Object-Detection-Camera-Using-YOLOv3-Deep-Learning
I was working on the YOLOv3 algorithm to create a simple working version of a out-of-stock shelf inventory management software for small businesses. This model will compare the before sales and after sales images captured from a camera and detect the out-of-stock items from the shelves.

YOLOv3 uses 3 techniques:

Residual blocks: The image is divided into a grid of SxS dimension.
Bounding box regression: Every bounding box in the image consists of Width, Height, Class, Bounding box center.
Intersection Over Union (IOU): It describes how boxes overlap. The blue box is the predicted box while the green box is the real box.
YOLOv3 then combines the three techniques to get high accuracy, high speed, and learning capabilities.
