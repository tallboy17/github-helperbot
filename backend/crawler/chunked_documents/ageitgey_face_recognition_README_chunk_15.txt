Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
The `face_detection` command lets you find the location (pixel coordinatates)
of any faces in an image.  
Just run the command `face_detection`, passing in a folder of images
to check (or a single image):  
```bash
$ face_detection  ./folder_with_pictures/

examples/image1.jpg,65,215,169,112
examples/image2.jpg,62,394,211,244
examples/image2.jpg,95,941,244,792
```  
It prints one line for each face that was detected. The coordinates
reported are the top, right, bottom and left coordinates of the face (in pixels).