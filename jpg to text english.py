import pytesseract
from PIL import Image

path = r"C:\Users\kryna\Downloads\call.jpg"                                      #opening pictures
img = Image.open(path)
pytesseract.pytesseract.tesseract_cmd = r'D:\Programme\Tesseract-OCR\tesseract.exe'


#custom_config = r'--oem 3 --psm 13'
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, lang = 'eng', config = custom_config)    #reading language settings

lines=[]
new=[]
new_text =''
lines=text.split('\n')

for i in lines:                                                                  #removing spaces and ethers in the text
    if ' ' != i and '' != i:
        new.append(i)
for k in new:
    new_text = new_text + k + '\n'
print(new_text)


with open(r'C:\Users\kryna\Downloads\call.txt', 'w', encoding="utf-8") as f:     #creating text.doc. and entering data from the text
    f.write(new_text)
print('The end')
