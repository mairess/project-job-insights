from src.pre_built.counter import count_ocurrences


def test_counter():
    "Tests python occurrence in file"
    assert count_ocurrences("data/jobs.csv", "python") == 1639
