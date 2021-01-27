from mcpi.minecraft import Minecraft as mc
m
mcs =mc.create()
print (mcs.player.getPos())
x=100
y=100
z=100
x=100
i=0
mcs.player.setPos(x,y,z)
time.sleep(1.5)
y=y-10
mcs.player.setPos(x,y,z)
time.sleep(1.5)
y=y-10
mcs.player.setPos(x,y,z)
time.sleep(1.5)
y=y-10
