import mock
from urllib2 import HTTPError

from layman import LaymanTranslator


class ExampleTranslator(LaymanTranslator):
    """
    Given a list of possible exceptions, this class implements an API to help translate them into friendly
    error messages for the end user
    """

    def __init__(self):

        # This is the explicit list of exceptions we know how to translate
        self.exceptions = [
            HTTPError,
            IndexError,
        ]

    def translate_HTTPError(self, exception):
        """
        Method that actually translates the HTTPError into something user friendly
        """

        status_codes = {
            404: 'The remote file could not be found.',
            403: 'Access to the remote file was denied.',
        }

        if exception.code in status_codes:
            return status_codes[exception.code]

        return "The server responded with %s" % exception.msg

    def translate_IndexError(self, exception):
        """
        Method that actually translates the IndexError into something user friendly
        """
        return "We hit an IndexError"


def example_error_tranlation():

    # Instantiate the translator
    et = ExampleTranslator()

    # Create a method that throws an exception
    mock_method = mock.Mock()
    mock_method.side_effect = HTTPError(code=404, msg="Test 404 error mesage")

    try:
        mock_method()
    except ExampleTranslator.as_tuple() as e:
        print et.handle_exception(e)
