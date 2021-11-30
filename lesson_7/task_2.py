# coding=utf-8

# Задание 2
# *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:

import yaml
import os

pattern = {'my_second_project':
    [{'settings': [
        '__init__.py', 'dev.py', 'prod.py'
    ],
    },
        {'mainapp': [
            '__init__.py', 'models.py', 'views.py', {'templates': [{
                'mainapp': ['base.html', 'index.html']}]
            }]},
        {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{
            'authapp': ['base.html', 'index.html']}]
        }
                     ]
         }
    ]
}
# Можно слделать и через json но в задаче сказали использовать yaml

f = open('config.yaml', 'w')
f.write(yaml.dump(pattern))
f.close()

with open("config.yaml") as y_file:
    cliche = yaml.safe_load(y_file)


def create_data(data):
    for folder, data_tmps in data.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for data_tmp in data_tmps:
            if isinstance(data_tmp, dict):
                create_data(data_tmp)
            else:
                if not os.path.exists(data_tmp):
                    if '.' in data_tmp:
                        with open(data_tmp, 'w') as f:
                            f.write('')
    else:
        os.chdir('../')

# Тренеруюсь использовать конструкции и исключения.


if __name__ == '__main__':
    my_path = cliche
    try:
        create_data(my_path)
    except Exception as e:
        print(e)
