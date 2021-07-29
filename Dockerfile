FROM ubuntu

RUN apt-get update -y

RUN apt install git -y
RUN git clone https://github.com/AnKi-cmd/testing_jenkins_pytest fog

RUN ln -snf /usr/share/zoneinfo/Europe/Moscow /etc/localtime && echo Europe/Moscow > /etc/timezone
RUN apt install python3 -y && apt install pip -y && apt install openssh-server -y && apt install sshpass -y && apt inst>RUN cd 'fog' && ./install.sh

EXPOSE 22

CMD cd fog
