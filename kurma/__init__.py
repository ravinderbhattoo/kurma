from kurma import data, frames, lmps, structure_order


def _print(verbose, *args, **kwargs):
    if verbose:
        print(*args, **kwargs)
