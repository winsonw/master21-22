MODELS_ = [{"DOMAIN": [1, 2, 3], "V": [1, 2], "T": [3], "B": [[2, 1], [3, 1]]}, {"DOMAIN": [1, 2, 3], "V": [1, 2], "T": [3], "B": [[2, 1], [3, 2]]}, {"DOMAIN": [1, 2, 3], "V": [1, 2], "T": [3], "B": [[2, 3], [3, 1]]}, {"DOMAIN": [1, 2, 3, 4], "V": [1, 2], "T": [3, 4], "B": [[2, 1], [3, 1], [4, 2]]}, {"DOMAIN": [1, 2, 3, 4], "V": [1, 2], "T": [3, 4], "B": [[2, 1], [3, 2], [4, 1]]}, {"DOMAIN": [1, 2, 3, 4], "V": [1, 2, 3], "T": [4], "B": [[2, 1], [3, 1], [4, 1]]}, {"DOMAIN": [1, 2, 3, 4], "V": [1, 2, 3], "T": [4], "B": [[2, 1], [3, 1], [4, 2]]}, {"DOMAIN": [1, 2, 3, 4], "V": [1, 2, 3], "T": [4], "B": [[2, 1], [3, 2], [4, 1]]}, {"DOMAIN": [1, 2, 3, 4], "V": [1, 2, 3], "T": [4], "B": [[2, 1], [3, 2], [4, 2]]}, {"DOMAIN": [1, 2, 3, 4], "V": [1, 2, 3], "T": [4], "B": [[2, 1], [3, 4], [4, 1]]}, {"DOMAIN": [1, 2, 3, 4], "V": [1, 2, 3], "T": [4], "B": [[2, 4], [3, 4], [4, 1]]}, {"DOMAIN": [1, 2, 3, 4, 5], "V": [1, 2, 3], "T": [4, 5], "B": [[2, 1], [3, 1], [4, 1], [5, 2]]}, {"DOMAIN": [1, 2, 3, 4, 5], "V": [1, 2, 3], "T": [4, 5], "B": [[2, 1], [3, 1], [4, 2], [5, 1]]}, {"DOMAIN": [1, 2, 3, 4, 5], "V": [1, 2, 3], "T": [4, 5], "B": [[2, 1], [3, 1], [4, 2], [5, 3]]}, {"DOMAIN": [1, 2, 3, 4, 5], "V": [1, 2, 3], "T": [4, 5], "B": [[2, 1], [3, 2], [4, 1], [5, 2]]}, {"DOMAIN": [1, 2, 3, 4, 5], "V": [1, 2, 3], "T": [4, 5], "B": [[2, 1], [3, 2], [4, 2], [5, 1]]}, {"DOMAIN": [1, 2, 3, 4, 5], "V": [1, 2, 3], "T": [4, 5], "B": [[2, 1], [3, 4], [4, 1], [5, 2]]}, {"DOMAIN": [1, 2, 3, 4, 5], "V": [1, 2, 3], "T": [4, 5], "B": [[2, 1], [3, 5], [4, 2], [5, 1]]}, {"DOMAIN": [1, 2, 3, 4, 5, 6], "V": [1, 2, 3], "T": [4, 5, 6], "B": [[2, 1], [3, 1], [4, 1], [5, 2], [6, 3]]}]
MODELS = [
    {
        'DOMAIN': {1, 2, 3},
        'V': {1, 2},
        'T': {3},
        'B': {(3,2), (2,1)}
    },
    {
        'DOMAIN': {1, 2, 3},
        'V': {1, 2},
        'T': {3},
        'B': {(3, 1), (2, 3)}
    },
    {
        'DOMAIN': {1, 2, 3},
        'V': {1, 2},
        'T': {3},
        'B': {(3, 1), (2, 1)}
    },
    {
        'DOMAIN': {1, 2, 3, 4},
        'V': {1, 2, 3},
        'T': {4},
        'B': {(4, 1), (2, 1), (3, 1)}
    },
    {
        'DOMAIN': {1, 2, 3, 4},
        'V': {1, 2, 3},
        'T': {4},
        'B': {(4, 1), (2, 4), (3, 4)}
    },
    {
        'DOMAIN': {1, 2, 3, 4},
        'V': {1, 2, 3},
        'T': {4},
        'B': {(4, 1), (2, 1), (3, 2)}
    },
    {
        'DOMAIN': {1, 2, 3, 4},
        'V': {1, 2, 3},
        'T': {4},
        'B': {(4, 1), (2, 1), (3, 4)}
    },
    {
        'DOMAIN': {1, 2, 3, 4},
        'V': {1, 2, 3},
        'T': {4},
        'B': {(4, 2), (2, 1), (3, 2)}
    },
    {
        'DOMAIN': {1, 2, 3, 4},
        'V': {1, 2, 3},
        'T': {4},
        'B': {(4, 2), (2, 1), (3, 1)}
    },
    {
        'DOMAIN': {1, 2, 3, 4},
        'V': {1, 2},
        'T': {3, 4},
        'B': {(4, 2), (1, 2), (3, 1)}
    },
    {
        'DOMAIN': {1, 2, 3, 4, 5},
        'V': {1, 2, 3},
        'T': {4, 5},
        'B': {(4, 2), (3, 5), (5, 1), (2, 1)}
    },
    {
        'DOMAIN': {1, 2, 3, 4, 5},
        'V': {1, 2, 3},
        'T': {4, 5},
        'B': {(4, 1), (5, 2), (2, 1), (3, 2)}
    },
    {
        'DOMAIN': {1, 2, 3, 4, 5},
        'V': {1, 2, 3},
        'T': {4, 5},
        'B': {(4, 1), (5, 2), (3, 1), (2, 1)}
    },
    {
        'DOMAIN': {1, 2, 3, 4, 5},
        'V': {1, 2, 3},
        'T': {4, 5},
        'B': {(4, 2), (5, 3), (2, 1), (3, 1)}
    },
    {
        'DOMAIN': {1, 2, 3, 4, 5, 6},
        'V': {1, 2, 3},
        'T': {4, 5, 6},
        'B': {(4, 1), (5, 2), (6, 3), (2, 1),(3, 1)}
    },
]

from axioms import test_axioms

if __name__ == "__main__":
    # for model in MODELS:
    #     for column in model:
    #         if column == "B":
    #             b_set = set()
    #             for b in model[column]:
    #                 b_set.add(tuple(b))
    #             model[column] = b_set
    #         model[column] = set(model[column])

    # not_e = []
    # for i in MODELS:
    #     for j in not_e:
    from random import random
    for i in range(5):
        random_index_1 = random(15)
        random_index_2 = random(15)
        s = MODELS[random_index_1]
        MODELS[random_index_1] = MODELS[random_index_2]
        MODELS[random_index_2] = s


    # with open("vegetables_and_toys_models.py", "w") as file:
    #     file.write(str(MODELS))