import os
from flask import Flask, request, render_template,url_for
from flask_cors import CORS, cross_origin
import shutil
import src.predict as predict 
import cv2
import matplotlib.pyplot as plt
app = Flask(__name__)
CORS(app)

upload_folder="./models/brain tumor/static"


@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        image_file=request.files["file"]
        #print(image_file)
        if image_file:
            shutil.rmtree(upload_folder)
            os.makedirs(upload_folder)
            image_loc=os.path.join(upload_folder,image_file.filename)
            image_file.save(image_loc)
            image_name = os.path.basename(image_loc)
            image_name = image_name.split('.')[0]
            print(image_name)
            print(image_loc)
            
            # plt.imshow(cv2.imread(image_loc))
            # plt.show()
            print(upload_folder+"/"+image_name+"NEW.png")
            classifier=predict.predict_img(image_loc,image_name,upload_folder)
            classifier.predict_image()
            # plt.imshow(pred,cmap='gray')
            # plt.show()
            
            # cv2.imwrite(upload_folder+"/"+image_name+"New.png",pred)
            # print(pred.shape)
            return render_template('index.html',image_loc=image_name+"NEW.jpg")
    return render_template('index.html',image_loc=None)


if __name__ == '__main__':
    app.run(debug=True)