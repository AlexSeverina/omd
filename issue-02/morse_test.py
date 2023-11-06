import pytest as pytest
from morse import decode


@pytest.mark.parametrize("test_input,expected",
                         [('... --- ...', 'SOS'),
                          ('... .- .. .--. .--. ..- .- -.- .. ...'
                           '- .. -.- .- ..- .--. .--. .. .- ...',
                           'SAIPPUAKIVIKAUPPIAS'),
                          ('... .... .-.. -.-- .- .--. .-', 'SHLYAPA')])
def test_decode(test_input, expected):
    """
    Test function for morse decode funtion.

    :param test_input: Input for decode function.
    :param expected: Expected output from decode function
    for the corresponding input.
    """
    assert decode(test_input) == expected


if __name__ == '__main__':
    print('File for testing decode function.')
