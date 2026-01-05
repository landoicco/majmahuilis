from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFile


loadPrcFile("settings.prc")


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        grass_block = loader.loadModel("resources/grass-block.glb")
        girl = loader.loadModel("resources/girl.blend")

        grass_block = grass_block.reparentTo(render)
        # girl = girl.reparentTo(render)


Game().run()
