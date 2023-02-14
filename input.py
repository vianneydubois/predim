#---- FUSELAGE ----
fus_width = 0.25
fus_height = 0.25
fus_length = 2.2
fus_S_wet = 0
fus_volume = 0

#---- WEIGHT ----
MTOW = 24
# LIFT REQUIREMENTS
w_C_L_max_target = 2.1

#---- WING ----
w_AR = 8 # wing aspect ratio
w_S = 2.1 # wing surface
w_span = 4.2 # wingspan
w_chord = 0.50 # wing chord (constant for rectangular planform)

#---- WING AEROFOIL (E423) ----
# max aeroifoil lift coefficient at Re~300k
w_C_l_max_clean = 1.9 # from Selig
w_t_c = 0.125 # aerofoil thickness-to-chord ratio
w_x_c_max_t = 0.237 # aerofoil max thickness location
w_C_l_alpha = 5.85 # E423, XFOIL prediction

#---- HTP AEROFOIL ----
ht_C_l_alpha = 5