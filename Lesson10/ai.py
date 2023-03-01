import cv2
from PIL import Image

image_path = "person1.jpg"
image = cv2.imread(image_path)
person_face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
person_face_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")
person_face = person_face_cascade.detectMultiScale(image)

person = Image.open(image_path)
glasses = Image.open('glasses.png')
usy = Image.open('usy.png')
person = person.convert("RGBA")
glasses = glasses.convert("RGBA")

print(person_face)
for(x, y ,w, h,) in person_face:
    glasses = glasses.resize((w, int(h/3)))
    usy = usy.resize((int(w/2), int(h/3)))
    person.paste(glasses, (x, int(y + h/4)), glasses)
    person.paste(usy, (x, int(y + h/4)), usy)
    person.save("newPerson.png")
    person_with_glasses = cv2.imread("newPerson.png")
    cv2.imshow("Person", person_with_glasses)
    cv2.waitKey()


   # cv2.rectangle(image, (x,y),(x+w, y+h), (0,0,255),3)'''

cv2.imshow("Person", image)
cv2.waitKey()
