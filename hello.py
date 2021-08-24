

def test_function(number):
        try:
                return int(number) + 5
        except ValueError as err:
                return err
