Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
```python
import face_recognition

image = face_recognition.load_image_file("my_picture.jpg")
face_locations = face_recognition.face_locations(image)

# face_locations is now an array listing the co-ordinates of each face!
```  
See [this example](https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_picture.py)
to try it out.  
You can also opt-in to a somewhat more accurate deep-learning-based face detection model.  
Note: GPU acceleration (via NVidia's CUDA library) is required for good
performance with this model. You'll also want to enable CUDA support
when compliling `dlib`.  
```python
import face_recognition

image = face_recognition.load_image_file("my_picture.jpg")
face_locations = face_recognition.face_locations(image, model="cnn")

# face_locations is now an array listing the co-ordinates of each face!
```  
See [this example](https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_picture_cnn.py)
to try it out.  
If you have a lot of images and a GPU, you can also
[find faces in batches](https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_batches.py).