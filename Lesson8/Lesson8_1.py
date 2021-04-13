import re

# Используем предварительую компиляцию, потому что проверка для всех email всегда будет одна и та же
# и потенциально может пригодиться не только в функции email_parse(), но и где-то еще
# используем упрощенную версию проверки (грубо говорят что есть что-то перед @ и после что-то похожее на доменное имя)
RE_EMAIL = re.compile(r"^(\w+)@([a-zA-Z0-9\-]+\.[a-zA-Z]+)$")


def email_parse(email):
    if not RE_EMAIL.match(email):
        raise ValueError(f"Wrong Email: {email}")
    search = RE_EMAIL.search(email)
    return {
        "Username": search.group(1),
        "Domain": search.group(2)
    }


email_for_test = [
    "test@test.ru",
    "sKruchinin@inbox.com",
    "12@gmail.com",
    "vk.ru"
]

for email in email_for_test:
    try:
        email_dict = email_parse(email)
    except ValueError as e:
        print(email, " - ", e)
    else:
        print(email, " - ", email_dict)
