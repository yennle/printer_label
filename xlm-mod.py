from xml.dom import minidom

datas = ["Part", "Rev", "Date", "PO"]

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
    textfield.setAttribute("id", d)

    #Volatile
    volatile = xmldoc.createElement("Volatile")
    volatile.appendChild(xmldoc.createTextNode("0"))
    textfield.appendChild(volatile)

    #BoundingBox
    boundingbox = xmldoc.createElement("BoundingBox")
    boundingbox.setAttribute("units", "Inches")
    boundingbox.setAttribute("x", "0.080")
    boundingbox.setAttribute("y", "0.000")
    textfield.appendChild(boundingbox)

    #<Font pointsizeheight="12.000" pointsizewidth="0.000" italics="0" weight="400">Arial Bold</Font>
    font = xmldoc.createElement("Font")
    font.setAttribute("pointsizeheight", "12.000")
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
    element.appendChild(xmldoc.createTextNode(d))
    textfield.appendChild(element)

    #append to textfield
    fields.appendChild(textfield)

nodeList = job.childNodes

file = open("ren_test.lnt", 'w')
file.write(xmldoc.toxml())
