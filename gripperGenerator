import rhinoscriptsyntax as rs

# Assuming x and y are defined
ptOrigin = rs.AddPoint(0, 0, 0)
ptHeight = rs.AddPoint(0, y, 0)
yLine = rs.AddLine(ptOrigin, ptHeight)
offsetLine = rs.OffsetCurve(yLine, (x * 10, y / 2, 0), x)

yParam = rs.CurveDomain(yLine)
offsetParam = rs.CurveDomain(offsetLine)


paramListOne = (yParam[0], offsetParam[0])
paramListTwo = (yParam[1], offsetParam[1])
print(paramListOne)
# Adjusting the call to AddBlendCurve to correctly use the start and end parameters
blendOne = rs.AddBlendCurve((yLine, offsetLine), (paramListOne), (True, True), (1,1))
blendTwo = rs.AddBlendCurve((yLine, offsetLine), (paramListTwo), (False, False), (1,1))

print(y*arcRatio)

arcRatioPointLowLeft = rs.AddPoint(0, y*arcRatio, 0)
arcRatioPointTopLeft = rs.AddPoint(0, y-y*arcRatio,0)
arcRatioPointMidLeft = rs.AddPoint(arcDepth, y/2, 0)


arc1 = rs.AddArcPtTanPt(arcRatioPointLowLeft, arcRatioPointMidLeft, arcRatioPointTopLeft)
arc2 = rs.MirrorObject(arc1, (x/2, 0, 0),(x/2, 1, 0), True)


def ezBlender(curve1, curve2):
    dmn1, dmn2 = rs.CurveDomain(curve1), rs.CurveDomain(curve2)
    prmList1 = (dmn1[0], dmn2[0])
    blend = rs.AddBlendCurve((curve1, curve2), prmList1, (True, True),(1,1))
    return blend



def mirrorObjectInQuadrants(objToBeMirrored, xAxisLength, yAxisLength):
    # Calculate midpoints for the mirror planes
    xMid = xAxisLength / 2.0
    yMid = yAxisLength / 2.0
    
    # Create points for the mirror planes
    ptX = rs.AddPoint(xMid, 0, 0)
    ptY = rs.AddPoint(0, yMid, 0)
    
    # Create mirror planes
    planeX = rs.PlaneFromNormal(ptX, rs.VectorCreate([0,0,1], ptX))
    planeY = rs.PlaneFromNormal(ptY, rs.VectorCreate([0,0,1], ptY))
    # Mirror the object in the X direction
    mirroredX = rs.MirrorObject(objToBeMirrored, planeX.Origin, planeX.XAxis, True)
    # Mirror the original and the X-mirrored object in the Y direction
    mirroredYOriginal = rs.MirrorObject(objToBeMirrored, planeY.Origin, planeY.YAxis, True)
    mirroredYX = rs.MirrorObject(mirroredX, planeY.Origin, planeY.YAxis, True)
    return [objToBeMirrored, mirroredX, mirroredYOriginal, mirroredYX]


smoother = ezBlender(arc1, blendOne)
print(smoother)
curveList = mirrorObjectInQuadrants(smoother, x, y)


curveList = (yLine, offsetLine, blendOne, blendTwo)
border = rs.JoinCurves(curveList)




print(border)
