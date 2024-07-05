from backend.util.hex_to_binary import hex_to_binary

def test_hex_to_binary():
    original_num = 789
    hex_num = hex(original_num)[2:]
    binary_number = hex_to_binary(hex_num)

    assert int(binary_number,2) == original_num


