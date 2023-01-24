import os

a="E:/Manas/New folder/"

dl = os.listdir(a)

for i in dl:
	if i[:3] == "One" :
		on = a + i
		nn = a + i[:21] + ".mp4"
		os.rename(on,nn)
	else:
		on = a + i
		nn = a + "One Piece Episode " + i[3:6] + ".mp4"
		os.rename(on,nn)

dl2 = os.listdir(a)
print(dl,'\n')

print(dl2)
