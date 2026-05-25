from PIL import Image, ImageDraw, ImageFont
import textwrap

text="Hello I am AASISH"

font_path = r"C:\Users\aasis\Documents\Handwriting Script\sketchy_notes\Sketchy Notes.otf"
font_size = 32

width,height=800,1000
background=Image.new("RGB",(width,height),(255,255,255))
draw=ImageDraw.Draw(background)

font=ImageFont.truetype(font_path,font_size)
margin=50
offset=50
for line in textwrap.wrap(text,width=40):
    draw.text((margin,offset),line,font=font,fill=(0,0,0))
    offset+=font_size+10

background.save("output.jpg")
print("Image saved as output.jpg")
