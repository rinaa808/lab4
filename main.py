from flask import Flask, render_template, request

app = Flask(__name__)

list_of_operations = []


@app.route('/')
def main():
    list_of_operations.clear()
    return render_template('main.html')


@app.route("/calculate", methods=["POST"])
def calculate():
    number_one = request.form["first_number"]
    number_two = request.form["second_number"]
    operation = request.form["operation"]

    if operation == "add":
        result = float(number_one) + float(number_two)
        list_of_operations.append('{0} + {1} = {2}'.format(number_one, number_two, result))
        return render_template("main.html", result=result, operations=list_of_operations)

    elif operation == "subtract":
        result = float(number_one) - float(number_two)
        list_of_operations.append('{0} - {1} = {2}'.format(number_one, number_two, result))
        return render_template("main.html", result=result, operations=list_of_operations)

    elif operation == "multiply":
        result = float(number_one) * float(number_two)
        list_of_operations.append('{0} * {1} = {2}'.format(number_one, number_two, result))
        return render_template("main.html", result=result, operations=list_of_operations)

    elif operation == "divide":

        try:
            result = float(number_one) / float(number_two)
            list_of_operations.append('{0} / {1} = {2}'.format(number_one, number_two, result))
            return render_template("main.html", result=result, operations=list_of_operations)

        except ZeroDivisionError:
            result = "You tried to divide by zero !"
            list_of_operations.append('{0} / {1} - ! Zero Division Error !'.format(number_one, number_two))
            return render_template("main.html", result=result, operations=list_of_operations)

    else:
        return render_template("main.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("error_404.html", error=error)


@app.errorhandler(500)
def srv_error(error):
    return render_template("error_500.html", error=error)


if __name__ == '__main__':
    app.run(debug=True)
