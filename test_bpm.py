import pytest
from bpm.bpm import BPMCounter


@pytest.fixture
def bpm_counter():
    bpm_counter = BPMCounter()
    return bpm_counter


@pytest.fixture
def average_array(bpm_counter):
    average_array = bpm_counter.average_array
    return average_array


@pytest.fixture
def get_bpm(bpm_counter):
    get_bpm = bpm_counter.get_bpm
    return get_bpm


"""
count tests
"""


@pytest.mark.count
def test_count_exists(bpm_counter):
    bpm_counter.reset()
    bpm_counter.count(1.0)


@pytest.mark.count
def test_count_outputs_something(bpm_counter):
    bpm_counter.reset()
    assert bpm_counter.count(1.0) is not None


@pytest.mark.count
def test_count_outputs_floar(bpm_counter):
    bpm_counter.reset()
    assert type(bpm_counter.count(1.0)) is float


@pytest.mark.count
def test_count_takes_integer_as_input(bpm_counter):
    bpm_counter.reset()
    bpm_counter.count(1.0)


@pytest.mark.count
def test_count_durations_exists(bpm_counter):
    bpm_counter.reset()
    assert type(bpm_counter.durations) is list


@pytest.mark.count
def test_count_durations_empty_on_init(bpm_counter):
    bpm_counter.reset()
    assert bpm_counter.durations == []


@pytest.mark.count
def test_count_push_to_durations(bpm_counter):
    bpm_counter.reset()
    bpm_counter.count(1.0)
    assert bpm_counter.durations == [1.0]


"""
reset tests
"""


@pytest.mark.reset
def test_reset_clears_array(bpm_counter):
    bpm_counter.reset()
    bpm_counter.count(1.0)
    bpm_counter.reset()
    assert bpm_counter.durations == []


"""
average_array tests
"""


@pytest.mark.average_array
def test_average_array_exists(average_array):
    average_array([1.0, 2.0, 3.0])


@pytest.mark.average_array
def test_average_array_input_list(average_array):
    average_array([1.0, 2.0, 3.0])


@pytest.mark.average_array
def test_average_array_input_list_of_floats(average_array):
    average_array([1.0, 2.0, 3.0])


@pytest.mark.average_array
def test_average_array_input_list_of_not_floats(average_array):
    with pytest.raises(TypeError):
        average_array([1, 2, 3])


@pytest.mark.average_array
def test_avaerage_array_returns_float(average_array):
    avg = average_array([1.0, 2.0, 3.0])
    assert type(avg) is float


@pytest.mark.average_array
def test_avaerage_array_returns_correct_value(average_array):
    avg = average_array([1.0, 2.0, 3.0])
    assert avg == 2.0


"""
get_bpm tests
"""


@pytest.mark.get_bpm
def test_get_bpm_exists(get_bpm):
    pass


@pytest.mark.get_bpm
def test_get_bpm_returns_float(bpm_counter):
    bpm_counter.count(1.0)
    bpm_counter.count(1.0)
    bpm_counter.count(1.0)
    bpm_counter.count(1.0)
    bpm = bpm_counter.get_bpm()
    assert type(bpm) is float
    bpm_counter.reset()


@pytest.mark.get_bpm
def test_get_bpm_returns_correct_value(bpm_counter):
    bpm_counter.reset()
    bpm_counter.count(0.0)
    bpm_counter.count(1.0)
    bpm = bpm_counter.get_bpm()
    assert bpm == 120
    bpm_counter.reset()
