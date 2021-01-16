"""
Nudge extension for Krita 4
Use the arrow keys to nudge layers or selections 1 pixel at a time
"""

from krita import *


class Nudge(Extension):
    def __init__(self, parent):
        self.previousSelect = None
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        leftAction = window.createAction("nudgeLeftAction", "Nudge Left", "tools/scripts/Nudge")
        rightAction = window.createAction("nudgeRightAction", "Nudge Right", "tools/scripts/Nudge")
        upAction = window.createAction("nudgeUpAction", "Nudge Up", "tools/scripts/Nudge")
        downAction = window.createAction("nudgeDownAction", "Nudge Down", "tools/scripts/Nudge")

        leftAction.triggered.connect(self.nudgeLeft)
        rightAction.triggered.connect(self.nudgeRight)
        upAction.triggered.connect(self.nudgeUp)
        downAction.triggered.connect(self.nudgeDown)

    def nudgeOne(self, x, y):
        doc = Krita.instance().activeDocument()
        #select = doc.selection()
        node = doc.activeNode()

        #if select is not None:
        #    """
        #    This is not the functionality that I originally wanted. The functionality that
        #    I want is if a selection is active AND a select tool is active, nudging moves
        #    the selection area by 1px. If any other tool is selected, the selected content
        #    is moved by 1px. This is unfortunately impossible due to the behavior noted
        #    below.
        #    
        #    Documentation for selection is actually shit. x() and y() refer to the actual
        #    position in canvas space of top left corner, but move() will move some internal
        #    pixel selection around to the relative coordinates provided. And it thinks that
        #    0,0 is at x,y. Calling move() will update x and y, but the internal pixel
        #    selection will still think that 0,0 refers to the original x,y position. The
        #    cherry on top is that the dotted line showing the selection is never moved.
        #    """
        #    select.cut(node)
        #    newNode = doc.createNode(node.name() + " - selection", node.type())
        #    doc.rootNode().addChildNode(newNode, node)
        #    select.paste(newNode, select.x(), select.y())
        #    doc.setActiveNode(newNode)
        #    node = doc.activeNode()
        #    select.clear()
        #    doc.setSelection(None)
        """
        Even more problems arose when trying the above, it seems like selection positioning
        in general is bugged and/or terribly documented for scripting.
        """
        npos = node.position()
        node.move(npos.x() + x, npos.y() + y)
        doc.refreshProjection()

    def nudgeLeft(self):
        self.nudgeOne(-1, 0)

    def nudgeRight(self):
        self.nudgeOne(1, 0)

    def nudgeUp(self):
        self.nudgeOne(0, -1)

    def nudgeDown(self):
        self.nudgeOne(0, 1)


Krita.instance().addExtension(Nudge(Krita.instance()))
