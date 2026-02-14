def can_eject_electron(wavelength, work_function):
    """Determine if a photon can eject an electron from a material.
    
    Args:
        wavelength (float): wavelength of incident light in nm
        work_function (float): work function of material in eV
    
    Returns:
        bool: True if electron ejection occurs, False otherwise
    """
    
    hc = 1240  # eV·nm
    
    # Calculate photon energy in eV
    photon_energy = hc / wavelength
    
    return photon_energy > work_function


def electron_kinetic_energy(wavelength, work_function):
    """Calculate the kinetic energy of an ejected electron.
    
    Args:
        wavelength (float): wavelength of incident light in nm
        work_function (float): work function of material in eV
    
    Returns:
        kinetic_energy (float): KE of ejected electron in eV, or 0.0 if no ejection
    """
    
    hc = 1240  # eV·nm
    
    # Calculate photon energy
    photon_energy = hc / wavelength
    
    # Check if ejection occurs
    if photon_energy > work_function:
        return photon_energy - work_function
    else:
        return 0.0
