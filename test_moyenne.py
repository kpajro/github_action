from moyenne import calcul_moyenne

def test_calcul_moyenne():
    assert calcul_moyenne([1,2,3]) == 2
    assert calcul_moyenne([10,20,30,40]) == 24
    assert calcul_moyenne([]) == 0