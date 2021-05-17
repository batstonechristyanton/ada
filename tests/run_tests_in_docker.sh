docker run -e HOST=host.docker.internal -v `pwd`:/tests  -it --rm nyurik/alpine-python3-requests  /bin/sh -c "pip install -Ur /tests/requirements.txt; python /tests/test_messages.py"
