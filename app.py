

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from graphviz import Graphviz
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/api', methods=['POST'])
def create_person():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'message': 'Name is required'}), 400

    person = Person(name=name)
    db.session.add(person)
    db.session.commit()
    return jsonify({'message': 'Person created successfully'}), 201

@app.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    with app.app_context():
        person = Person.query.get(person_id)

        if not person:
            return jsonify({'message': 'Person not found'}), 404

        return jsonify({'id': person.id, 'name': person.name})


@app.route('/api/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    person = Person.query.get(person_id)

    if not person:
        return jsonify({'message': 'Person not found'}), 404

    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'message': 'Name is required'}), 400

    person.name = name
    db.session.commit()
    return jsonify({'message': 'Person updated successfully'})

@app.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get(person_id)

    if not person:
        return jsonify({'message': 'Person not found'}), 404

    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully'})

if __name__ == '__main__':
    with app.app_context():  # Create an application context before creating tables
        db.create_all()
    app.run(debug=True)