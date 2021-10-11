# obrigado pokepetter e os outros dev por desenvolver uma base do Projeto!
# Thank You pokepetter and others devs for make this "base" of Minecraft

# Codigo Feito na IDE  Padrão, Minecraft em Python!

# Futuras Adições:  1:

# 1 = Criar Launcher do Jogo
#2 = Criar Mapas diferentes
#3 = Geração de mundo aleatoria (complexo)
#4 = Criar um Inventario
#5 = Gerar Executavel Windows

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

minecraft_run= Ursina()

class Bloco_de_Madeira(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = "assets/planks_oak.png",
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.white,
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                postion_block = Bloco_de_Madeira(position=self.position + mouse.normal)

            if key == 'left mouse down':
                destroy(self)
            if key == 'q':
                close_minecraft= exit('Minecraft Closed.')

for y in range (15):
    voxel = Bloco_de_Madeira(position=(y,0,2))
    for x in range(15):
        voxel = Bloco_de_Madeira(position=(x,0,y))
        
FirstPersonController()
minecraft_run.run()

#WARNING: Não Tente alterar o Valor de Y e X para um nivel de 40+ se sua maquina tiver somente 2GB de RAM e um processador um pouco antigo!
