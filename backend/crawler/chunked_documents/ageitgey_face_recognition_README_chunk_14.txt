Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
The `face_recognition` command lets you recognize faces in a photograph or
folder full  for photographs.  
First, you need to provide a folder with one picture of each person you
already know. There should be one image file for each person with the
files named according to who is in the picture:  
![known](https://cloud.githubusercontent.com/assets/896692/23582466/8324810e-00df-11e7-82cf-41515eba704d.png)  
Next, you need a second folder with the files you want to identify:  
![unknown](https://cloud.githubusercontent.com/assets/896692/23582465/81f422f8-00df-11e7-8b0d-75364f641f58.png)  
Then in you simply run the command `face_recognition`, passing in
the folder of known people and the folder (or single image) with unknown
people and it tells you who is in each image:  
```bash
$ face_recognition ./pictures_of_people_i_know/ ./unknown_pictures/

/unknown_pictures/unknown.jpg,Barack Obama
/face_recognition_test/unknown_pictures/unknown.jpg,unknown_person
```  
There's one line in the output for each face. The data is comma-separated
with the filename and the name of the person found.  
An `unknown_person` is a face in the image that didn't match anyone in
your folder of known people.