# Challenge

![Workflow](https://github.com/jenspfeifle/challenge/actions/workflows/docker-image.yml/badge.svg)

![Docker](https://img.shields.io/docker/v/jenspfeifle/challenge/latest?label=DockerHub)

This is a small example of how I work, and took me 3-4 hours. Code quality is
checked by various tools. Commits and pull requests are tested automatically
using GitHub Actions. The code is published as a Docker container on DockerHub.

## Description

The task is to merge a list of overlapping intervals. For example, `[[25, 30],
[2, 19], [14, 23], [4, 8]]` should become `[[2, 23], [25, 30]]`.

The runtime of the solution depends primarily on length of the input list. The
dominant factor is sorting the intervals into the correct order, which requires
`O(n log n)` in the worst and average case (the Python standard library uses
[Timsort](https://en.wikipedia.org/wiki/Timsort)).

The memory required grows linearly with the size of the input. Generally, I've
optimized for readability over maximum efficiency. However, by sorting the list
in place and using slices to access the intervals, duplicating data is largely
avoided.

## Getting Started

### Prerequisites

In order to run the container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

Run the example, pulling the container from DockerHub:
```shell
docker run jenspfeifle/challenge:latest
```

Run tests in the container:
```shell
# open a shell in the container
docker run -it jenspfeifle/challenge:latest /bin/bash

# Install development dependencies (these are not included by default in the image pushed to DockerHub)
poetry install

# run tests
poetry run pytest -vv
```

### Building locally

Please see the [Makefile](Makefile), which includes the commands to build,
test, and run the container.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
