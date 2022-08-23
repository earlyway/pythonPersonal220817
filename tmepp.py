newScene()

sign = 2.0
localZ = 0
def animate(node):
    global sign
    global localZ

    node.setLocalTranslation(0, 0, localZ)
    localZ = localZ + sign

    if localZ > 10:
        timer.setActive(false)


box = createBox(50, 50, 50, 1, 1, 5000,   1.0, 0.0, 0.0, 0)
# for vertices animation we disable the display list cache to get more speed!
box.setDlistCache(false)
box.makeTransform()
box = findNode("Transform");

timer = vrTimer(0.5)
timer.connect(animate, box)
timer.setActive(true)

updateScene()
setNear(0.1)