Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
```python
import face_recognition

image = face_recognition.load_image_file("my_picture.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)

# face_landmarks_list is now an array with the locations of each facial feature in each face.
# face_landmarks_list[0]['left_eye'] would be the location and outline of the first person's left eye.
```  
See [this example](https://github.com/ageitgey/face_recognition/blob/master/examples/find_facial_features_in_picture.py)
to try it out.