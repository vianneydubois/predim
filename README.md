# UAV sizing and analysis tools

## Files

### For sizing and analysis process
- `predim.ipynb` : initial sizing, provides constraint diagrams for $W/S$ and $P/W$
- `input.py` : defines the values of key parameters for the aeroplane design, that can remain constant during the sizing process : wing planform geometry, aerofoils, mass...
- `sizing_functions.py` : sets all other Jupyter Notebooks into functions than can be used for sizing loops **(used for sizing)**
- `sizing_main.ipynb` : calls the sizing functions, plots and displays the sizing process outputs

### For test only
- `tailplane.ipynb` : sizes the horizontal and vertical stabilisers according to the tailplane volume coefficients method
- `aerodynamic_centre.ipynb` : computes the longitudinal location of the neutral point for a given wing-tailplane configuration. **MUST BE RENAMED `neutral_point.ipynb`
- `parasitic_drag.ipynb` : using Raymer's component buildup method, computes the parasitic drag coefficent $C_{D0}$
- `flaps.ipynb` : provides an estimation of the spanwise length of flaps required to achieve the targat $C_{Lmax}$
- `ailerons.ipynb` : computes the aileron edge inboard spanwise station for a given manoeuvring criteria
- 'landing_gear.ipynb' : analyses an undercarriage geometry : overturn angle, nose landing gear loading, max tipback angle

## Variables naming and notation
A variable containing the value of property `prop` of the component `comp` is written `comp_prop`. "Components" can be virtual, see `ref`or `np`. 
_Example :_ The wing surface area is represented by the variable `w_S`

List (non exhaustive) of component prefixes :
- `fus` : fuselage
- `w` : wing
- `ht` : horizontal tailplane
- `vt` : vertical taiplane
- `ref` : reference value (for $S_{ref}$, $c_{ref}$, ...)
- `np` : neutral point

Be careful reading lift coefficients :
- `C_l` : **aerofoil** lift coefficient
- `C_L` : **wing** lift coefficient

Roll coefficients :
- `C_roll` is the roll moment coefficient usually written $C_l$
- `C_roll_delta_a` is the aileron roll control derivative $\dfrac{\partial C_l}{\partial \delta_A}$ usually written $C_{l,\delta_A}$

## References

- _General Aviation Aircraft Design. Applied Methods and Procedures_, Second Edition, Snorri Gudmundsson, 2021
- _Aircraft Design : A Conceptual Approach_, Sixth Edition, Daniel P. Raymer, 2018
- _Aérodynamique Avancée de l'Avion_, lecture notes, Jean-Marc Moschetta, 2022
- _Summary of Low-Speed Airfoil Data_, Volume 2, Michael S. Selig, Christopher A. Lyon, Philippe Giguere, Cameron P. Ninham, James J. Guglielmo, 1996

## Contact
* Vianney Dubois : vianney.dubois[at]student.isae-supaero.fr
