Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
```python
import face_recognition

picture_of_me = face_recognition.load_image_file("me.jpg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

unknown_picture = face_recognition.load_image_file("unknown.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
print("It's a picture of me!")
else:
print("It's not a picture of me!")
```  
See [this example](https://github.com/ageitgey/face_recognition/blob/master/examples/recognize_faces_in_pictures.py)
to try it out.