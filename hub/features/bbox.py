# from typing import Tuple

from hub.features.features import Tensor


class BBox(Tensor):
    """`HubFeature` for a normalized bounding box.
    Output:
    bbox: Tensor of type `float32` and shape `[4,]` which contains the
          normalized coordinates of the bounding box `[ymin, xmin, ymax, xmax]`
    """

    def __init__(self, dtype="float64", chunks=None):
        """Construct the connector.
        Args:
        dtype: dtype of bbox coordinates.
        Default: 'float64'
        """
        super(BBox, self).__init__(shape=(4,), dtype=dtype, chunks=chunks)

    def get_attr_dict(self):
        """Return class attributes."""
        return self.__dict__
