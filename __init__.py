from anki import version
assert(version.startswith("2.1."))
subversion = int(version[4:])
if subversion >= 20:
    from . import init20
else:
    from . import init17
