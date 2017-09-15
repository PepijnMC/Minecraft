import os
import sys

files = os.listdir()
test = files[0:10]
textures = {}
unique_textures = []
default_limit = 0

def error_handler(error):
	print (error)
	log = open('_error_log.txt','w')
	log.write(error)
	log.close()

if (len(sys.argv) > 1):
	arg = sys.argv[1]
	try:
		limit = int(arg)
	except ValueError:
		error_handler('Error: Limit must be an integer.')
		sys.exit()
else:
	limit = default_limit

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

f = open('_textures_%s.txt' % (limit),'w')
for texturefile in textures:
	count = len(textures[texturefile])
	if (count > limit):
		f.write('%s (%s): [ ' % (texturefile,count))
		for jsonfile in textures[texturefile]:
			f.write('%s ' % (jsonfile))
		f.write(']\n')
f.close()
