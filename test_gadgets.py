import root


def test_list_gadget_models():
    gadgets = root.list_gadget_models()
    # Not null
    assert gadgets
    # Resulting list longer than 0
    assert len(gadgets) > 0
    # Tests for any Apple Products
    assert any(['Apple' in x['make'] for x in gadgets])
    # Test should have at least one iPhone or more in test_list_gadget_models
    assert any(['iPhone' in x['name'] for x in gadgets])
