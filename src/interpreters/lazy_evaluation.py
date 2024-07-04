from src.interpreters.expressions import do


def do_comment(env, args):
    """Ignore instructions.
    ["comment" "text"] => None
    """
    return None


def do_if(env, args):
    """Make a choice: only one sub-expression is evaluated.
    ["if" C A B] => A if C else B
    """
    assert len(args) == 3
    cond = do(env, args[0])
    choice = args[1] if cond else args[2]
    return do(env, choice)
