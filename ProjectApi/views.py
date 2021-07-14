from django.http import HttpResponse
from django.shortcuts import render
import pickle
#import torch
#import torchvision
import numpy as np

#model=pickle.load(open('resnet.pkl','rb'))
def home(request):
    return render(request,"home.html")

def predict(request):
    # test_transform = torchvision.transforms.Compose([
    # torchvision.transforms.Resize(size=(224,224)),
    # torchvision.transforms.ToTensor(),
    # torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229,0.224,0.225])
    # ])


    # image = 

    # transformed_image = test_transform(image)
    # outputs=resnet18(transformed_image[None,...])
    # _,predicts=torch.max(outputs,1)
    # if predicts[0]==2:
    #     print("COVID")
    # elif predicts[0]==1:
    #     print("VIRAL")
    # else:
    #     print("NORMAL")
    
    print(predicts)
    return render(request,"home.html")
