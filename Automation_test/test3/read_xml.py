from xml.dom import minidom
#打开xml文档
dom = minidom.parse('info.xml')
#得到文档的元素对象
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)

