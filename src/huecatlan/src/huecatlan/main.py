from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile, DirectionalLight, AmbientLight


loadPrcFile("settings.prc")


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load models
        grass_block = loader.loadModel("resources/grass-block.glb")
        dirt_block = loader.loadModel("resources/dirt-block.glb")
        stone_block = loader.loadModel("resources/stone-block.glb")
        sand_block = loader.loadModel("resources/sand-block.glb")

        girl = loader.loadModel("resources/girl.blend")

        # Render models
        grass_block = grass_block.reparentTo(render)

        dirt_block.setPos(0, 2, 0)
        dirt_block = dirt_block.reparentTo(render)
        stone_block.setPos(0, 4, 0)
        stone_block = stone_block.reparentTo(render)
        sand_block.setPos(0, 6, 0)
        sand_block = sand_block.reparentTo(render)

        # girl = girl.reparentTo(render)

        # Lights
        main_light = DirectionalLight("main light")
        main_light_node_path = render.attachNewNode(main_light)
        main_light_node_path.setHpr(30, -60, 0)
        render.setLight(main_light_node_path)

        ambient_light = AmbientLight("ambient light")
        ambient_light.setColor((0.3, 0.3, 0.3, 1))
        ambient_light_node_path = render.attachNewNode(ambient_light)
        render.setLight(ambient_light_node_path)


Game().run()
