# UAV sizing tools

## Files
- `predim.ipynb` : initial sizing, helps determining $W/S$ and $P/W$
- `input.py` : defines the properties than remain constant : wing dimensions, mass...
- `tailplane.ipynb` : sizes the horizontal and vertical stabilisers using the tailplane volume coefficients method
- `aerodynamic_centre.ipynb` : computes the longitudinal location of the neutral point for a given wing-tailplane configuration. **MUST BE RENAMED TO `neutral_point.ipynb`**
- `parasitic_drag.ipynb` : using Raymer's component buildup method, computes the parasitic drag coefficent $C_{D0}$
- `flaps.ipynb` : provides an estimation of the spanwise length of flaps required to achieve the targat $C_{Lmax}$
- `sizing_functions.py` : sets all other Jupyter Notebooks into functions than can be used for sizing loops

## References

- _General Aviation Aircraft Design. Applied Methods and Procedures_, Snorri Gudmundsson
- _Conceptual Aircraft Design_, Daniel P. Raymer

