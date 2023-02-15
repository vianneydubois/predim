#---- FUSELAGE ----
fus_width = 0.252
fus_height = 0.252
fus_length = 2.085
fus_S_wet = 1.6
fus_volume = 0.1
fus_upsweep = 10 # /!\ CENTRELINE upsweep angle in DEGREES

#---- PERFORMANCE ----
MTOW = 24
# lift requirement 
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
ht_t_c = 0.12
ht_x_c_max_t = 0.3

#---- VTP AEROFOIL ----
vt_t_c = 0.12
vt_x_c_max_t = 0.3

#----- LANDING GEAR
lg_height = 0.25
lg_track = 0.75 # MLG wheel to wheel distance
lg_wheel_diam = 0.10
lg_wheel_thickness = 0.02
lg_maine_strut_thickness = 3e-3 # thickness of MLG strut
lg_nose_leg_diam = 10e-3 # diameter of NLG leg


#---- MISC -----
skin_roughness = 0.634e-5 # [m], for smooth paint (Raymer)
