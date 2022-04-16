from utils import load_candidates, get_candidates_all, get_candidates_by_id, get_candidates_by_skill
from flask import Flask


app = Flask(__name__)
candidates_list = load_candidates()


@app.route('/')
def main_route():
    return get_candidates_all(candidates_list)


@app.route('/candidates/<int:candidate_id>')
def candidates_route(candidate_id):
    return get_candidates_by_id(candidates_list, candidate_id)


@app.route('/skills/<candidate_skill>')
def skills_route(candidate_skill):
    return get_candidates_by_skill(candidates_list, candidate_skill)


app.run()
