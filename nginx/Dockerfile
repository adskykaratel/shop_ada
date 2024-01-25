FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/default.conf /etc/nginx/conf.d/

EXPOSE 80
# Добавьте создание директории и файла лога перед выполнением collectstatic
# RUN mkdir -p /home/eldos/shopbooks/ && touch /home/eldos/shopbooks/log.log

# # Выполните collectstatic
# RUN python3 manage.py collectstatic --noinput