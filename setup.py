from setuptools import setup
setup(
    name='atrac',
    version='1.0',
    author = "Jiri Moskovcak",
    author_email = "jmoskovc@redhat.com",
    description = ("Simple commandline tool to create, modify or view "
                   "trac milestones and tickets"),
    license = "GPLv2+",
    url = "http://fedorahosted.org/abrt/",
    scripts = ['src/atrac'],
    package_dir = {'': 'src'},
    data_files = [('/etc/atrac', ['src/atrac.conf']),]
)
