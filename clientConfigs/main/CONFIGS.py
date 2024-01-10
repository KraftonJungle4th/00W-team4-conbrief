SEARCH_CONFIG = {

    'introduction': '궁금한 수강생의 번호를 입력해보세요!',
    'name': 'searchNo',
    'type': 'number',
    'pattern': '[0-9]*',
    'placeholder': 'ex. 4기-06의 경우 0406',
    'btnName': '조회',
    'btnId': 'searchNoBtn'

}

GAME_BTN_CONFIG = {

    'btnName': '미니 게임 시작',
    'btnId': 'miniStartBtn'

}

INFO_CONFIG = {
    'defaultImg': 'https://cataas.com/cat',
    'rankList': [
        {'key': 'friendlyRate', 'label': '인지도 랭킹', 'unit': '위'},
        {'key': 'correctRate', 'label': '정답률 랭킹', 'unit': '위'}
    ],
    'infoList': [
        {"key": 'email', "label": '이메일'},
        {"key": 'github', "label": '깃헙'},
        {"key": 'phone', "label": '전화번호'},
        {"key": 'major', "label": '전공'},
        {"key": 'preferredMenus', "label": '선호 음식'},
        {"key": 'hatedMenues', "label": '불호 음식'},
        {"key": 'hometown', "label": '출신지'},
        {"key": 'interests', "label": '관심 분야'},
    ]
}
