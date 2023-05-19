FROM ghcr.io/domo-iot/domo-nginx-jwt-base-amd64:latest

COPY nginx.conf /etc/nginx

ADD public_key_yggio.pem /public.pem

EXPOSE 8000

STOPSIGNAL SIGTERM

#ADD Cert.pem /
#ADD Key.pem /

CMD ["nginx", "-g", "daemon off;"]
