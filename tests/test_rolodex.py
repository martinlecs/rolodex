from rolodex import rolodex

TEST_RECORDS: list[rolodex.Record] = [
    {"name": "Martin", "address": "Address is here", "phone_number": "1231312321312"},
    {"name": "Random12", "address": "a masmdlamsda", "phone_number": "123213213123"},
    {"name": "asdasd", "address": "lkjasdnklads", "phone_number": "1212-1221-12121"},
]


def test_init():
    assert len(rolodex.Rolodex().records) == 0
    assert rolodex.Rolodex([TEST_RECORDS[0]]).records == [TEST_RECORDS[0]]


def test_add_records_from_dicts():
    rolo = rolodex.Rolodex()
    rolo.add_records_from_dicts(TEST_RECORDS)
    assert len(rolo.records) == len(TEST_RECORDS)
    assert rolo.records[0] == TEST_RECORDS[0]
    assert rolo.records[1] == TEST_RECORDS[1]
    assert rolo.records[2] == TEST_RECORDS[2]


def test_add_records_from_string():
    rolo = rolodex.Rolodex()
    rolo.add_records_from_string(["mike,random addy,555-555-555", "opi,a s d a d,1231231"])
    assert len(rolo.records) == 2
    assert rolo.records[0] == {"name": "mike", "address": "random addy", "phone_number": "555-555-555"}
    assert rolo.records[1] == {"name": "opi", "address": "a s d a d", "phone_number": "1231231"}


def test_filter_records():
    records1 = rolodex.Rolodex(TEST_RECORDS).filter_records("name", "*12").records
    assert len(records1) == 1
    assert records1[0] == {"name": "Random12", "address": "a masmdlamsda", "phone_number": "123213213123"}

    records2 = rolodex.Rolodex(TEST_RECORDS).filter_records("address", "*res*").records
    assert len(records2) == 1
    assert records2[0] == {"name": "Martin", "address": "Address is here", "phone_number": "1231312321312"}

    records3 = rolodex.Rolodex(TEST_RECORDS).filter_records("phone_number", "*8*").records
    assert len(records3) == 0


def test_filter_chain():
    rolo = (
        rolodex.Rolodex(TEST_RECORDS)
        .filter_records("name", "*a*")
        .filter_records("address", "*l*")
        .filter_records("phone_number", "1212-*")
    )

    assert len(rolo.records) == 1
    assert rolo.records[0] == {"name": "asdasd", "address": "lkjasdnklads", "phone_number": "1212-1221-12121"}
