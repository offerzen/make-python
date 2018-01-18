from commands import command


@command('list all phone brands')
def list_all_phone_brands(message):
    brands = ["Apple", "Samsung"]
    response = "The phone brands are:\n%s" % '\n'.join(brands)

    return response


@command('list all the phones made by (.*)')
def list_all_phones_by_brand(message, brand):
    phones = ["iPhone5", "iPhone6"]
    response = "The phones made by %s are:\n%s" % (brand, '\n'.join(phones))

    return response


@command('what is the value of a (.*)')
def get_phone_value(message, phone):
    response = "The value of a %s is R%.2f" % (phone, 5000)

    return response
