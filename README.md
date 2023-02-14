# UAV sizing tools

## Files
- `predim.ipynb` : initial sizing, providing constraint diagrams for $W/S$ and $P/W$
- `input.py` : defines the key parameters of the aeroplane design, that can remain constant during the sizing process : wing planform geometry, mass...
- `tailplane.ipynb` : sizes the horizontal and vertical stabilisers according to the tailplane volume coefficients method
- `aerodynamic_centre.ipynb` : computes the longitudinal location of the neutral point for a given wing-tailplane configuration. **MUST BE RENAMED TO `neutral_point.ipynb`**
- `parasitic_drag.ipynb` : using Raymer's component buildup method, computes the parasitic drag coefficent $C_{D0}$
- `flaps.ipynb` : provides an estimation of the spanwise length of flaps required to achieve the targat $C_{Lmax}$
- `sizing_functions.py` : sets all other Jupyter Notebooks into functions than can be used for sizing loops

## Variable naming
Generic : a variable containing the value of property `prop` of the component `comp` is written `comp_prop`. 
++Example :++ : The wing surface is represented by the variable `w_S`

List of component prefixes :
- `fus` : fuselage
- `w` : wing
- `ht` : horizontal tailplane
- `vt` : vertical taiplane
- `ref` : reference value

## References

- _General Aviation Aircraft Design. Applied Methods and Procedures_, Snorri Gudmundsson
- _Aircraft Design : A Conceptual Approach_, Daniel P. Raymer

