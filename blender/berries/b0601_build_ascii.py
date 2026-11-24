# build_ascii
#
# Copied verbatim from https://github.com/NK8007/gofonix
#   file scripts/gen_fixtures.py, line 48
#   licence (as GitHub reports it): Apache-2.0   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

ASCII_SENTENCES = [
    "The engine reads each input string one byte at a time and never assumes a fixed width.",
    "A tokenizer groups letters into words, keeps whitespace intact, and isolates punctuation.",
    "When a word is found in the dictionary, the system emits a neutral phoneme sequence.",
    "Out of vocabulary words may use deterministic fallback rules before becoming unknown.",
    "Each phoneme carries a compact feature mask that records its phonological properties.",
    "The feature stream has exactly one entry per input byte, which keeps alignment simple.",
    "Numbers such as 42, 1024, and 3 are classified as numeric runs rather than words.",
    "Mixed tokens like MP3 and 3rd are treated carefully so the output stays predictable.",
    "Hyphenated forms such as well-known split into a word, a hyphen, and another word.",
    "The batch mode sees the whole text, while the causal mode may use only the prefix.",
    "Reproducibility matters, so every result records the version of the dictionary used.",
    "A checksum over the dictionary file lets two machines confirm they share the same data.",
    "The alignment maps phonemes back onto byte ranges using a uniform distribution rule.",
    "Boundary symbols exist in the inventory but never leak into the projected feature stream.",
    "Determinism is a hard requirement: the same input always yields the same output.",
    "Concurrency is safe because the engine holds no mutable state after construction.",
    "The parser skips comment lines, blank lines, and any record it cannot understand.",
    "Stress markers from the source notation are stripped before the phonemes are mapped.",
    "Variant selection is deterministic, so the canonical pronunciation is selected.",
    "Performance is measured with benchmarks that report allocations but set no thresholds.",
    "Engineers can extend the inventory later without breaking the opaque mask contract.",
    "The cat sat on the mat while the dog watched it from across the quiet room.",
    "Hello there; the well known phrase appears again, and again, across many lines.",
    "Punctuation marks, including commas, periods, and semicolons, anchor the byte spans.",
    "A robust pipeline favors clear contracts over clever shortcuts that resist testing.",
]


def build_ascii(target_bytes: int) -> str:
    out = []
    size = 0
    i = 0
    para = []
    sentences_in_para = 0
    while size < target_bytes:
        s = ASCII_SENTENCES[i % len(ASCII_SENTENCES)]
        para.append(s)
        size += len(s) + 1
        sentences_in_para += 1
        if sentences_in_para >= 4:
            block = " ".join(para) + "\n\n"
            out.append(block)
            para = []
            sentences_in_para = 0
        i += 1
    if para:
        out.append(" ".join(para) + "\n")
    text = "".join(out)
    return text
