#!/bin/bash

# Download OpenSans fonts
curl https://github.com/googlefonts/opensans/raw/main/fonts/ttf/OpenSans-Regular.ttf > src/fonts/OpenSans-Regular.ttf
curl https://github.com/googlefonts/opensans/raw/main/fonts/ttf/OpenSans-Bold.ttf > src/fonts/OpenSans-Bold.ttf

# Download and extract Pillow wheel
curl https://files.pythonhosted.org/packages/66/9c/2e1877630eb298bbfd23f90deeec0a3f682a4163d5ca9f178937de57346c/pillow-10.2.0-cp311-cp311-manylinux_2_28_x86_64.whl > src/PIL.whl
unzip src/PIL.whl -d src/.
rm src/PIL.whl

