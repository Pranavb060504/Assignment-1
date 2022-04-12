import vpython as vp
rod = vp.cylinder(pos=vp.vector(0,-3,0),axis=vp.vector(0,1,0), radius=3,length=7,opacity=0.3,color=vp.vector(0,0,1))
cone = vp.cone(pos=vp.vector(0,-3,0),axis=vp.vector(0,1,0),radius=3,length=3,color=vp.vector(1,0,0))
ball = vp.sphere(pos=vp.vector(0,4,0),radius=3,color=vp.vector(1,0,0))
mybox = vp.box(pos=vp.vector(0,6,0),axis=vp.vector(1,0,0),length=6, height=4, width=6,color=vp.color.black)
