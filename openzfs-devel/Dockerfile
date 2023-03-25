# Debian bookworm (testing) ships Clang-13, Clang-14 and Clang-15
FROM docker.io/debian:bookworm-20230202-slim

# Version of LLVM, can "-13", "-14", "-15" or "" (empty for GCC)
ARG LLVM=-15

# Install the dependencies to configure the Linux kernel (except the compiler and linker)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      bc \
      bison \
      cpio \
      flex \
      kmod \
      git \
      libelf-dev \
      libssl-dev:native \
      make \
      build-essential:native \
      rsync \
      alien \
      autoconf \
      automake \
      dkms \
      fakeroot \
      gawk \
      libaio-dev \
      libattr1-dev \
      libblkid-dev \
      libcurl4-openssl-dev \
      libffi-dev \
      libssl-dev \
      libtool \
      python3 \
      python3-dev \
      python3-packaging \
      python3-cffi \
      python3-setuptools \
      uuid-dev \
      zlib1g-dev \
      clang$LLVM \
      llvm$LLVM \
      lld$LLVM && \
    apt-get clean

#RUN cd linux && \
#     make LLVM=$LLVM defconfig prepare && \
#     grep ^CONFIG_BLOCK=y .config && \
#     make LLVM=$LLVM -j $(nproc --all) bindeb-pkg && \
#     dpkg -i ../*.deb
# 
#WORKDIR /zfs
#
## install ZFS sources here
#
#RUN set -x && \
#    ./autogen.sh && \
#    ./configure -v KERNEL_LLVM=$LLVM \
#    make -j $(nproc --all) deb
