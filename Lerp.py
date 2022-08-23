class Lerp:
    def __init__(self):
        pass
    def __del__(self):
        pass

    @classmethod
    def ValueLerp(self, startPos, endPos, t):
        return (startPos * (1.0 - t)+ endPos * t)

    @classmethod
    def Vector2Lerp(self, startPos, endPos, t):
        return (startPos[0] * (1.0 - t)+ endPos[0] * t, startPos[1] * (1.0 - t)+ endPos[1] * t)

    @classmethod
    def Vector3Lerp(self, startPos, endPos, t):
        return (startPos[0] * (1.0 - t)+ endPos[0] * t, startPos[1] * (1.0 - t)+ endPos[1] * t, startPos[2] * (1.0 - t)+ endPos[2] * t)

    @classmethod
    def Vector4Lerp(self, startPos, endPos, t):
        return (startPos[0] * (1.0 - t)+ endPos[0] * t, startPos[1] * (1.0 - t)+ endPos[1] * t, startPos[2] * (1.0 - t)+ endPos[2] * t, startPos[3] * (1.0 - t)+ endPos[3] * t)

        
# print(Lerp.ValueLerp(0, 2, 0.9))