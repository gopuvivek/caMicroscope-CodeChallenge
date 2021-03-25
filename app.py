from flask import Flask, Response, request, render_template, redirect
import os
from werkzeug.utils import secure_filename
import cv2
import random as rd
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def makeBorders(img):
    image = cv2.imread(img)
    image_de = cv2.fastNlMeansDenoisingColored(image,None,40,10,7,21)
    ret,th1 = cv2.threshold(image_de,60,255,cv2.THRESH_BINARY)
    edges = cv2.Canny(th1,127,255)
    edges = cv2.cvtColor(edges, cv2.COLOR_BGR2RGB)
    r,c,_ = edges.shape
    
    fig = plt.figure(figsize=(10,10))
    plt.subplot(2,2,1)
    plt.title("Original Image")
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,2,2)
    plt.title("Denoised Image")
    plt.imshow(image_de)
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,2,3)
    plt.title("After Binary Thresholding")
    plt.imshow(th1)
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,2,4)
    plt.title("Final Edges")
    plt.imshow(edges)
    plt.xticks([])
    plt.yticks([])
    plt.savefig('static/outputs/detail_o.jpg')
    cv2.imwrite('static/outputs/edges.jpg',edges)
    for x in range(r):
        for y in range(c):
            if(False not in edges[x,y,:]):
                image[x,y,:] = [255,255,0]
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    cv2.imwrite('static/outputs/input_e.jpg',image)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(7,7))
    plt.imshow(image)
    plt.title("Input Image with Edges")
    plt.savefig('static/outputs/input_edges.jpg')
    
    

def getClosestEdge(x,y,edges):
    r,c = edges.shape
    x = int(x)
    y = int(y)
    
    d,i,j = (0,0,0)
    queue = [(x,y,0)]
    vis = set()
    while queue:
        i,j,d = queue.pop(0)
        if((i,j) in vis):
            continue
        if(not(0<=i<r and 0<=j<c)):
            continue
        if(edges[i,j]==255):
            return [d,(i,j)]
            
        vis.add((i,j))
        queue+=[((i+1,j,d+1))]
        queue+=[((i-1,j,d+1))]
        queue+=[((i,j+1,d+1))]
        queue+=[((i,j-1,d+1))]

    

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getImage',methods=['GET','POST'])
def getImage():
    ischeck = request.form.get('check')
    lfile = request.form.get('local')
    fname=""
    if ischeck==None:
        if 'file' not in request.files:
            return "No Input file given"
        file = request.files['file']
        if  file.filename == '':
            return "No Input file given"
        ftype = file.filename.split(".")[-1]
        fname = "upload."+ftype   
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(fname)))
        

    else:
        fname = "{}.jpeg".format(lfile)
    timg = os.path.join(app.config['UPLOAD_FOLDER'],fname)
    imge = cv2.imread(timg)
    imge = cv2.cvtColor(imge, cv2.COLOR_BGR2RGB)
    fig = plt.figure(figsize=(7,7))
    plt.imshow(imge)
    plt.title("Input Image")
    plt.savefig('static/outputs/input_plot.jpg')
    cv2.imwrite('static/outputs/input.jpg',imge)

    return render_template('getImage.html')


@app.route('/getEdges',methods=['POST'])
def getBorders():

    makeBorders('static/outputs/input.jpg')

    return render_template('getEdges.html')

@app.route('/getInputPoint',methods=['GET','POST'])
def getInputPoint():
    return render_template('getInputPoint.html')

    
@app.route('/getNearestEdge',methods=['POST'])
def Solve():
    try:
        x = int(request.form.get('x'))
        y = int(request.form.get('y'))
    except:
        return "Please select a point!"
    edges = cv2.cvtColor(cv2.imread('static/outputs/edges.jpg'),cv2.COLOR_BGR2GRAY)
    d,t = getClosestEdge(x,y,edges)
    tx,ty = t
    # image = cv2.imread('static/outputs/input_e.jpg')
    # image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    # fig = plt.figure()
    # assert edges[tx,ty]==255
    # src = plt.scatter(y,x,color='red',s=25)
    # dest = plt.scatter(ty,tx,color='green',s=0)
    # plt.imshow(image)
    # plt.title("Final Output")
    # plt.legend((src,dest),("Given Point","Point On Edge"),fontsize=7.5,loc="upper right")
    # plt.savefig("static/outputs/final_output.jpg")

    return render_template('getNearestEdge.html',d=d,x=x,y=y,tx=tx,ty=ty)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(debug=True)