Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
If you simply want to know the names of the people in each photograph but don't
care about file names, you could do this:  
```bash
$ face_recognition ./pictures_of_people_i_know/ ./unknown_pictures/ | cut -d ',' -f2

Barack Obama
unknown_person
```