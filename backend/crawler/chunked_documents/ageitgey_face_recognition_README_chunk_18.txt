Repository: ageitgey/face_recognition
Language: Python
Stars: 54927
Forks: 13615
-----
Face recognition can be done in parallel if you have a computer with
multiple CPU cores. For example, if your system has 4 CPU cores, you can
process about 4 times as many images in the same amount of time by using
all your CPU cores in parallel.  
If you are using Python 3.4 or newer, pass in a `--cpus <number_of_cpu_cores_to_use>` parameter:  
```bash
$ face_recognition --cpus 4 ./pictures_of_people_i_know/ ./unknown_pictures/
```  
You can also pass in `--cpus -1` to use all CPU cores in your system.