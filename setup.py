
import sys
setup_kwds = {}
if sys.version_info > (3,):
    from setuptools import setup
    setup_kwds["test_suite"] = "djsupervisor.tests"
    setup_kwds["use_2to3"] = True
else:
    from distutils.core import setup


try:
    next = next
except NameError:
    def next(i):
        return i.next()


info = {}
try:
    src = open("djsupervisor/__init__.py")
    lines = []
    ln = next(src)
    while "__version__" not in ln:
        lines.append(ln)
        ln = next(src)
    while "__version__" in ln:
        lines.append(ln)
        ln = next(src)
    exec("".join(lines),info)
except Exception:
    raise
    pass


NAME = "django-supervisor"
VERSION = info["__version__"]
DESCRIPTION = "easy integration between djangocl and supervisord"
LONG_DESC = info["__doc__"]
AUTHOR = "Ryan Kelly"
AUTHOR_EMAIL = "ryan@rfk.id.au"
URL="http://github.com/rfk/django-supervisor"
LICENSE = "MIT"
KEYWORDS = "django supervisord process"
PACKAGES = ["djsupervisor"]
CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved",
    "License :: OSI Approved :: MIT License",
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
]

setup(
  name=NAME,
  version=VERSION,
  author=AUTHOR,
  author_email=AUTHOR_EMAIL,
  url=URL,
  description=DESCRIPTION,
  long_description=LONG_DESC,
  license=LICENSE,
  keywords=KEYWORDS,
  packages=PACKAGES,
  classifiers=CLASSIFIERS,
  install_requires=[
    "supervisor",
  ],
  **setup_kwds
)
