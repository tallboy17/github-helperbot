Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
Recognize who appears in each photo.  
![](https://cloud.githubusercontent.com/assets/896692/23625229/45e049b6-025d-11e7-89cc-8a71cf89e713.png)  
```python
import face_recognition
known_image = face_recognition.load_image_file("biden.jpg")
unknown_image = face_recognition.load_image_file("unknown.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
```  
You can even use this library with other Python libraries to do real-time face recognition:  
![](https://cloud.githubusercontent.com/assets/896692/24430398/36f0e3f0-13cb-11e7-8258-4d0c9ce1e419.gif)  
See [this example](https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py) for the code.