from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


def get_requirements(env):
    with open(u'requirements-{}.txt'.format(env)) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


install_requires = get_requirements('base')
print(install_requires)

tests_require = get_requirements('test')

setup(
    name='funzione_omeografica_test',
    version='0.1',
    description="Generatore di Test a risposta aperta sulla Funzione Omeografica.",
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.9', ],
    author='Chiara Pierpaoli',
    author_email='pierpaolichiara@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=tests_require,
    entry_points='''
                 [console_scripts]
                 genera_test=funzione_omeografica_test.main:main
                 ''',
)
