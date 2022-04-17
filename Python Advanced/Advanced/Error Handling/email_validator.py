class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()
approved_domains = (".com", ".bg", ".org", ".net")

while email != "End":

    # check if "@" is in email and length of name is more than 4
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    index_symbol_at = email.index("@")
    name = email[:index_symbol_at]

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    # check if "." is in email and there is domain name between "@" and "."
    if "." not in email:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    index_symbol_dot = email.index(".")
    domain_name = email[index_symbol_at + 1:index_symbol_dot]

    if len(domain_name) == 0:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    # check if email ends with valid domain
    if not email.endswith(approved_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()
