import gdsfactory as gf
import components.markers as markers

from gdsfactory.generic_tech import get_generic_pdk
from layer_map import LayerMapUDNF

generic_pdk = get_generic_pdk()

LAYER_MAP = LayerMapUDNF()
bosonian_PDK = gf.Pdk(name="bosonian-PDK",
                  layers=dict(LAYER_MAP),
                  base_pdk=generic_pdk)

bosonian_PDK.activate()

test_die = markers.UDNF_10mm_die('test_id')
test_die.show()