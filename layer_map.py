from pydantic import BaseModel

import gdsfactory as gf
from gdsfactory.generic_tech import LAYER, LAYER_STACK
from gdsfactory.generic_tech.get_klayout_pyxs import get_klayout_pyxs
from gdsfactory.technology import LayerLevel, LayerStack, LayerViews
from gdsfactory.generic_tech import get_generic_pdk

from gdsfactory.config import PATH

Layer = tuple[int, int] 

class LayerMap(BaseModel):
    """ 
    Inspired by “Silicon Photonics Design: From Devices to Systems Lukas Chrostowski, Michael Hochberg” and 
    University of Delaware Nanofabrication Facility's markers template.

    PAM_ARRAYS: EBL pre-alignment marker arrays.
    GaAs_P: p-doped GaAs.
    GaAs_N: n-doped GaAs.
    GaAs_I: instrinsic GaAs.
    AlGaAs_SACRIFICE: AlGaAs sacrificial layer.
    INVERSE_CPL_WG: inverse design coupler-waveguide
    MEEP: FDTD sim in Meep.
    """
    
    SUBSTRATE: Layer = (255, 0)
    FLOORPLAN: Layer = (100, 0) 
    CORNERS: Layer = (101, 0)
    PAM_ARRAYS: Layer = (105, 0) 
    SQUARES_20UM: Layer = (106, 0)
    PAM_LABELS: Layer = (107, 0)
    LASER_CROSSES: Layer = (108, 0)
    
    GaAs_P: Layer = (200, 0)
    GaAs_N: Layer = (201, 0)
    GaAs_I: Layer = (202, 0)
    AlGaAs_SACRIFICE: Layer = (203, 0)

    PAD_OPEN: Layer = (46, 0)   
    METAL1: Layer = (20, 0)
    METAL2: Layer = (30, 0)
    METAL3: Layer = (40, 0)
    METAL4: Layer = (50, 0)
    METAL5: Layer = (60, 0)
    
    LABEL: Layer = (199, 0)
    
    INVERSE_CPL_WG: Layer = (0, 0)
    UNDERCUT: Layer = (5, 0)
    SHALLOW_ETCH: Layer = (21, 0)
    DEEP_ETCH: Layer = (22, 0)

    MEEP: Layer = (30, 1)


    