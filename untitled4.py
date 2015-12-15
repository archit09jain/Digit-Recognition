from sklearn import datasets
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage import color

def flatten_list(l):
    result = []
    for i in l:
        for j in i:
            result.append(j)
    return result

##training features
features = [color.rgb2gray(mpimg.imread("one.png")),color.rgb2gray(mpimg.imread("two.png")),
        color.rgb2gray(mpimg.imread("nine.png"))]

#corresponding labels
labels = [1,2,9]

data = []
for i in features:
    data.append(flatten_list(i))

clf = SVC(gamma = 0.001)
clf.fit(data,labels)

demo_img = color.rgb2gray(mpimg.imread("two_demo.png"))
plt.imshow(demo_img)

print "Prediction: "+ str(clf.predict(flatten_list(demo_img)))
