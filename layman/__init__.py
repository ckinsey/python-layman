class LaymanTranslator(object):
    """
    Given a list of possible exceptions, this class implements an API to help translate them into friendly
    error messages for the end user
    """

    # Explicit list of exceptions we can translate
    exceptions = []

    def __init__(self):
        pass

    def as_tuple(self):
        return tuple(e for e in self.exceptions)

    def handle_exception(self, e):
        """
        Handles the particular exception from self.as_tuple() that was caught.  Since the exception was defined in
        our list of translations there should be an appropriate translation method.  If not we raise a
        NotImplementedError

        *Sample Usage*
        try:
            some_expression
        catch ExceptionTranslator.as_tuple() as e:
            error_message = ExceptionTranslator.handle_exception(e)

        """
        trans_method = 'translate_%s' % e.__class__.__name__

        if hasattr(self, trans_method):
            return getattr(self, trans_method)(e)
        else:
            raise NotImplementedError(trans_method)
