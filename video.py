import os
import cv2
from PIL import Image

os.chdir(r"C:\Users\berza\OneDrive\Documenten\cv\video using images\images")
path = os.getcwd()

mean_height=0
mean_width=0
image_files = [f for f in os.listdir(path) if f.endswith(('.jpg', '.jpeg', '.png'))]
number_of_images=len(image_files)

for i in image_files:
    img=Image.open(os.path.join(path,i))
    width,height=img.size
    mean_width=mean_width+width
    mean_height=mean_height+height

mean_width=mean_width//number_of_images
mean_height=mean_height//number_of_images
print(mean_width,mean_height)

for i in os.listdir('.'):
    if i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.png'):
        img=Image.open(os.path.join(path,i))
        width,height=img.size
        print(height,width)
        image_resize=img.resize((mean_width,mean_height),Image.ANTIALIAS)
        image_resize.save(i,"JPEG",quality=95)
def video_generator():
    video_name="video.avi"
    os.chdir("C:\\Users\\berza\\OneDrive\\Documenten\\cv\\video using images\\images")
    images=[]
    for i in os.listdir('.'):
        if i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.png'):
            images.append(img)
    frame=cv2.imread(os.path.join(".",images[0]))
    height,width,layers=frame.shape

    video=cv2.VideoWriter(video_name,0,1,(width,height))
    for image in images:
        video.write(cv2.imread(os.path.join(".",image)))
    cv2.destroyAllWindows()
    video.release()
video_generator()