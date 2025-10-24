from typing import Literal

from .ThickElement import ThickElement
from ..parameters import MagneticMultipoleParameters


class Sextupole(ThickElement):
    """A sextupole element"""

    # Discriminator field
    kind: Literal["Sextupole"] = "Sextupole"

    # Magnetic multipole parameters
    MagneticMultipoleP: MagneticMultipoleParameters