import numpy
from matchms.typing import SpectrumType


def select_by_relative_intensity(spectrum_in: SpectrumType, intensity_from=0.0, intensity_to=1.0) -> SpectrumType:

    if spectrum_in is None:
        return None

    spectrum = spectrum_in.clone()

    assert intensity_from >= 0.0, "'intensity_from' should be larger than or equal to 0."
    assert intensity_to <= 1.0, "'intensity_to' should be smaller than or equal to 1.0."
    assert intensity_from <= intensity_to, "'intensity_from' should be smaller than or equal to 'intensity_to'."

    if spectrum.intensities.size > 0:
        scale_factor = numpy.max(spectrum.intensities)
        intensities = spectrum.intensities / scale_factor

        condition = numpy.logical_and(intensity_from <= intensities, intensities <= intensity_to)

        spectrum.mz = spectrum.mz[condition]
        spectrum.intensities = spectrum.intensities[condition]

    return spectrum
