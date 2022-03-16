FROM traefik:v2.6.1
RUN mkdir -p /etc/traefik/acme \
  && touch /etc/traefik/acme/acme.json \
  && chmod 600 /etc/traefik/acme/acme.json
COPY ./backend/compose/production/traefik/traefik.yml /etc/traefik
