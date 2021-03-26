# caMicroscope-CodeChallenge
This is developed as a part of code challenge for caMicroscope's Pathology Smartpens project in GSOC 2021


The page is live [here](https://gsoc2021challenge.herokuapp.com/)

## Tasks

### Edge Detection
- This task was accomplished using a series of steps including image-denoising, binary-thresholding and canny edge detection
- All of which were implemented using opencv-python
![image](https://user-images.githubusercontent.com/56498758/112587574-d4325500-8e23-11eb-8b02-946eb871efb5.png) 
![image](https://user-images.githubusercontent.com/56498758/112587545-c086ee80-8e23-11eb-8543-12a0795d61d5.png)



### Finding Nearest Edge
- The user selects a point on the given image
- This point is then used to find the nearest point on an edges
- Breadth First Search algorithm was used to achieve this

![image](https://user-images.githubusercontent.com/56498758/112586795-6a657b80-8e22-11eb-8a19-456563598b25.png)
![image](https://user-images.githubusercontent.com/56498758/112586944-ab5d9000-8e22-11eb-858d-d143d362f7dd.png)
