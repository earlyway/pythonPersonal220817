'''

1 머터리얼에 image를 주는 방법
2 머터리얼에 투명도를 높이는 방법
3 라이트 생성해놓고 show/hide 시키는 방법

'''

#1------------------------------------------------------
# 매터리얼에 이미지 텍스처를 추가하는 방법
# 주의점은 머터리얼이 다른 노드와 중복되면 안된다.
examplesDir = vrFileIOService.getVREDExamplesDir()

# load the image that we will use as texture
waterImage = vrImageService.loadImage(examplesDir + "/textures/Wasser1.png")

# find the material we want to change and edit its diffuse texture
f = vrMaterialService.findMaterial("fur_white")
fTex = f.getDiffuseTexture()
fTex.setImage(waterImage)
fTex.setUseTexture(True)


#2------------------------------------------------------
# 매터리얼의 투명도를 주는 방법
# 주의점은 머터리얼이 다른 노드와 중복되면 안된다.
f = vrMaterialService.findMaterial("fur_white")
dd = vrdBRDFMaterial.getTransparency(f)

a = QVector3D(0.25,0.25,0.25)
dd.setSeeThrough(a)


#3------------------------------------------------------
#오브젝트 하위에 포인트라이트를 넣고 constraintOn될 때마다 이 라이트를 show 하는 방법.
#주의점 : vr 환경에서 라이트 노드는 최소화하는 방향으로 하는 것이 리소스관리, 메모리관리 측면에서 좋음.
#vset1
a = vrNodeService.findNode("PointLight1")
b = hideNode(a)

#vset2
t = showNode(a)


