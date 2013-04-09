import xml.etree.ElementTree as et
modules = []
roots = []
blocks = []
modules.append(raw_input('first module file '))
modules.append(raw_input('second module file '))
file_out = raw_input('What file would you like to export to? ')
modules[0] = et.parse(modules[0])
modules[1] = et.parse(modules[1])
roots.append(modules[0].getroot())
roots.append(modules[1].getroot())
blocks.append([])
blocks.append([])
for root in roots:
  for child in root:
		blocks[0].append(child.tag)
		blocks[1].append(child.attrib)
wrapper = et.Element('blocks')
wrapper.attrib = {'app':'Snap! Module Combiner 1.0', 'version':'0.1'}
for i in range(0, len(blocks[0])):
	et.SubElement(wrapper, blocks[0][i])
for i in range(0, len(blocks[1])):
	wrapper[i].attrib = blocks[1][i]
f = open(file_out, 'w+')
f.write(et.tostring(wrapper))
f.close()
