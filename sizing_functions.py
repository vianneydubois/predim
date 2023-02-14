import numpy as np
from input import *

#---- TAILPLANE ----
def tailplane_sizing(ht_V, ht_arm, ht_AR, ht_taper, \
        vt_V, vt_arm, vt_AR, vt_taper, \
        ref_S, ref_chord, ref_span):

    # horizontal and vertical stabilisers : surface area
    ht_S = ht_V * ref_S * ref_chord / ht_arm
    vt_S = vt_V * ref_S * ref_span / vt_arm


    # horizontal and vertical stabilisers : span
    # tip-to-tip for horizontal
    # root to tip for vertical
    ht_span = np.sqrt(ht_AR*ht_S)
    vt_span = np.sqrt(vt_AR*vt_S)

    # horizontal and vertical stabilisers : root chord
    ht_root_chord = 2 * ht_S/ht_span/(1+ht_taper)
    vt_root_chord = 2 * vt_S/vt_span/(1+vt_taper)

    return [[ht_S, ht_span, ht_root_chord],[vt_S, vt_span, vt_root_chord]]

#---- TE FLAPS ----
def flaps_sizing(flaps_chord_fraction, foil_C_l_max):
    # WING
    w_C_L_max_clean = 0.9*w_C_l_max_clean # for zero sweep angle

    # targeted wing lift increase
    w_Delta_C_L_target = w_C_L_max_target - w_C_l_max_clean

    w_S_flapped = w_S * w_Delta_C_L_target / 0.9 / foil_C_l_max

    w_span_flapped = w_S_flapped / (flaps_chord_fraction * w_chord)

    w_flaps_span_stations = [2*y/w_span for y in [fus_width/2, fus_width/2 + w_span_flapped/2]]
    
    return w_flaps_span_stations

#---- NEUTRAL POINT ----
def neutral_point(ht_arm, ht_S, ht_AR):

    #---- AERODYNAMICS ----
    # /!\ Aerodynamic coefficients are nondimensionalied using the local characteristic dimension, not ref_S
    # Ex : fot the HTP, C_L_alpha is nondimensionalised by ht_S, not w_S

    # wing lift gradient coefficient
    w_C_L_alpha = np.pi * w_AR / (1 + np.sqrt(1 + (np.pi * w_AR / w_C_l_alpha)**2) )
    # wing AC position
    w_AC_x = 0.25*w_chord

    # ht lift gradient coefficient /!\ : non-dimensionalised with Sref = ht_S
    ht_C_L_alpha = np.pi * ht_AR / (1 + np.sqrt(1 + (np.pi * ht_AR / ht_C_l_alpha)**2) )
    # ht AC position
    ht_AC_x = w_AC_x + ht_arm

    # ht efficiency -- should be around 0.6-0.75
    ht_eta = 1 - 8*w_C_L_alpha/np.pi**3/w_AR * (1 + 1/np.cos(np.arctan(w_span*np.pi/8/ht_arm)))

    
    #---- NEUTRAL POINT
    np_x = (w_C_L_alpha*w_S*w_AC_x + ht_eta*ht_C_L_alpha*ht_S*ht_AC_x - 2*fus_volume ) \
    / (w_C_L_alpha*w_S + ht_eta*ht_C_L_alpha*ht_S )

    return np_x

#---- PARASITIC DRAG ----
def parasitic_drag(\
        V, w_x_tr, skin_roughness,\
        ht_dim, ht_x_tr, vt_dim, vt_x_tr,\
        fus_S_wet, fus_x_tr):

    ht_S, ht_span, ht_chord, ht_t_c, ht_x_c_max_t = ht_dim
    vt_S, vt_span, vt_chord, vt_t_c, vt_x_c_max_t = vt_dim


    # equivalent diameter
    fus_d_eq = np.sqrt(4*fus_height*fus_width/np.pi)

    #---------------------------
    # ---- USEFUL FUNCTIONS ----
    #---------------------------

    # flat plate laminar friction coefficient
    def C_f_lam(Re):
        return 1.328/np.sqrt(Re)

    # flat plate turbulent friction coefficient
    def C_f_turb(Re):
        return 0.0442/(Re**(1/6))

    # Reynolds number at sea level conditions
    def Re(V, l):
        return 1.225*V*l/1.8e-5

    # cutoff Reynolds number
    def Re_cutoff (l, k):
        return 38.21 * (l/k)**1.053

    # lifting surface, pylon, strut, form factor
    def FF_wing(x_c_max, t_c):
        return 1 + 0.6/x_c_max * t_c + 100 * t_c**4

    # fuselage form factor
    def FF_fus(length, d_eq, geometry: str='circ', ):
        f = length/d_eq
        FF = 0.9 + 5/f**1.5 + f/400
        if geometry == 'square':
            # Raymer : 30-40% extra FF for square-sided fuselage
            return FF*1.35
        elif geometry == 'circ':
            return FF
        else :
            return FF

    # wing wetted area
    def S_wet_wing(S_exposed, t_c):
        return S_exposed * (1.977 + 0.52*t_c)

    #-----------------------
    #---- FRICTION DRAG ----
    #-----------------------

    #---- WING ----
    w_Re_cutoff = Re_cutoff(w_chord, skin_roughness)
    w_Re = Re(V, w_chord)

    if w_Re_cutoff < w_Re:
        w_Re = w_Re_cutoff

    # flat plate friction coefficient
    w_C_f = w_x_tr * C_f_lam(w_Re) + (1-w_x_tr) * C_f_turb(w_Re)

    # wing form factor
    w_FF = FF_wing(w_x_c_max_t, w_t_c)

    # wing interference factor
    w_Q = 1.0 # Raymer, for a high-mounted wing

    # wing wetted area
    w_S_wet = S_wet_wing(w_S - fus_width * w_chord, w_t_c)

    # wing parasitic drag surface
    w_S_D_0 = w_C_f * w_FF * w_Q * w_S_wet


    #---- HORIZONTAL TAILPLANE ----

    ht_Re_cutoff = Re_cutoff(ht_chord, skin_roughness)
    ht_Re = Re(V, ht_chord)

    if ht_Re_cutoff < ht_Re:
        ht_Re = ht_Re_cutoff

    # flat plate friction coefficient
    ht_C_f = ht_x_tr * C_f_lam(ht_Re) + (1-ht_x_tr) * C_f_turb(ht_Re)

    # ht form factor
    ht_FF = FF_wing(ht_x_c_max_t, ht_t_c)

    # ht interference factor
    ht_Q = 1.05 # Raymer, for a conventional tail

    # ht wetted area
    ht_S_wet = S_wet_wing(ht_S, ht_chord)

    # ht parasitic drag surface
    ht_S_D_0 = ht_C_f * ht_FF * ht_Q * ht_S_wet


    #---- VERTICAL TAILPLANE ----

    vt_Re_cutoff = Re_cutoff(vt_chord, skin_roughness)
    vt_Re = Re(V, vt_chord)

    if vt_Re_cutoff < vt_Re:
        vt_Re = vt_Re_cutoff

    # flat plate friction coefficient
    vt_C_f = vt_x_tr * C_f_lam(vt_Re) + (1-vt_x_tr) * C_f_turb(vt_Re)

    # vt form factor
    vt_FF = FF_wing(vt_x_c_max_t, vt_t_c)

    # vt interference factor
    vt_Q = 1.05 # Raymer, for a conventional tail

    # vt wetted area
    vt_S_wet = S_wet_wing(vt_S, vt_t_c)

    # vt parasitic drag surface
    vt_S_D_0 = vt_C_f * vt_FF * vt_Q * vt_S_wet


    #---- FUSELAGE ----

    fus_Re_cutoff = Re_cutoff(fus_d_eq, skin_roughness)
    fus_Re = Re(V, fus_d_eq)

    if fus_Re_cutoff < fus_Re:
        fus_Re = fus_Re_cutoff

    # flat plate friction coefficient
    fus_C_f = fus_x_tr * C_f_lam(fus_Re) + (1-fus_x_tr) * C_f_turb(fus_Re)

    # fuselage form factor
    fus_FF = FF_fus(fus_length, fus_d_eq, 'rect')

    # fuselage interference factor
    fus_Q = 1.0 # Raymer

    # fuselage wetted area
    #fus_S_wet = 2 * (fus_width + fus_height) * fus_length * 0.8 # /!\ 0.8 factor is to be adjusted !!!!

    # fuselage parasitic drag surface
    fus_S_D_0 = fus_C_f * fus_FF * fus_Q * fus_S_wet

    #---- PARASITIC FRICTION DRAG COEFFICIENT ----
    C_D_0_f = (w_S_D_0 + ht_S_D_0 + vt_S_D_0 + fus_S_D_0) / w_S


    #-------------------
    #---- MISC DRAG ----
    #-------------------

    # aft-fuselage upsweep angle separation drag
    # Neglidated for pusher propeller configuration if upsweep angle < 30 deg
    upsweep_C_D_0 = 0

    # LANDING GEAR
    # Main langind gear : MLG
    # length = 0.35m, thickness = 3mm
    mlg_leg_C_D_0 = 2 * 1.40 * (0.35*3e-3) / w_S
    mlg_wheel_C_D_0 = 2 * 0.25 * 0.0020 / w_S # assuming 20cm^2 for wheel frontal area

    # nose langing gear : NLG
    nlg_strut_C_D_0 = 1.17 * (0.25 * 1e-2) / w_S
    nlg_wheel_C_D_0 = 0.25 * (0.0020) / w_S

    # undercarriage parasitic drag (+20% for interence drag, cf Raymer)
    lg_C_D_0 = (mlg_leg_C_D_0 + mlg_wheel_C_D_0 + nlg_strut_C_D_0 +nlg_wheel_C_D_0) * 1.2

    C_D_0_misc = lg_C_D_0 + upsweep_C_D_0


    #---------------------------
    #---- PROTUBERANCE DRAG ----
    #---------------------------

    C_D_0_protuberance_factor = 1.1 # 1.05 to 1.10 (Raymer) for SE propeller aircraft


    #------------------------------
    #---- TOTAL PARASITIC DRAG ----
    #------------------------------

    C_D_0 = (C_D_0_f + C_D_0_misc) * C_D_0_protuberance_factor

    return C_D_0
