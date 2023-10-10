import sqlite3
from tkinter import messagebox
from tkinter import *
root=Tk()
import cv2
conn = sqlite3.connect('Form.db')
dbuser = "-"
dbpw = "-"

with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM temp")
        rows = cur.fetchall()
        for row in rows:
            dbuser = row[0]
            dbpw = row[1]
        cur.execute("SELECT * FROM register where fullname=? and email=?",(dbuser,dbpw))
        rows = cur.fetchall()

        xxx2 = "-"
        for row in rows:
           filename = row[7]
img = cv2.imread(filename)

# cv2.imread() -> takes an image as an input
h, w, channels = img.shape

half = w // 2

# this will be the first column
left_part = img[:, :half]

# [:,:half] means all the rows and
# all the columns upto index half

# this will be the second column
right_part = img[:, half:]

# [:,half:] means all the rows and all
# the columns from index half to the end
# cv2.imshow is used for displaying the image
cv2.imshow('Left part', left_part)
cv2.imshow('Right part', right_part)

# this is horizontal division
half2 = h // 2

top = img[:half2, :]
bottom = img[half2:, :]

cv2.imshow('Top', top)
cv2.imshow('Bottom', bottom)

# saving all the images
# cv2.imwrite() function will save the image
# into your pc
cv2.imwrite('top.jpg', top)
cv2.imwrite('bottom.jpg', bottom)
cv2.imwrite('right.jpg', right_part)
cv2.imwrite('left.jpg', left_part)
cv2.waitKey(0)
import cv2

# read the images
img1 = cv2.imread('top.jpg')
img2 = cv2.imread('bottom.jpg')
img3 = cv2.imread('right.jpg')
img4 = cv2.imread('left.jpg')
im_v1 = cv2.vconcat([img1, img2])
#im_v2 = cv2.hconcat([img3, img4])
#im_v = cv2.hconcat([im_v1, im_v2])
cv2.imwrite('join.jpg', im_v1)
# show the output image
cv2.imshow('join.jpg', im_v1)
cv2.waitKey(0)



cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)

frame1 = cv2.imread("join.jpg")
frame2 = frame1
frame3 = cv2.imread(filename)

compare1 = cv2.compare(frame1,frame2,0)


cv2.imshow('image1', compare1)


if compare1.all():
    messagebox.showinfo("Login", " Graphical Authentication is Successfull")
    root.destroy()
else:
    messagebox.showinfo("Login", " Try Again")


cv2.waitKey(0)
cv2.destroyAllWindows()