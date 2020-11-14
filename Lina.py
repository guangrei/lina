import Arjawinangun as awn
from rivescript import RiveScript


class Lina(RiveScript):
    def reply(self, user, msg, errors_as_replies=True, context={}):
        """Fetch a reply from the RiveScript brain.

        Arguments:
            user (str): A unique user ID for the person requesting a reply.
                This could be e.g. a screen name or nickname. It's used internally
                to store user variables (including topic and history), so if your
                bot has multiple users each one should have a unique ID.
            msg (str): The user's message. This is allowed to contain
                punctuation and such, but any extraneous data such as HTML tags
                should be removed in advance.
            errors_as_replies (bool): When errors are encountered (such as a
                deep recursion error, no reply matched, etc.) this will make the
                reply be a text representation of the error message. If you set
                this to ``False``, errors will instead raise an exception, such as
                a ``DeepRecursionError`` or ``NoReplyError``. By default, no
                exceptions are raised and errors are set in the reply instead.

        Returns:
            str: The reply output.
        """
        ret = self._brain.reply(user, msg, errors_as_replies)
        return awn.render(ret, context)
