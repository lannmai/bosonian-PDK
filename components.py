import gdsfactory as gf

@gf.cell
def UDNF_10mm_laser_crosses() -> gf.Component:
    return 

@gf.cell
def UDNF_10mm_PAM_arrays() ->gf.Component:
    return

@gf.cell
def UDNF_10mm_EBL_squares_20um() -> gf.Component:
    return

@gf.cell
def UDNF_10mm_EBL_markers() -> gf.Component:
    return

@gf.cell
def UDNF_10mm_all_markers() -> gf.Component:
    return

@gf.cell
def UDNF_10mm_die(sample_id: str) -> gf.Component:
    return gf.components.die(size=(10000.0, 10000.0),
                             street_width=0,
                             street_length=0,
                             die_name=sample_id,
                             text_size=100.0,
                             text_location='N',
                             layer='FLOORPLAN')

@gf.cell
def label() -> gf.Component:
    return

@gf.cell
def inverse_design_coupler_wvg() -> gf.Component:
    return

@gf.cell
def etch_pit() -> gf.Component:
    return

@gf.cell
def contact_pad() -> gf.Component:
    return

@gf.cell
def grating_coupler() -> gf.Component:
    return

@gf.cell
def photonic_crystal_wvg() ->gf.Component:
    return