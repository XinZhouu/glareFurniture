from flask import Flask
import ghhops_server as hs

import rhino3dm

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/pointat",
    name = "PointAt",
    description = "get point along curve",
    #icon = ".png",
    inputs = [
        hs.HopsCurve("Curve", "C", "Curve to evaluate"),
        hs.HopsNumber("t", "t", "Parameters on Curve to evaluate", default = 2.0),
    ],
    outputs = [hs.HopsPoint("P", "P", "Point on curve at t")],
)
def pointat(curve, t):
    return curve.PointAt(t)

if __name__ == "__main__":
    app.run()