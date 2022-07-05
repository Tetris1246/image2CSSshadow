from PIL import Image

def getColors(image):
    with Image.open(image) as im:
        pix = im.load()
        Sx, Sy = im.size[1], im.size[0]
    colors = []
    temp = []
    for x in range(Sx):
        temp = []
        for y in range(Sy):
            temp.append(pix[y, x])
        colors.append(temp)
    return colors

pixelsize = 1
imagename = input("image name: ")

colors = getColors(imagename)
shadowlist = []
for lines in range(1, len(colors)):
    for pixel in range(1, len(colors[0])):
        shadowlist.append(f"{pixel*pixelsize}px {lines*pixelsize}px rgb({colors[lines][pixel][0]}, {colors[lines][pixel][1]}, {colors[lines][pixel][2]})")
css = "#image {\nbox-shadow:\n"
css += ", \n".join(shadowlist)
css += ";\n}"

with open('style.css', 'a') as filehandle:
    filehandle.write(css)
    filehandle.close()

html = f"<!DOCTYPE html>\n<html lang='en'>\n<title>{imagename}</title>\n<style>\n"
html += css
html += f"</style>\n<body id='image' style='width: 1px;'>\n{imagename}\n</body>\n</html>"

with open('index.html', 'a') as filehandle:
    filehandle.write(html)
    filehandle.close()
