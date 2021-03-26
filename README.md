# caMicroscope-CodeChallenge
This is developed as a part of code challenge for caMicroscope's Pathology Smartpens project in GSOC 2021


The page is live [here](https://gsoc2021challenge.herokuapp.com/)

## Tasks

### Edge Detection
- This task was accomplished using a series of steps including image-denoising, binary-thresholding and canny edge detection
- All of which were implemented using opencv-python

<img href="https://gsoc2021challenge.herokuapp.com/static/outputs/input_plot.jpg" height="300" width="300">         <img href="https://gsoc2021challenge.herokuapp.com/static/outputs/input_edges.jpg" height="300" width="300">



### Finding Nearest Edge
- The user selects a point on the given image
- This point is then used to find the nearest point on an edges
- Breadth First Search algorithm was used to achieve this

<img href="https://user-images.githubusercontent.com/56498758/112586795-6a657b80-8e22-11eb-8a19-456563598b25.png"
height="300" width="300">         <img href="https://user-images.githubusercontent.com/56498758/112586944-ab5d9000-8e22-11eb-858d-d143d362f7dd.png" height="300" width="300">
