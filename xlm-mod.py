from xml.dom import minidom

class Data:
    def __init__(self, name, value, font_h, x, y):
        self.name = name
        self.value = value
        self.font_h = font_h
        self.x = x
        self.y = y

f_height = "10.000"

part = Data("Part #", "CN-321", "14.000", "0.080", "0.000")
rev = Data("Rev", "31", f_height, "0.000", "0.300")
dash_1 = Data("dash1", "-", f_height, "0.150", "0.350")
date = Data("Date", "2101", f_height, "0.250", "0.300")
dash_2 = Data("dash2", "-", f_height, "0.580", "0.350")
po = Data("PO", "12345678", f_height, "0.700", "0.300")

datas = [part, rev, dash_1, date, po, dash_2]

DOMimpl = minidom.getDOMImplementation()

xmldoc = DOMimpl.createDocument(None,"Job", None)
job = xmldoc.documentElement

#Energy
energy = xmldoc.createElement("Energy")
energy.appendChild(xmldoc.createTextNode("Normal"))
job.appendChild(energy)

#SensorMode
sensor = xmldoc.createElement("SensorMode")
sensor.appendChild(xmldoc.createTextNode("BlackMark"))
job.appendChild(sensor)

#Quantity
quantity = xmldoc.createElement("Quantity")
quantity.appendChild(xmldoc.createTextNode("1"))
job.appendChild(quantity)

#LabelSize
label_size = xmldoc.createElement("LabelSize")
label_size.setAttribute("units", "Inches")
label_size.setAttribute("length", "1.000")
label_size.setAttribute("width", "1.200")
job.appendChild(label_size)

#Image
image = xmldoc.createElement("Image")
image.setAttribute("id", "DD Label")
image.setAttribute("version", "1")
job.appendChild(image)

#ImageSize
image_size = xmldoc.createElement("ImageSize")
image_size.setAttribute("units", "Inches")
image_size.setAttribute("x", "0.040")
image_size.setAttribute("y", "0.100")
image_size.setAttribute("height", "0.800")
image_size.setAttribute("width", "1.000")
image_size.setAttribute("origin", "TopLeft")
image.appendChild(image_size)

#Fields
fields = xmldoc.createElement("Fields")
fields.setAttribute("counts", str(len(datas)))
image.appendChild(fields)

for d in datas:
    #Create Textfield
    textfield = xmldoc.createElement("Textfield")
    textfield.setAttribute("id", d.name)

    #Volatile
    volatile = xmldoc.createElement("Volatile")
    volatile.appendChild(xmldoc.createTextNode("0"))
    textfield.appendChild(volatile)

    #BoundingBox
    boundingbox = xmldoc.createElement("BoundingBox")
    boundingbox.setAttribute("units", "Inches")
    boundingbox.setAttribute("x", d.x)
    boundingbox.setAttribute("y", d.y)
    textfield.appendChild(boundingbox)

    #<Font pointsizeheight="12.000" pointsizewidth="0.000" italics="0" weight="400">Arial Bold</Font>
    font = xmldoc.createElement("Font")
    font.setAttribute("pointsizeheight", d.font_h)
    font.setAttribute("pointsizewidth", "0.000")
    font.setAttribute("italics", "0")
    font.setAttribute("weight", "400")
    font.appendChild(xmldoc.createTextNode("Arial"))
    textfield.appendChild(font)

    #<BackgroundColor>White</BackgroundColor>
    bg_color = xmldoc.createElement("BackgroundColor")
    bg_color.appendChild(xmldoc.createTextNode("White"))
    textfield.appendChild(bg_color)

    #<ForegroundColor>Black</ForegroundColor>
    fg_color = xmldoc.createElement("ForegroundColor")
    fg_color.appendChild(xmldoc.createTextNode("Black"))
    textfield.appendChild(fg_color)

    #<VerticalJustification>Top</VerticalJustification>
    vert_just = xmldoc.createElement("VerticalJustification")
    vert_just.appendChild(xmldoc.createTextNode("Top"))
    textfield.appendChild(vert_just)

    #<HorizontalJustification>Left</HorizontalJustification>
    hori_just = xmldoc.createElement("HorizontalJustification")
    hori_just.appendChild(xmldoc.createTextNode("Left"))
    textfield.appendChild(hori_just)

    #create Data
    element = xmldoc.createElement("Data")
    element.appendChild(xmldoc.createTextNode(d.value))
    textfield.appendChild(element)

    #append to textfield
    fields.appendChild(textfield)

nodeList = job.childNodes

file = open("ren_test.lnt", 'w')
file.write(xmldoc.toxml())
