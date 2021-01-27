from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
while True:
        num=0
        try:
            num=int(input('what do you want?'))
        except:
            print("that is not number.")
        x,y,z=mcs.player.getTilePos()
        mcs.setBlock(x,y,z,num)
        e=input("EXIT")
        if e=='y' or e=='y' or e==\
            'yes' or e== 'yes' :
            break
        else:
            continue