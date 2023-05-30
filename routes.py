from app import app, db, cache
from flask import jsonify

@app.route('/match/<int:user_id>')
@cache.cached(timeout=3600)  # Cache the response for 1 hour
def get_potential_matches(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'})

    users = User.query.filter(User.id != user_id).all()
    matches = []

    for u in users:
        common_hobbies = set(user.hobbies) & set(u.hobbies)
        compatibility_score = len(common_hobbies)
        if compatibility_score > 0:
            matches.append({
                'id': u.id,
                'name': u.name,
                'hobbies': u.hobbies,
                'compatibility_score': compatibility_score
            })

    matches = sorted(matches, key=lambda x: x['compatibility_score'], reverse=True)
    return jsonify(matches[:10])  # Return top 10 potential matches

@app.route('/')
def hello():
    return 'Hello, world!'

if __name__ == '__main__':
    db.create_all()
    app.run()
