from setuptools import setup, find_packages

# Copyright (C) 2025 qvipin
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

setup(
    name="qfetch-py",
    version="1.0.0",
    author="Vipin B",
    author_email="vipin@vipin.xyz",
    description="a simple, no-fuss System Information CLI tool written in Python (Designed/Tested for Ubuntu, Debian, and MacOS)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/qvipin/qfetch",  
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "qfetch=qfetch.qfetch:main",  
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Topic :: System :: Monitoring",
    ],
    python_requires=">=3.12",
)
