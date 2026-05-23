"""CadQuery - A parametric 3D CAD scripting framework.

CadQuery is an intuitive, easy-to-use Python module for building parametric 3D CAD models.
It is analogous to OpenSCAD, but uses Python instead of a custom language.

CadQuery has several goals:
    - Build models with scripts that are as close as possible to how you'd describe the object to a human.
    - Create parametric models that can be easily customized by end users.
    - Output high quality CAD formats such as STEP and AMF in addition to traditional STL.
    - Provide a clean, easy-to-use API that is not tied to any CAD kernel.

Example usage::

    import cadquery as cq

    result = cq.Workplane("XY").box(1, 2, 3)
    cq.exporters.export(result, "box.step")

Personal fork notes:
    - Using this fork for learning CadQuery internals and experimenting with custom shapes.
    - See the examples/ directory for personal project scripts.
    - Added `cq.show` as a convenience alias for quick REPL inspection (prints object info).
"""

from .cq import Workplane, CQContext
from .assembly import Assembly, Constraint
from .sketch import Sketch
from .selectors import (
    NearestToPointSelector,
    ParallelDirSelector,
    DirectionSelector,
    PerpendicularDirSelector,
    TypeSelector,
    DirectionMinMaxSelector,
    CenterNthSelector,
    RadiusNthSelector,
    LengthNthSelector,
    AreaNthSelector,
    StringSyntaxSelector,
)
from .occ_impl.geom import Vector, Matrix, Plane, Location
from .occ_impl.shapes import (
    Shape,
    Vertex,
    Edge,
    Wire,
    Face,
    Shell,
    Solid,
    Compound,
)
from . import exporters
from . import importers
from . import selectors

__version__ = "2.5.0.dev0"
__author__ = "CadQuery Contributors"
__license__ = "Apache License 2.0"


def show(obj):
    """Personal convenience helper: print a summary of a CadQuery object.

    Useful for quick inspection in the REPL without needing a full viewer.
    """
    if isinstance(obj, Workplane):
        solids = obj.solids().vals()
        print(f"<Workplane: {len(obj.vals())} object(s), {len(solids)} solid(s)>")
    else:
        print(repr(obj))


__all__ = [
    "Workplane",
    "CQContext",
    "Assembly",
    "Constraint",
    "Sketch",
    "Vector",
    "Matrix",
    "Plane",
    "Location",
    "Shape",
    "Vertex",
    "Edge",
    "Wire",
    "Face",
    "Shell",
    "Solid",
    "Compound",
    "NearestToPointSelector",
    "ParallelDirSelector",
    "DirectionSelector",
    "PerpendicularDirSelector",
    "TypeSelector",
    "DirectionMinMaxSelector",
    "CenterNthSelector",
    "RadiusNthSelector",
    "LengthNthSelector",
    "AreaNthSelector",
    "StringSyntaxSelector",
    "exporters",
    "importers",
    "selectors",
    "show",
]
