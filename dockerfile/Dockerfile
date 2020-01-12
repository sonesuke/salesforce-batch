FROM python:latest

RUN wget https://developer.salesforce.com/media/salesforce-cli/sfdx-linux-amd64.tar.xz && \
    mkdir sfdx && tar xvf sfdx-linux-amd64.tar.xz -C sfdx --strip-components 1 && \
    echo 'export PATH=$PATH:/sfdx/bin' >> /root/.bashrc

COPY requirements.txt /
RUN pip install -r requirements.txt

WORKDIR /host
