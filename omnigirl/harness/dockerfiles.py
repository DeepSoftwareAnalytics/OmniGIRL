from functools import partial

# IF you change the base image, you need to rebuild all images (run with --force_rebuild)
_DOCKERFILE_BASE = r"""
FROM --platform={platform} ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN apt update && apt install -y \
wget \
git \
build-essential \
libffi-dev \
libtiff-dev \
python3 \
python3-pip \
python-is-python3 \
jq \
curl \
locales \
locales-all \
tzdata \
&& rm -rf /var/lib/apt/lists/*

# Download and install conda
RUN wget 'https://repo.anaconda.com/miniconda/Miniconda3-py311_23.11.0-2-Linux-{conda_arch}.sh' -O miniconda.sh \
    && bash miniconda.sh -b -p /opt/miniconda3
# Add conda to PATH
ENV PATH=/opt/miniconda3/bin:$PATH
# Add conda to shell startup scripts like .bashrc (DO NOT REMOVE THIS)
RUN conda init --all
RUN conda config --append channels conda-forge

RUN adduser --disabled-password --gecos 'dog' nonroot
"""


_DOCKERFILE_BASE_JAVA = r"""
FROM --platform={platform} ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# 更新包列表并安装必要的软件包
RUN apt update && apt install -y \
    wget \
    git \
    build-essential \
    curl \
    unzip \
    zip \
    ca-certificates \
    locales \
    locales-all \
    tzdata \
    && rm -rf /var/lib/apt/lists/*


RUN adduser --disabled-password --gecos 'dogs' nonroot

"""


_DOCKERFILE_BASE_JS = r"""
FROM --platform={platform} ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# 更新包列表并安装必要的软件包
RUN apt update && apt install -y \
wget \
git \
build-essential \
libffi-dev \
libtiff-dev \
python3 \
python3-pip \
python-is-python3 \
jq \
curl \
locales \
locales-all \
tzdata \
&& rm -rf /var/lib/apt/lists/*

RUN curl https://get.volta.sh | bash

ENV VOLTA_HOME=/root/.volta
ENV PATH=$VOLTA_HOME/bin:$PATH

RUN adduser --disabled-password --gecos 'dog' nonroot
"""

_DOCKERFILE_BASE_JS_20 = r"""
FROM --platform={platform} ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# 更新包列表并安装必要的软件包
RUN apt update && apt install -y \
wget \
git \
build-essential \
libffi-dev \
libtiff-dev \
python3 \
python3-pip \
python-is-python3 \
jq \
curl \
locales \
locales-all \
tzdata \
&& rm -rf /var/lib/apt/lists/*

RUN curl https://get.volta.sh | bash

ENV VOLTA_HOME=/root/.volta
ENV PATH=$VOLTA_HOME/bin:$PATH

RUN adduser --disabled-password --gecos 'dog' nonroot
"""

_DOCKERFILE_BASE_16 = r"""
FROM --platform=linux/x86_64 ubuntu:{ubuntu_version}.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN apt update && apt install -y \
wget \
git \
build-essential \
libffi-dev \
libtiff-dev \
python3 \
python3-pip \
jq \
curl \
locales \
locales-all \
tzdata \
&& rm -rf /var/lib/apt/lists/*

# Download and install conda
RUN wget 'https://repo.anaconda.com/miniconda/Miniconda3-py311_23.11.0-2-Linux-x86_64.sh' -O miniconda.sh \
    && bash miniconda.sh -b -p /opt/miniconda3
# Add conda to PATH
ENV PATH=/opt/miniconda3/bin:$PATH
# Add conda to shell startup scripts like .bashrc (DO NOT REMOVE THIS)
RUN conda init --all
RUN conda config --append channels conda-forge

RUN adduser --disabled-password --gecos 'dog' nonroot
"""


_DOCKERFILE_BASE_ = r"""
FROM --platform=linux/x86_64 ubuntu:{ubuntu_version}.04

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

RUN apt update && apt install -y \
wget \
git \
build-essential \
libffi-dev \
libtiff-dev \
python3 \
python3-pip \
python-is-python3 \
jq \
curl \
locales \
locales-all \
tzdata \
&& rm -rf /var/lib/apt/lists/*

# Download and install conda
RUN wget 'https://repo.anaconda.com/miniconda/Miniconda3-py311_23.11.0-2-Linux-x86_64.sh' -O miniconda.sh \
    && bash miniconda.sh -b -p /opt/miniconda3
# Add conda to PATH
ENV PATH=/opt/miniconda3/bin:$PATH
# Add conda to shell startup scripts like .bashrc (DO NOT REMOVE THIS)
RUN conda init --all
RUN conda config --append channels conda-forge

RUN adduser --disabled-password --gecos 'dog' nonroot
"""

_DOCKERFILE_ENV = r"""FROM --platform={platform} sweb.base.{arch}:latest

COPY ./setup_env.sh /root/
RUN chmod +x /root/setup_env.sh
RUN /bin/bash -c "source ~/.bashrc && /root/setup_env.sh"

WORKDIR /testbed/

# Automatically activate the testbed environment
RUN echo "source /opt/miniconda3/etc/profile.d/conda.sh && conda activate testbed" > /root/.bashrc
"""

_DOCKERFILE_ENV_JS = r"""FROM --platform={platform} sweb.base.{arch}:latest

COPY ./setup_env.sh /root/
RUN chmod +x /root/setup_env.sh
RUN /bin/bash -c "source ~/.bashrc && /root/setup_env.sh"

WORKDIR /testbed/

# Automatically activate the testbed environment

"""

_DOCKERFILE_ENV_JAVA = r"""FROM --platform={platform} sweb.base.{arch}:latest

COPY ./setup_env.sh /root/


# 赋予脚本执行权限
RUN chmod +x /root/setup_env.sh

# 手动加载 SDKMAN 并运行 setup_env.sh
RUN /bin/bash /root/setup_env.sh

WORKDIR /testbed/

"""
# -c "source ~/.bashrc
_DOCKERFILE_INSTANCE = r"""FROM --platform={platform} {env_image_name}

COPY ./setup_repo.sh /root/
RUN /bin/bash /root/setup_repo.sh

WORKDIR /testbed/
"""

_DOCKERFILE_INSTANCE_JAVA = r"""FROM --platform={platform} {env_image_name}

COPY ./setup_repo.sh /root/
ENV JAVA_HOME="/root/.sdkman/candidates/java/current"
ENV PATH="$JAVA_HOME/bin:/root/.sdkman/candidates/maven/current/bin:${{PATH}}"
ENV PATH="/root/.sdkman/candidates/maven/current/bin:${{PATH}}"
RUN /bin/bash /root/setup_repo.sh

WORKDIR /testbed/
"""

_DOCKERFILE_INSTANCE_JAVA_GRADLE = r"""FROM --platform={platform} {env_image_name}

COPY ./setup_repo.sh /root/
ENV JAVA_HOME="/root/.sdkman/candidates/java/current"
ENV PATH="$JAVA_HOME/bin:/root/.sdkman/candidates/gradle/current/bin:${{PATH}}"
ENV PATH="/root/.sdkman/candidates/gradle/current/bin:${{PATH}}"
RUN /bin/bash /root/setup_repo.sh

WORKDIR /testbed/
"""



def get_dockerfile_base(platform, arch):
    if arch == "arm64":
        conda_arch = "aarch64"
    elif 'js' in arch:
        if 'ubuntu_20' in arch:
            return _DOCKERFILE_BASE_JS_20.format(platform=platform)
        else:
            return _DOCKERFILE_BASE_JS.format(platform=platform)
    elif 'java' in arch:
        # if 'ubuntu_20' in arch:
        #     return _DOCKERFILE_BASE_JS_20.format(platform=platform)
        # else:
        return _DOCKERFILE_BASE_JAVA.format(platform=platform)
    else:
        if 'ubuntu_20' in arch:
            return _DOCKERFILE_BASE_.format(ubuntu_version=20)
        elif 'ubuntu_16' in arch:
            return _DOCKERFILE_BASE_16.format(ubuntu_version=16)
        conda_arch = arch
    return _DOCKERFILE_BASE.format(platform=platform, conda_arch=conda_arch)


def get_dockerfile_env(platform, arch):
    if 'js' in arch:
        return _DOCKERFILE_ENV_JS.format(platform=platform, arch=arch)
    elif 'java' in arch:
        return _DOCKERFILE_ENV_JAVA.format(platform=platform, arch=arch)
    else:
        return _DOCKERFILE_ENV.format(platform=platform, arch=arch)


def get_dockerfile_instance(platform, env_image_name):
    if 'gradle' in env_image_name:
        return _DOCKERFILE_INSTANCE_JAVA_GRADLE.format(platform=platform, env_image_name=env_image_name)
    elif 'java' in env_image_name:
        return _DOCKERFILE_INSTANCE_JAVA.format(platform=platform, env_image_name=env_image_name)
    else:
        return _DOCKERFILE_INSTANCE.format(platform=platform, env_image_name=env_image_name)
