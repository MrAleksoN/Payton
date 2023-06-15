def convert(x):
 tf=(9/5)*x+32
 return tf
while True:
 tc=input('t v celciax ')
 if tc=='':
     break #или exit()
 else :
     tc=int(tc)
 tf=convert(tc)
 print('t в цельсиях',tc,'т в фаренгейтах',tf)