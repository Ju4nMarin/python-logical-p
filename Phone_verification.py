import phonenumbers


def phone_val(telefono_str, code=None):
    try:
        telefono = phonenumbers.parse(telefono_str,code)
        return phonenumbers.is_valid_number(telefono)
    except Exception as e:
        print(e)
        return False


valido = phone_val("3033457211")
print(valido)