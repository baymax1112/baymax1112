from mcpi.minecraft import Minecraft 
c=Minecraft.create()m

while 1+1==2:
        hits=mc.events.pollBlockHits()
        if len(hits) > 0:
            hit = hits[0]
            x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
            block=mc.getBlock(x,y,z)
            mc.setBlock(x,y,z,20)