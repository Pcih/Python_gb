# Зададние 1
# Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]


with open('nginx_logs.txt') as file:
    data = []
    row_data = []
    for num, row in enumerate(file):
        raw_row = row.split()
        row_data = [raw_row[0], raw_row[5].replace('"', ''), raw_row[6]]
        data.append(tuple(row_data))
        if num == 10:
            print(data)