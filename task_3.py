import re

def normalize_phone(phone_number):
    rule = r"[^0-9+]"
    phone = re.sub(rule, "", phone_number)

    if phone.startswith("+"):
        phone = "+" + phone[1:].replace("+", "")
    else:
        phone = phone.replace("+", "")
        if phone.startswith("380"):
            phone = "+" + phone
        else:
            phone = "+38" + phone
    return phone
