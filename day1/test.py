from mcpi.minecraft import Minecraft as mc
mcs =mc.create()
print (mcs.player.getTilePos())
x=50
y=50
z=50
x=60
mcs.player.setTilePos(x,y,z)