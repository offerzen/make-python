import root


def test_list_gadget_models():
    gadgets = root.list_gadget_models()
    assert gadgets
    assert len(gadgets) > 0
    assert any(['Apple' in x['make'] for x in gadgets])
    assert any(['iPhone' in x['name'] for x in gadgets])
