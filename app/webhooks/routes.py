from flask import Blueprint, request, jsonify
from app.extensions import mongo

webhook_bp = Blueprint('webhook_bp', __name__, url_prefix='/webhook')


@webhook_bp.route('/receiver', methods=["POST"])
def receiver():
    if request.headers.get('Content-Type') == 'application/json':
        payload = request.json
        event_type = request.headers.get('X-GitHub-Event')

        if event_type == 'pull_request':
            pr = payload.get("pull_request", {})
            action = payload.get("action")
            is_merged = pr.get("merged", False)

            data = {
                "request_id": str(pr.get("id")),
                "author": pr.get("user", {}).get("login") or "Unknown",
                "action": "MERGE" if action == "closed" and is_merged else "PULL_REQUEST",
                "from_branch": pr.get("head", {}).get("ref") or None,
                "to_branch": pr.get("base", {}).get("ref") or None,
                "timestamp": pr.get("updated_at") or "N/A"
            }

            mongo.cx["webhook_db"].events.insert_one(data)
            return jsonify({"message": "Pull Request event saved"}), 200

        elif event_type == 'push':
            data = {
                "request_id": payload.get("after"),
                "author": payload.get("pusher", {}).get("name") or "Unknown",
                "action": "PUSH",
                "from_branch": None,
                "to_branch": payload.get("ref", "").split("/")[-1] or None,
                "timestamp": payload.get("head_commit", {}).get("timestamp") or "N/A"
            }

            mongo.cx["webhook_db"].events.insert_one(data)
            return jsonify({"message": "Push event saved"}), 200

        return jsonify({"message": f"Ignored event: {event_type}"}), 200

    return jsonify({"error": "Invalid Content-Type"}), 400


@webhook_bp.route('/events', methods=["GET"])
def get_events():
    events = list(mongo.cx["webhook_db"].events.find({}, {"_id": 0}))
    return jsonify(events)
