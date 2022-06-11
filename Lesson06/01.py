with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        ip = (i.split('-')[0])
        request_type = (i.split('"')[1][0:3])
        request_url = (i.split('"')[1][4:24])
        request_tuple = (ip, request_type, request_url)
        print(request_tuple)
