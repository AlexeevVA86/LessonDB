with open('nginx_logs.txt', 'r', encoding='utf-8') as g:
    for z in g.readlines():
        ip = (z.split('-')[0])
        request_type = (z.split('"')[1][0:3])
        request_url = (z.split('"')[1][4:24])
        request_tuple = (ip, request_type, request_url)
        print(request_tuple)
