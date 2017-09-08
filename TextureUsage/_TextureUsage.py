import os

files = os.listdir()
test = files[0:10]
textures = {}
unique_textures = []
for json in files:
	if ('.json' in json):
		file = open(json,'r')

		lines = file.readlines()
		texture_list = []
		for line in lines:
			if ('blocks/' in line):
				splitline = line.split(':')
				texturepart = splitline[1]
				texture = texturepart.strip().replace('"','').replace(',','')
				if (texture not in texture_list):
					texture_list.append(texture)
		
		for key in texture_list:
			if key in textures:
				textures[key].append(json)
			else:
				textures[key] = [json]

		file.close()

f = open('_textures.txt','w')
for texturefile in textures:
	count = len(textures[texturefile])
	if (count > 1):
		f.write('%s: [ ' % (texturefile))
		for jsonfile in textures[texturefile]:
			f.write('%s ' % (jsonfile))
		f.write(']\n')
f.close()
