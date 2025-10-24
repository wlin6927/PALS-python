from typing import Literal

from .ThickElement import ThickElement
from ..parameters import MagneticMultipoleParameters


class Kicker(ThickElement):
    """A kicker element"""

    # Discriminator field
    kind: Literal["Kicker"] = "Kicker"

    # Magnetic multipole parameters
    MagneticMultipoleP: MagneticMultipoleParameters
