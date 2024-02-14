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

arc1 = rs.AddArc3Pt(arcRatioPointLowLeft, arcRatioPointMidLeft, arcRatioPointTopLeft)
arc2 = rs.MirrorObject(arc1, ((x/2),0,0), ((x/2),y,0))



curveList = (yLine, offsetLine, blendOne, blendTwo)
border = rs.JoinCurves(curveList)
print(border)
