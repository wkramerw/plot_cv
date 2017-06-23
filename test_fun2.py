def n_neg(seq):
    """Number of negative residues a protein sequence"""

    # Convert sequence to upper case
    seq = seq.upper()

    # Count E's and D's, since these are the negative residues
    return seq.count('E') + seq.count('D')

def test_n_neg():
    """Perform unit tests on n_neg."""

    assert n_neg('E') == 1
    assert n_neg('D') == 1
    assert n_neg('') == 0
    assert n_neg('acktywtta') == 0
    assert n_neg('ACKLWTTAE') == 1
    assert n_neg('DDDDEEEE') == 8
    assert n_neg('acklwttae') == 1
