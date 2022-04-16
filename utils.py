import json
import os.path


def load_candidates():
    """
    Загружает JSON файл с информацией о кандидатах
    """
    path_to_file = os.path.join('data', 'candidates.json')
    with open(path_to_file, encoding='utf-8') as file:
        return json.load(file)


def get_candidates_all(candidates_list):
    """
    Выбирает из списка всех кандидатов
    """
    response_ = '<pre>\n'
    for record in candidates_list:
        response_ += (f'Имя кандидата: {record["name"]}\n'
                      f'Позиция кандидата: {record["position"]}\n'
                      f'Навыки: {record["skills"]}\n\n')
    response_ += '<pre>'
    return response_


def get_candidates_by_id(candidates_list, candidate_id):
    """
    Выбирает из списка кандидата по ID
    """
    response_ = ''
    for record in candidates_list:
        if record['id'] == candidate_id:
            response_ += (f'<img src={record["picture"]}>\n<pre>\n'
                          f'Имя кандидата: {record["name"]}\n'
                          f'Позиция кандидата: {record["position"]}\n'
                          f'Навыки: {record["skills"]}\n<pre>\n')
            break
    return response_


def get_candidates_by_skill(candidates_list, candidate_skill):
    """
    Выбирает из списка кандидатов по skill
    """
    response_ = '<pre>\n'
    for record in candidates_list:
        skill_list = record['skills'].lower().split(', ')
        if candidate_skill.lower() in skill_list:
            response_ += (f'Имя кандидата: {record["name"]}\n'
                          f'Позиция кандидата: {record["position"]}\n'
                          f'Навыки: {record["skills"]}\n\n')
        response_ += '<pre>'
    return response_
