import requests
import time
from retry import requests_retry_session

# SUCESSO
print('--------------------------------')
print('TESTE DE SUCESSO')
t0 = time.time()
try:
    response = requests_retry_session().get(
        'http://httpbin.org/delay/1'
    )
except Exception as e:
    print('Resquest falhou: ', e.__class__.__name__)
else:
    print('Resquest funcionou:', response.status_code)
finally:
    t1 = time.time()
    print('Tempo: ', t1 - t0, 's')


# ERRO DE CONEXÃO
print('--------------------------------')
print('TESTE DE ERRO DE CONEXÃO')
t0 = time.time()
try:
    response = requests_retry_session(retries=5).get(
        'http://localhost:9999',
    )
except Exception as e:
    print('Resquest falhou: ', e.__class__.__name__)
else:
    print('Resquest funcionou:', response.status_code)
finally:
    t1 = time.time()
    print('Tempo: ', t1 - t0, 's')


# ERRO DE TIMEOUT
print('--------------------------------')
print('TESTE DE TIMEOUT')
t0 = time.time()
try:
    response = requests_retry_session().get(
        'http://httpbin.org/delay/10',
        timeout=5
    )
except Exception as e:
    print('Resquest falhou: ', e.__class__.__name__)
else:
    print('Resquest funcionou:', response.status_code)
finally:
    t1 = time.time()
    print('Tempo: ', t1 - t0, 's')


# ERRO 500
print('--------------------------------')
print('TESTE DE ERRO 500')
t0 = time.time()
try:
    response = requests_retry_session().get(
        'http://httpbin.org/status/500',
    )
except Exception as e:
    print('Resquest falhou: ', e.__class__.__name__)
    print('Resquest falhou: ', e.args)
else:
    print('Resquest funcionou:', response.status_code)
finally:
    t1 = time.time()
    print('Tempo: ', t1 - t0, 's')
