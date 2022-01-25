# MIT License

# Copyright (c) 2022 Eros Fabrici eros.fabrici@gmail.com

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

FROM amancevice/pandas

LABEL base.image="amancevice/pandas"
LABEL version="1"
LABEL software="Data handling"
LABEL software.version="1.0"
LABEL description="Utility functions for genomic pipeline"
LABEL license="https://github.com/eferos93/data-handling/blob/main/LICENSE"
LABEL maintainer="Eros Fabrici"
LABEL maintainer.email="eros.fabrici@gmail.com"

COPY data_handling_utils.py .

# RUN mkdir genomic_data

ENTRYPOINT ["python3", "data_handling_utils.py"]
