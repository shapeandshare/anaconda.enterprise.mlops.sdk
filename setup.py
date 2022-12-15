import setuptools

setuptools.setup(
    name="anaconda.enterprise.mlops.sdk",
    version="0.1.2",
    package_dir={"": "src"},
    packages=setuptools.find_namespace_packages(where="src"),
    author="Joshua C. Burt",
    description="Anaconda Enterprise MLOps SDK",
    long_description="Anaconda Enterprise MLOps SDK",
    include_package_data=True,
    zip_safe=False,
)
