import xml.dom.minidom as minidom  

# فتح ملف XML للقراءة  
with open('currency.xml', 'r') as xml_file:  
    xml_data = xml_file.read()  

# تحليل البيانات XML  
dom = minidom.parseString(xml_data)  
dom.normalize()  

# الحصول على جميع عناصر Valute  
elements = dom.getElementsByTagName('Valute')  
currency_dict = {}  

# معالجة كل عنصر Valute  
for node in elements:  
    char_code = None  
    nominal_value = None  

    for child in node.childNodes:  
        if child.nodeType == minidom.Node.ELEMENT_NODE:  # استخدم minidom.Node.ELEMENT_NODE للتأكد من نوع العقدة  
            if child.tagName == "CharCode":  
                char_code = child.firstChild.data if child.firstChild else None  
            elif child.tagName == 'Nominal':  
                nominal_value = child.firstChild.data.replace(',', '.') if child.firstChild else None  

    # اجعل الشرط أكثر أمانًا للتأكد من وجود char_code وقيمة nominal قبل إضافته إلى القاموس  
    if char_code is not None and nominal_value is not None:  
        currency_dict[char_code] = nominal_value  

# طباعة النتائج  
print(currency_dict)
