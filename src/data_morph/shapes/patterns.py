"""Shapes that are patterns of lines."""

from .lines import Lines


class HighLines(Lines):
    """Class for the high lines shape."""

    def __init__(self, data) -> None:
        q1, q3 = data.y.quantile([0.25, 0.75])

        super().__init__(
            [[0, q1], [100, q1]], [[0, q3], [100, q3]]
        )  # TODO: figure out way to get 0, 100 min/max plus offset?
        # TODO q1, q3 works better on some datasets than others (might need to move it a little)

    def __repr__(self) -> str:
        """Return string representation of the shape."""
        return 'high_lines'


class HorizontalLines(Lines):
    """Class for the horizontal lines shape."""

    def __init__(self, data) -> None:
        # xmin, ymin = data.min()[['x', 'y']]
        # xmax, ymax = data.max()[['x', 'y']]

        super().__init__(
            *[[[0, y], [100, y]] for y in [10, 30, 50, 70, 90]]
        )  # TODO: figure out the values based on the data

    def __repr__(self) -> str:
        """Return string representation of the shape."""
        return 'h_lines'


class SlantUpLines(Lines):
    """Class for the slant up lines shape."""

    def __init__(self, data) -> None:
        # q1, q3 = data.y.quantile([0.25, 0.75])

        super().__init__(
            [[0, 0], [100, 100]],
            [[0, 30], [70, 100]],
            [[30, 0], [100, 70]],
            [[50, 0], [100, 50]],
            [[0, 50], [50, 100]],
        )  # TODO: figure out how to use the data to derive these

    def __repr__(self) -> str:
        """Return string representation of the shape."""
        return 'slant_up'


class VerticalLines(Lines):
    """Class for the vertical lines shape."""

    def __init__(self, data) -> None:
        # xmin, ymin = data.min()[['x', 'y']]
        # xmax, ymax = data.max()[['x', 'y']]

        super().__init__(
            *[[[x, 0], [x, 100]] for x in [10, 30, 50, 70, 90]]
        )  # TODO: figure out the values based on the data

    def __repr__(self) -> str:
        """Return string representation of the shape."""
        return 'v_lines'


class WideLines(Lines):
    """Class for the wide lines shape."""

    def __init__(self, data) -> None:
        q1, q3 = data.x.quantile([0.25, 0.75])

        super().__init__(
            [[q1, 0], [q1, 100]], [[q3, 0], [q3, 100]]
        )  # TODO: figure out way to get 0, 100 min/max plus offset?

    def __repr__(self) -> str:
        """Return string representation of the shape."""
        return 'wide_lines'


class XLines(Lines):
    """Class for the X shape consisting of two crossing, perpendicular lines."""

    def __init__(self, data) -> None:
        xmin, ymin = data.min()
        xmax, ymax = data.max()

        super().__init__([[xmin, ymin], [xmax, ymax]], [[xmin, ymax], [xmax, ymin]])

    def __repr__(self) -> str:
        """Return string representation of the shape."""
        return 'x'
