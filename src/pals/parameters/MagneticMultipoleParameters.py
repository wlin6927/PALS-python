from pydantic import BaseModel, ConfigDict, model_validator
from typing import Any, Dict


class MagneticMultipoleParameters(BaseModel):
    """Magnetic multipole parameters

    Valid parameter names:
        - Normalized normal: KnN
        - Normalized skew: KsN
        - Field normal: BnN
        - Field skew: BsN
        - Tilt: tiltN

    where N is a non-negative integer (no leading zeros except for '0').
    """

    # Allow arbitrary fields
    model_config = ConfigDict(extra="allow")

    @staticmethod
    def _validate_order(key_num: str, msg: str):
        """Ensure N in keys like 'BnN' or 'KnN' is a valid integer without leading zeros."""
        if not key_num.isdigit() or (key_num.startswith("0") and key_num != "0"):
            raise ValueError(msg)

    @model_validator(mode="before")
    def validate(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Validate that keys follow correct naming patterns."""
        valid_prefixes = ("tilt", "Bn", "Bs", "Kn", "Ks")

        for key in values:
            if key.startswith(valid_prefixes):
                # Identify the prefix type and extract numeric suffix
                for prefix in valid_prefixes:
                    if key.startswith(prefix):
                        key_num = key[len(prefix):]
                        msg = (
                            f"Invalid {prefix} parameter: '{key}'. "
                            f"Must be of the form '{prefix}N' where N is an integer (no leading zeros)."
                        )
                        cls._validate_order(key_num, msg)
                        break
            else:
                raise ValueError(
                    f"Invalid magnetic multipole parameter: '{key}'. "
                    "Parameters must be of the form 'tiltN', 'BnN', 'BsN', 'KnN', or 'KsN', "
                    "where N is an integer."
                )

        return values
