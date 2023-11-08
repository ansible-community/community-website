# Build the community website with Nikola
FROM python:3.11 AS builder

# Add the contents of this repository to the working directory
ADD . /community-website

# Set the working directory
WORKDIR /community-website

# Install Nikola and build the community website
RUN pip install -r requirements.in -c requirements.txt
RUN nikola build --strict

# Host the community website on a caddy web server
FROM registry.fedoraproject.org/fedora:38
EXPOSE 8080
RUN dnf install --setopt=install_weak_deps=False --best -y caddy && dnf clean all
COPY --from=builder /community-website/output/ /var/www/html/
CMD ["/usr/bin/caddy", "file-server", "--listen", ":8080", "--root", "/var/www/html/"]
