from array_insert_shift.array_insert_shift import insert_shift_array
def test_even_array():
    array = [1,5,4,6]
    new_val=7
    actual=insert_shift_array(array,new_val)
    expected = [1,5,7,4,6]
    assert actual == expected
    

def test_odd_array():
    array=[1,5,7,6,8]
    newVal=10
    actual=insert_shift_array(array,newVal)
    expected= [1,5,7,10,6,8]
    assert actual==expected
    