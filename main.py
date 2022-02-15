#!/usr/bin/python3

from bottle import route, run, HTTPError

#####=====----- Variables -----=====#####

#####=====----- Classes -----=====#####

#####=====----- Functions -----=====#####

@route('/')
def server_root():
    with open('web/index.html', 'r', encoding='utf-8') as f_:
        output_ = f_.read()
    return output_

#####=====----- MAIN -----=====#####

if __name__ == '__main__':
    run(host='127.0.0.1', port=8080, debug=True)
    pass

#####=====----- THE END -----=====########################################