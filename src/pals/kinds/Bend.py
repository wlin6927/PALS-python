from typing import Literal, Optional

from .ThickElement import ThickElement
from ..parameters import MagneticMultipoleParameters
from ..parameters import BendParameters

class Sbend(ThickElement):
    """A sector bend element (Sbend)

    Attributes
    ----------
    kind : Literal["Sbend"]
        Element type discriminator.
    BendP : BendParameters
        Required bend parameters defining the dipole geometry and field.
    MagneticMultipoleP : Optional[MagneticMultipoleParameters]
        Optional magnetic multipole parameters.
        Can be omitted if the bend has no additional multipole field components.
    """

    # Discriminator field
    kind: Literal["Sbend"] = "Sbend"

    # Bend parameters
    BendP: BendParameters

    # Optional magnetic multipole parameters
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None

class Rbend(ThickElement):
    """A rectangular bend element (Rbend)

    Attributes
    ----------
    kind : Literal["Rbend"]
        Element type discriminator.
    BendP : BendParameters
        Required bend parameters defining the dipole geometry and field.
    MagneticMultipoleP : Optional[MagneticMultipoleParameters]
        Optional magnetic multipole parameters.
        Can be omitted if the rectangular bend has no additional multipole field components.
    """

    # Discriminator field
    kind: Literal["Rbend"] = "Rbend"

    # Bend parameters
    BendP: BendParameters

    # Optional magnetic multipole parameters
    MagneticMultipoleP: Optional[MagneticMultipoleParameters] = None