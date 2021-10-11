from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'stone.png',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.white,
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'left mouse down':
                destroy(self)

for y  in range (15):
    voxel = Voxel(position=(y,0,2))
    for x in range(8):
        voxel = Voxel(position=(x,0,y))

player = FirstPersonController()

app.run()
