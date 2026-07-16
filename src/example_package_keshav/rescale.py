"""Helpers for rescaling numeric data."""

from __future__ import annotations

import numpy as np


def rescale(values: np.ndarray) -> np.ndarray:
	"""Rescale an array to the range 0 to 1."""
	values = np.asarray(values)
	minimum = values.min()
	maximum = values.max()

	if maximum == minimum:
		return np.zeros_like(values, dtype=float)

	return (values - minimum) / (maximum - minimum)
