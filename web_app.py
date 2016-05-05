from flask import Flask, request
import checkers

app = Flask(__name__, static_url_path='/static')


#### Backend
@app.route('/gdal_checker')
def gdal_checker():
    path = request.args.get('path')
    checker = checkers.GDALChecker(path)
    return checker.check()

@app.route('/hdf5_checker')
def hdf5_checker():
    path = request.args.get('path')
    checker = checkers.HDF5Checker(path)
    return checker.check()


#### Frontend
@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':

    app.run(port=5000)
    #app.run(host="0.0.0.0", port=5000)