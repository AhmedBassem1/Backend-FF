import app as a


@a.app.route("/give_access", methods=["GET"])
def give_access():
    
    try:
        
        token = a.request.headers.get('Authorization')
        if not token:
            return a.jsonify({"error": "Token missing!"}), 401
        
        else:
        
            with a.conn.cursor() as cur:
                
                decoded = a.jwt.decode(token, a.app.config['SECRET_KEY'], algorithms=['HS256'])
                user_id = decoded['user_id']
                
                query = "SELECT give_access FROM actor.user WHERE user_id = %s;"
                cur.execute(query, (user_id,))
                data = cur.fetchone()
            
            if data and data[0] == 1:
                return a.jsonify({"message": "You have access!", "access": True}), 200
            else:
                return a.jsonify({"message": "You don't have access!", "access": False}), 200

    except Exception as e:
        return a.jsonify({"error": str(e)}), 500

@a.app.route("/global_access", methods=["GET"])
def global_access():
    try:
        
        
        token = a.request.headers.get('Authorization')
        if not token:
            return a.jsonify({"error": "Token missing!"}), 401
        
        else:
            decoded = a.jwt.decode(token, a.app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = decoded['user_id']
        
            with a.conn.cursor() as cur:
                query = "SELECT global_access FROM actor.user WHERE user_id = %s;"
                cur.execute(query, (user_id,))
                data = cur.fetchone()
            
            if data and data[0] == 1:
                return a.jsonify({"message": "You have global access!", "access": True}), 200
            else:
                return a.jsonify({"message": "You don't have global access!", "access": False}), 200

    except Exception as e:
        return a.jsonify({"error": str(e)}), 500
    


@a.app.route("/data_sensor_access", methods=["GET"])
def data_sensor_access():
    
    try:
        
        
        token = a.request.headers.get('Authorization')
        if not token:
            return a.jsonify({"error": "Token missing!"}), 401
        
        else:
            decoded = a.jwt.decode(token, a.app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = decoded['user_id']
        
            with a.conn.cursor() as cur:
                query = "SELECT data_sensor_access FROM actor.user WHERE user_id = %s;"
                cur.execute(query, (user_id,))
                data = cur.fetchone()
            
            if data and data[0] == 1:
                return a.jsonify({"message": "You have data sensor access!", "access": True , "user_id":user_id}), 200
            else:
                return a.jsonify({"message": "You don't have  data sensor access!", "access": False , "user_id":user_id}), 200

    except Exception as e:
        return a.jsonify({"error": str(e)}), 500


@a.app.route("/daily_report", methods=["GET"])
def daily_report():
    try:
        
        token = a.request.headers.get('Authorization')
        if not token:
            return a.jsonify({"error": "Token missing!"}), 401
        
        else:
            decoded = a.jwt.decode(token, a.app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = decoded['user_id']
        
            with a.conn.cursor() as cur:
                query = "SELECT daily_report FROM actor.user WHERE user_id = %s;"
                cur.execute(query, (user_id,))
                data = cur.fetchone()
            
            if data and data[0] == 1:
                return a.jsonify({"message": "You have daily report access!", "access": True}), 200
            else:
                return a.jsonify({"message": "You don't have  daily report access!", "access": False}), 200

    except Exception as e:
        return a.jsonify({"error": str(e)}), 500


@a.app.route("/ai_report", methods=["GET"])
def ai_report():
    try:
        
        token = a.request.headers.get('Authorization')
        if not token:
            return a.jsonify({"error": "Token missing!"}), 401
        
        else:
            decoded = a.jwt.decode(token, a.app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = decoded['user_id']
        
            with a.conn.cursor() as cur:
                query = "SELECT ai_report FROM actor.user WHERE user_id = %s;"
                cur.execute(query, (user_id,))
                data = cur.fetchone()
            
            if data and data[0] == 1:
                return a.jsonify({"message": "You have ai report access!", "access": True}), 200
            else:
                return a.jsonify({"message": "You don't have  ai report access!", "access": False}), 200

    except Exception as e:
        return a.jsonify({"error": str(e)}), 500  