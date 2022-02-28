# server.py
from flask import Flask, request
from blood_calculator import check_HDL


app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def status():
    return "Server On"


@app.route("/info", methods=["GET"])
def info():
    out_string = "This is a test server for class.\n"
    out_string += "THis would tell us how to work."
    return out_string

@app.route("/hdl_check", methods =["POST"])
def check_HDL_from_internet():
    """
    input_json = {"name": <patient_name_strings>,
                  "hdl_result": <hdl_int>}
    """
    in_data = request.get_json()
    hdl_value = in_data["hdl_result"]
    answer = check_HDL(hdl_value)
    print("the answer is {}".format(answer))
    return answer




if __name__ == "__main__":
    app.run()
