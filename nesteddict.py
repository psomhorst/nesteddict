import collections


__all__ = ['nesteddict']


class nesteddict(dict):
    """Nested-aware dictionary."""

    def update(self, *args, **kwargs):
        """D.update([E, ]**F) -> None. Update D from dict/iterable E and F.

        If updated values are dictionaries, they are converted to nesteddicts
        and updated as a dictionary, in stead of being overwritten.
        """

        args = args + (kwargs, )

        for d in args:
            if not isinstance(d, collections.Mapping):
                raise TypeError(
                    "can only update with dictionaries or keyword arguments")

            for k in d:
                if isinstance(d[k], collections.Mapping):
                    r = self.get(k, {})
                    if isinstance(self[k], collections.Mapping):
                        r = self.__class__(r)
                        r.update(d[k])
                        self[k] = r
                    else:
                        self[k] = self.__class__(d[k])
                else:
                    self[k] = d[k]
            return
