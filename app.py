from flask import Flask, render_template

app=Flask(__name__,template_folder='./Frontend/html_template',static_folder='./Frontend/static')



@app.route('/')
def index():
    return render_template("Index.html")


@app.route('/RectOptions.html')
def template():
    return render_template('RectOptions.html')

@app.route('/ElipseTool.html')
def template1():
    return render_template('ElipseTool.html')

@app.route('/RoundedRectTool.html')
def template2():
    return render_template('RoundedRectTool.html')

@app.route('/PolygonOptions.html')
def template3():
    return render_template('PolygonOptions.html')

@app.route('/LineOptions.html')
def template4():
    return render_template('LineOptions.html')

@app.route('/CurvedLineOptions.html')
def template5():
    return render_template('CurvedLineOptions.html')

@app.route('/BrushOptions.html')
def template6():
    return render_template('BrushOptions.html')

@app.route('/clear',methods=['GET'])
def template7():
    return ''

@app.route('/AirBrushOptions.html')
def template8():
    return render_template('AirBrushOptions.html')

@app.route('/EraserOptions.html')
def template9():
    return render_template('EraserOptions.html')

@app.route('/loadBox')
def load_box():
    return render_template('LoadBox.html')

if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)