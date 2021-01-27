from mcpi.minecraft import Minecraft as mc
import time
mcs=mc.create()
while True:
        x,y,z=mcs.player.getTilPos()
        mcs.postToChat("You are located on X :"+str(x)+\
                       ",Y:"=+str(y)+",z: "+str(z))
        time.sleep(0.5)
        