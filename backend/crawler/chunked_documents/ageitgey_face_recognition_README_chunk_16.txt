Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
If you are getting multiple matches for the same person, it might be that
the people in your photos look very similar and a lower tolerance value
is needed to make face comparisons more strict.  
You can do that with the `--tolerance` parameter. The default tolerance
value is 0.6 and lower numbers make face comparisons more strict:  
```bash
$ face_recognition --tolerance 0.54 ./pictures_of_people_i_know/ ./unknown_pictures/

/unknown_pictures/unknown.jpg,Barack Obama
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person
```  
If you want to see the face distance calculated for each match in order
to adjust the tolerance setting, you can use `--show-distance true`:  
```bash
$ face_recognition --show-distance true ./pictures_of_people_i_know/ ./unknown_pictures/

/unknown_pictures/unknown.jpg,Barack Obama,0.378542298956785
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person,None
```