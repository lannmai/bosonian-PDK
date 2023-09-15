import gdsfactory as gf

@gf.cell
def deep_etch_pit(size: tuple(int, int)) -> gf.Component:
    return gf.components.rectangle(size=size,
                                   layer='DEEP_ETCH')

@gf.cell
def shallow_etch_pit(size: tuple(int, int)) -> gf.Component:
    return gf.components.rectangle(size=size,
                                   layer='SHALLOW_ETCH')

@gf.cell
def p_contact(size: tuple(int, int)) -> gf.Component:
    return gf.components.pad(size=size, 
                             layer='P_CONTACT')

@gf.cell
def n_contact(size: tuple(int, int)) -> gf.Component:
    return gf.components.pad(size=size, 
                             layer='N_CONTACT')