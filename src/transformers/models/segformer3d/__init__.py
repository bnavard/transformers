"""SegFormer3D model implementation"""

from typing import TYPE_CHECKING

from transformers.utils import (
    OptionalDependencyNotAvailable,
    _LazyModule,
    is_torch_available,
)

_import_structure = {
    "configuration_segformer3d": ["SegFormer3DConfig"],
}

try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_segformer3d"] = [
        "SegFormer3DModel",
        "SegFormer3DPreTrainedModel",
    ]

if TYPE_CHECKING:
    from .configuration_segformer3d import SegFormer3DConfig
    from .modeling_segformer3d import SegFormer3DModel, SegFormer3DPreTrainedModel

else:
    import sys

    sys.modules[__name__] = _LazyModule(
        __name__,
        globals()["__file__"],
        _import_structure,
        module_spec=__spec__,
    )
