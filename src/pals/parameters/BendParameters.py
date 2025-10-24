from pydantic import BaseModel, ConfigDict, model_validator, Field
from typing import Any, Dict


class BendParameters(BaseModel):
    """Bend (dipole) element parameters (BendP)

    Defines reference and geometric parameters for sector or rectangular dipoles.
    These parameters describe the bend strength, edge angles, and geometry.

    Parameters
    ----------
    rho_ref : float = 0
        [radian] Reference bend angle.
    bend_field_ref : float = 0
        [T] Reference bend field.
    e1 : float = 0
        [radian] Entrance end pole face rotation with respect to a sector geometry.
    e2 : float = 0
        [radian] Exit end pole face rotation with respect to a sector geometry.
    e1_rect : float = 0
        [radian] Entrance end pole face rotation with respect to a rectangular geometry.
    e2_rect : float = 0
        [radian] Exit end pole face rotation with respect to a rectangular geometry.
    edge_int1 : float = 0
        [T·m] Entrance end fringe field integral.
    edge_int2 : float = 0
        [T·m] Exit end fringe field integral.
    g_ref : float = 0
        [1/m] Reference bend strength = 1 / radius_ref.
    h1 : float = 0
        Entrance end pole face curvature.
    h2 : float = 0
        Exit end pole face curvature.
    L_chord : float = 0
        [m] Chord length.
    L_sagitta : float = 0
        [m] Sagitta length (output parameter).
    tilt_ref : float = 0
        [radian] Reference tilt.
    """

    # Allow arbitrary extra fields (for flexibility / extensions)
    model_config = ConfigDict(extra="allow")

    rho_ref: float = Field(0.0, description="[radian] Reference bend angle.")
    bend_field_ref: float = Field(0.0, description="[T] Reference bend field.")
    e1: float = Field(0.0, description="[radian] Entrance end pole face rotation w.r.t. sector geometry.")
    e2: float = Field(0.0, description="[radian] Exit end pole face rotation w.r.t. sector geometry.")
    e1_rect: float = Field(0.0, description="[radian] Entrance end pole face rotation w.r.t. rectangular geometry.")
    e2_rect: float = Field(0.0, description="[radian] Exit end pole face rotation w.r.t. rectangular geometry.")
    edge_int1: float = Field(0.0, description="[T·m] Entrance end fringe field integral.")
    edge_int2: float = Field(0.0, description="[T·m] Exit end fringe field integral.")
    g_ref: float = Field(0.0, description="[1/m] Reference bend strength = 1 / radius_ref.")
    h1: float = Field(0.0, description="[1/m] Entrance end pole face curvature (TODO: define more precisely).")
    h2: float = Field(0.0, description="[1/m] Exit end pole face curvature (TODO: define more precisely).")
    L_chord: float = Field(0.0, description="[m] Chord length between entrance and exit faces.")
    L_sagitta: float = Field(0.0, description="[m] Sagitta length (output parameter — may be computed from geometry).")
    tilt_ref: float = Field(0.0, description="[radian] Reference tilt angle.")

    @model_validator(mode="before")
    def validate(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Custom validation to check parameter consistency."""
        # Check known field names
        known_fields = {
            "rho_ref", "bend_field_ref", "e1", "e2",
            "e1_rect", "e2_rect", "edge_int1", "edge_int2",
            "g_ref", "h1", "h2", "L_chord", "L_sagitta", "tilt_ref"
        }

        for key in values:
            # Skip known valid parameters
            if key in known_fields:
                continue

            # Allow extension parameters starting with 'aux_' (for custom use)
            if key.startswith("aux_"):
                continue

            # Otherwise, warn user about invalid parameter names
            raise ValueError(
                f"Invalid bend parameter: '{key}'. "
                f"Allowed parameters are {sorted(known_fields)} or user-defined 'aux_*' fields."
            )

        # # Optional: basic geometric sanity check
        # rho_ref = values.get("rho_ref", 0.0)
        # g_ref = values.get("g_ref", 0.0)
        # if rho_ref != 0.0 and g_ref != 0.0:
        #     # Check consistency between rho_ref (angle) and g_ref (1/radius)
        #     # This is not a strict error, just a check
        #     radius_est = 1.0 / g_ref
        #     if abs(rho_ref) > 1.0 and abs(radius_est) < 0.01:
        #         raise ValueError(
        #             f"Unlikely geometry: rho_ref={rho_ref} rad with g_ref={g_ref} (radius={radius_est} m)."
        #         )

        return values
