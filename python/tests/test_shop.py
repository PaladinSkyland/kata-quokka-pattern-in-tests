from shop import Shop, User

def test_happy_path(default_user):
    user = default_user

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop(default_user):
    user = default_user
    user.age = 17

    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified(default_user):
    user = default_user
    user.verified = False

    assert not Shop.can_order(user)


def test_foreigners_must_be_foreign_fee(default_user, paris_address):
    user = default_user
    user.address = paris_address

    assert Shop.must_pay_foreign_fee(user)
