from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile, DirectionalLight, AmbientLight


loadPrcFile("settings.prc")


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.load_models()
        # self.draw_samples()
        self.set_lights()
        self.generate_terrain()
        self.set_camera()

    def load_models(self):
        self.grass_block = loader.loadModel("resources/grass-block.glb")
        self.dirt_block = loader.loadModel("resources/dirt-block.glb")
        self.stone_block = loader.loadModel("resources/stone-block.glb")
        self.sand_block = loader.loadModel("resources/sand-block.glb")

        # girl = loader.loadModel("resources/girl.blend")

    def draw_samples(self):
        self.grass_block = self.grass_block.reparentTo(render)

        self.dirt_block.setPos(0, 2, 0)
        self.dirt_block = self.dirt_block.reparentTo(render)
        self.stone_block.setPos(0, 4, 0)
        self.stone_block = self.stone_block.reparentTo(render)
        self.sand_block.setPos(0, 6, 0)
        self.sand_block = self.sand_block.reparentTo(render)

        # girl = girl.reparentTo(render)

    def set_lights(self):
        main_light = DirectionalLight("main light")
        main_light_node_path = render.attachNewNode(main_light)
        main_light_node_path.setHpr(30, -60, 0)
        render.setLight(main_light_node_path)

        ambient_light = AmbientLight("ambient light")
        ambient_light.setColor((0.3, 0.3, 0.3, 1))
        ambient_light_node_path = render.attachNewNode(ambient_light)
        render.setLight(ambient_light_node_path)

    def set_camera(self):
        self.disableMouse()
        self.camera.setPos(0, 0, 3)

    def generate_terrain(self):
        for z in range(10):
            for y in range(20):
                for x in range(20):
                    new_block_node = render.attachNewNode("new-block-placeholder")

                    new_block_node.setPos(x * 2 - 20, y * 2 - 20, -z * 2)

                    if z == 0:
                        self.grass_block.instanceTo(new_block_node)
                    else:
                        self.dirt_block.instanceTo(new_block_node)


Game().run()
