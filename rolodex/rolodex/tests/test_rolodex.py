from rolodex.rolodex.rolodex import Record, Rolodex

TEST_RECORDS: list[Record] = [
    {"name": "Martin", "address": "Address is here", "phone_number": "1231312321312"},
    {"name": "Random12", "address": "a masmdlamsda", "phone_number": "123213213123"},
    {"name": "asdasd", "address": "lkjasdnklads", "phone_number": "1212-1221-12121"},
]


def test_init():
    assert len(Rolodex().records) == 0
    assert Rolodex([TEST_RECORDS[0]]).records == [TEST_RECORDS[0]]


def test_add_records():
    rolodex = Rolodex()
    rolodex.add_records(TEST_RECORDS)
    assert len(rolodex.records) == len(TEST_RECORDS)


def test_filter_records():
    rolodex = Rolodex(TEST_RECORDS)

    res1 = rolodex.filter_records("name", "*12")
    assert len(res1) == 1
    assert res1[0]["name"] == "Random12"
    assert res1[0]["address"] == "a masmdlamsda"
    assert res1[0]["phone_number"] == "123213213123"

    res2 = rolodex.filter_records("address", "*res*")
    assert len(res2) == 1
    assert res2[0]["name"] == "Martin"
    assert res2[0]["address"] == "Address is here"
    assert res2[0]["phone_number"] == "1231312321312"

    res3 = rolodex.filter_records("phone_number", "1*")
    assert len(res3) == len(TEST_RECORDS)
