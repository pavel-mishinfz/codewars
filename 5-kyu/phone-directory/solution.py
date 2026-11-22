import re


def phone(string, num):
    pattern = r'.*(\+' + re.escape(num) + r').*\n'
    matches = re.findall(pattern, string)
    if len(matches) == 0:
        return f'Error => Not found: {num}'
    elif len(matches) > 1:
        return f'Error => Too many people: {num}'
    else:
        phone_pattern = fr'\+({re.escape(num)})'
        name_pattern = r'<(.+)>'

        target_str = re.search(pattern, string).group()
        phone_number = re.search(phone_pattern, target_str).group(1)
        name = re.search(name_pattern, target_str).group(1)

        raw_address = re.sub(phone_pattern, '', target_str)
        raw_address = re.sub(name_pattern, '', raw_address)
        spec_symbols = ['*', '/', ';', ':', '!', '?', '$', '%', '#', ',']
        for symbol in spec_symbols:
            raw_address = raw_address.replace(symbol, '')
        raw_address = raw_address.replace('_', ' ')
        address = ' '.join(raw_address.split())
        return f'Phone => {phone_number}, Name => {name}, Address => {address}'