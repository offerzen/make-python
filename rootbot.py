import root
from commands import command

@command('list all phone brands')
def list_all_phone_brands(message):
    try:
        result = root.list_gadget_models()
        brands = set([phone['make'] for phone in result])
        response = "The phone brands are:\n%s" % '\n'.join(brands)
    except root.RootException:
        response = "An error occurred. Please try again."

    return response


@command('list all the phones made by (.*)')
def list_all_phones_by_brand(message, brand):
    try:
        result = root.list_gadget_models()
        phones = set([phone['name'] for phone in result if phone['make'] == brand])
        response = "The phones made by %s are:\n%s" % (brand, '\n'.join(phones))
    except root.RootException:
        response = "An error occurred. Please try again."

    return response


@command('what is the value of a (.*)')
def get_phone_value(message, phone):
    try:
        result = root.list_gadget_models()
        matching_phones = list(filter(lambda p: p['name'] == phone, result))
        response = "The value of a %s is R%.2f" % (phone, matching_phones[0]['value']/100)
    except root.RootException:
        response = "An error occurred. Please try again."
    return response
