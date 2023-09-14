import gdsfactory as gf

path = "/home/hglan/UDNF_1cm_marker_template_v6.gds"

comp1 = gf.import_gds(path)

comp1_extr = comp1.get_polygons()

print(len(comp1_extr))