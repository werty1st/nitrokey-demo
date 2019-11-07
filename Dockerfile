FROM ubuntu:19.10


RUN apt update
RUN apt install -y build-essential make autoconf automake
RUN apt install -y wget curl git
RUN apt install -y libgpg-error-dev libassuan-dev texinfo


WORKDIR /mnt

RUN wget https://github.com/gpg/gpgme/archive/gpgme-1.13.1.tar.gz
RUN tar xvf gpgme-1.13.1.tar.gz
RUN cd /mnt/gpgme-gpgme-1.13.1 && ./autogen.sh
RUN cd /mnt/gpgme-gpgme-1.13.1 && ./configure
RUN cd /mnt/gpgme-gpgme-1.13.1 && make


#docker run -it --rm -v $(pwd):/mnt2 nitrokey_gpgme bash -c "cp -rvp /mnt/gpgme-gpgme-1.13.1 /mnt2"