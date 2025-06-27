Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
Find all the faces that appear in a picture:  
![](https://cloud.githubusercontent.com/assets/896692/23625227/42c65360-025d-11e7-94ea-b12f28cb34b4.png)  
```python
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)
```