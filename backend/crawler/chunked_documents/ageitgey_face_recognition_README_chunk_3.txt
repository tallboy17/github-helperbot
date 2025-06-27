Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
Get the locations and outlines of each person's eyes, nose, mouth and chin.  
![](https://cloud.githubusercontent.com/assets/896692/23625282/7f2d79dc-025d-11e7-8728-d8924596f8fa.png)  
```python
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_landmarks_list = face_recognition.face_landmarks(image)
```  
Finding facial features is super useful for lots of important stuff. But you can also use it for really stupid stuff
like applying [digital make-up](https://github.com/ageitgey/face_recognition/blob/master/examples/digital_makeup.py) (think 'Meitu'):  
![](https://cloud.githubusercontent.com/assets/896692/23625283/80638760-025d-11e7-80a2-1d2779f7ccab.png)