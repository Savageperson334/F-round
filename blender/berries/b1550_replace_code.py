# replace_code
#
# Copied verbatim from https://github.com/david-rx/BioLingual
#   file animalspeak/process_watkins.py, line 60
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Animal acoustics
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

CODE_TO_COMMON = {"CC3A": "Gray Seal", "BD3A": "Long Beaked (Pacific) Common Dolphin", "BD15A": "Pantropical Spotted Dolphin", "CC14A": "Ross Seal", "BD4A": "Grampus- Risso's Dolphin", "BD6B": "White-beaked Dolphin", "BF6A": "Finless Porpoise", "CC5A": "Weddell Seal", "BE3D": "Short- Finned( Pacific) Pilot Whale", "CA1F": "New Zealand Fur Seal", "CC12L": "Spotted Seal", "AA3B": "Southern Right Whale", "CC4A": "Leopard Seal", "BD10A": "Melon Headed Whale", "BE9A": "False Killer Whale", "AC1A": "Minke Whale", "BD1A": "Commerson's Dolphin", "CA3B": "Steller Sea Lion", "BD15B": "Clymene Dolphin", "BD15L": "Spinner Dolphin", "AB1A": "Gray Whale", "CC12H": "Ringed Seal", "AA1A": "Bowhead Whale", "BB1A": "Beluga- White Whale", "BD17A": "Rough- Toothed Dolphin", "BD12B": "Tucuxi Dolphin", "BE3C": "Long- Finned Pilot Whale", "BD6H": "Dusky Dolphin", "BD3B": "Common Dolphin", "BB2A": "Narwhal", "AC2A": "Humpback Whale", "BE7A": "Killer Whale", "X": "Killer Whale", "CD1A": "Sea Otter", "BD15C": "Striped Dolphin", "BD6A": "White-sided Dolphin", "CC12F": "Ribbon Seal", "AA3A": "Northern Right Whale", "BA2A": "Sperm Whale", "BG2A": "Boutu- Amazon River Dolphin", "CC1A": "Hooded Seal", "BF4A": "Dall's Porpoise", "CB1A": "Walrus", "DB1B": "West Indian Manatee", "BD1C": "Heaviside's Dolphin", "BD15F": "Atlantic Spotted Dolphin", "BF2A": "Harbor Porpoise", "BD19D": "Bottlenose Dolphin", "CC12G": "Harp Seal", "BD5A": "Fraser's Dolphin", "CC2A": "Bearded Seal"}


def replace_code(text):
    for code, common in CODE_TO_COMMON.items():
        text = text.replace(code, common)
    return text.strip()
