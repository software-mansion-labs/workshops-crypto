from pymerkle import MerkleTree
import random
def prover_tests(prover_class):
    graph = [
        [0,1,0,1],
        [1,0,1,0],
        [0,1,0,1],
        [1,0,1,0]
    ]
    prover = prover_class(graph)
    hash_root = prover.commitment_phase()
    test_permutation_challange(prover, hash_root)
    test_cycle_challange(prover, hash_root)


def test_permutation_challange(prover, hash_root):
    tree = MerkleTree()

    permutation = prover.permutation_challange()
    # from seed
    permutation = [2, 0, 3, 1]
    correct_p = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 0]
    ] 
    for v in  [item for sublist in correct_p for item in sublist]:
        tree.encrypt(str.encode(str(v)))

    # Check if commit is correct
    assert hash_root == tree.get_root_hash()

def test_cycle_challange(prover, hash_root):
    tree = MerkleTree()
    correct_p = [
        [0, 0, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 0]
    ] 
    for v in  [item for sublist in correct_p for item in sublist]:
        tree.encrypt(str.encode(str(v)))

    cycle_challange = prover.cycle_challange()

    assert cycle_challange[0] == ([2,1], tree.generate_audit_path(9))
    assert cycle_challange[1] == ([1,3], tree.generate_audit_path(7))
    assert cycle_challange[2] == ([3,0], tree.generate_audit_path(12))
    assert cycle_challange[3] == ([0,2], tree.generate_audit_path(2))