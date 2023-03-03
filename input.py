#---- FUSELAGE ----
fus_width = 0.252
fus_height = 0.252
fus_length = 3
fus_nose_length = 0.21
fus_tail_length = 0.5445

# nose = half sphere, tail = square base pyramid
fus_volume = 0.5 * 4/3 * 3.142 * (fus_width/2)**3 \
    + (fus_length - fus_nose_length - fus_tail_length) * fus_width * fus_height \
    + (fus_width * fus_height) * fus_tail_length /3

# nose = half spehere, tail = 4 isoceles triangles
fus_S_wet = 0.5 * 4 * 3.142 * (fus_width/2)**2 \
    + (fus_length - fus_nose_length - fus_tail_length) * (2 * fus_width + 2 * fus_height) \
    + 2 * fus_width*fus_tail_length/2 + 2 * fus_height*fus_tail_length/2

fus_upsweep = 10 # /!\ upsweep angle (following the CENTRELINE) in DEGREES

#---- PERFORMANCE ----
mtow = 24 # kg
w_C_L_max_target = 2.1 # lift requirement 

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

#---- LANDING GEAR ----
#lg_height = 0.25
lg_wheel_diam = 0.10
lg_wheel_thickness = 0.02
lg_main_strut_thickness = 3e-3 # thickness of MLG strut
lg_nose_leg_diam = 10e-3 # diameter of NLG leg
#lg_nose_x = -1.0 # NLG x position
#lg_main_x = 0.5 # MLG x position
#lg_track = 0.75 # MLG track (wheel to wheel distance)


#---- PROPELLER ----
prop_diameter = 0.5 # propeller diameter
prop_axis_z = -0.035 # propeller shaft axis z postion

#---- MISC -----
skin_roughness = 0.634e-5 # [m], for smooth paint (Raymer)
cg_z = - fus_height/2 # CG z position, assumed to be along the fuselage centreline
