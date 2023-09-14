import gdsfactory as gf
import components

from gdsfactory.generic_tech import get_generic_pdk
from layer_map import LayerMapUDNF

generic_pdk = get_generic_pdk()

LAYER_MAP = LayerMapUDNF()
UDNF_PDK = gf.Pdk(name="UDNF",
                  layers=dict(LAYER_MAP),
                  base_pdk=generic_pdk)

UDNF_PDK.activate()

test_die = components.UDNF_10mm_die('test_id')
test_die.show()