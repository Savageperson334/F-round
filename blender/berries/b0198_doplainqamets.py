# doplainqamets
#
# Copied verbatim from https://github.com/ETCBC/phono
#   notebook programs/phono.ipynb (its code cells joined in order; line 638 of those)
#   licence (as GitHub reports it): MIT   see ../licenses/
#   catalogue shelf: Languages scripts and morphology
#
# Everything below the line is that repository's code, unmodified. Imports, constants and
# helper functions it needs from the same file are included, also unmodified.
# ----------------------------------------------------------------------------

import re
import collections

consx = "[bgdwzxvjklmns<pyqrfct]"

qamets_qatan1 = re.compile(
    r"(?<={c})(\.?)@(?={c}(?:\.?[/!]?(?:[ &-]|\Z)))".format(c=consx)
)

cons = "[>bgdhwzxvjklmns<pyqrfct]"

qamets_qatan2 = re.compile(r"(?<={c})(\.?)@(?={c}\.)".format(c=cons))

nbgdkpt = "[wzxvjlmns<yqrfc]"

bgdkpt = "[bgdkpt]"

qamets_qatan3 = re.compile(
    r"(?<={c})(\.?)@(?={c}:(?:{nb}|(?:{b}\.)))".format(c=cons, b=bgdkpt, nb=nbgdkpt)
)

prep = "[bkl]"

qamets_qatan4a = re.compile(r"(?<={p})(\.?[!/]?)@(?=-{c}:@)".format(p=prep, c=cons))

qamets_qatan4b = re.compile(r"(?<={c})(\.?[!/]?)@(?={c}:@)".format(c=cons))

stats = collections.Counter()


def qamets_qatan_repl(match):
    return match.group(1) + "^"


def doplainqamets(word, accentless=False, debug=False, count=False):
    dout = []
    result = word
    if accentless:
        result = result.replace("!", "").replace("/", "")
    if count:
        pre = result
    result = qamets_qatan1.sub(qamets_qatan_repl, result)
    if debug:
        dout.append(("qamets_qatan1", result))
    if count and pre != result:
        stats["qamets_qatan1"] += 1

    if count:
        pre = result
    result = qamets_qatan2.sub(qamets_qatan_repl, result)
    if debug:
        dout.append(("qamets_qatan2", result))
    if count and pre != result:
        stats["qamets_qatan2"] += 1

    if count:
        pre = result
    result = qamets_qatan3.sub(qamets_qatan_repl, result)
    if debug:
        dout.append(("qamets_qatan3", result))
    if count and pre != result:

        stats["qamets_qatan3"] += 1

    if count:
        pre = result
    result = qamets_qatan4a.sub(qamets_qatan_repl, result)
    if debug:
        dout.append(("qamets_qatan4a", result))
    if count and pre != result:
        stats["qamets_qatan4a"] += 1

    if count:
        pre = result
    result = qamets_qatan4b.sub(qamets_qatan_repl, result)
    if debug:
        dout.append(("qamets_qatan4b", result))
    if count and pre != result:
        stats["qamets_qatan4b"] += 1

    return (result, dout) if debug else result
