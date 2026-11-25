import pytest
import imaging.icc_profile_transform as mod

CASES = [
    ("transform_by_lut", (1,)),
    ("black_point_comp", (1,)),
    ("intent_select", (1,)),
    ("high_depth_intermediate", (1,)),
    ("read_per_image", (1,)),
    ("verify_after_transform", (1,)),
    ("load", (1,)),
    ("convert", (1,)),
    ("apply", (1,)),
    ("export", (1,)),
    ("validate_icc", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
