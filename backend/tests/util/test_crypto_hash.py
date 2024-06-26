from backend.util.crypto_hash import crypto_hash

def test_crypto_hash():
    #it should create the same hash with arguments of different
    # data types in any order
    assert crypto_hash(1,[2],'three') == crypto_hash('three',1,[2])
    assert crypto_hash('alvi') == '7b10702abd87f058dd6bdcc901d9087ff389b667ccc9588eee36e957b6ed3b88'
    