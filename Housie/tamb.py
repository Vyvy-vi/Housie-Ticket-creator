import random
from PIL import Image, ImageDraw, ImageFont
def ticket(tnum):
    tam=[[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]
    for ls in tam:
        for i in range(5):
            num_gen(ls)
    image = Image.open('./tc.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=16)
    color = 'rgb(0, 0, 0)'
    for i in tam:
        for j in range(len(i)):
            if i[j] != 0:
                draw.text((20+ 31.5*(j), 20+ (31*(tam.index(i)))), str(i[j]), fill=color, font=font)
            else:
                continue
    print('Created Ticket#',tnum)
    prnt='ticket#'+str(tnum)+'.png'  
    image.save(prnt)
def num_gen(ls):
    k=random.randint(1,100)
    if k not in ls:
        pos=random.randint(0,8)
        ps= pos-2
        pst= pos+2
        if pos==0 or pos==1 or pos==2:
            ps+=2
        elif pos==8 or pos==7 or pos ==6:
            pst-=2

        if ls[pos]==0 and (ls[ps]==0 or ls[pst]==0):
            ls[pos]=k
            return
        else:
            num_gen(ls)
    else:
        num_gen(ls)

nt= 12       
"""nt= int(input('Enter no. of tickets to be created:'))""" #uncommnet this to make tickets according to wanted amount.
for tnum in range(nt):
    ticket(tnum)





    
