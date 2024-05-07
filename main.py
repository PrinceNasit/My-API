import json
import functions_framework
from flask_cors import cross_origin
import actions


@cross_origin(allow_methods=["POST"])
@functions_framework.http
def get_query_response(request):
    try:
        data = request.get_json()
        user_query = data["query"]
        qr=user_query.split(",")
        e=qr[0].split(" ")
        s=" ".join(e[1:])
        qr.append(s)
        r=[e[0],qr[1:]]
        print(r)
        columns,data,error=actions.query(r)
        if error=="": 
            return json.dumps({"columns":columns,"data":data,"error":"NaN"}),200
        else:
            return json.dumps({"columns":"NaN","data":"NaN","error":error}),200
    except Exception as e:
        return {"error": str(e)},500