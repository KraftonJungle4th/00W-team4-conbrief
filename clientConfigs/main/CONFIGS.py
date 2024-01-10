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

MODYFIABLE_INFO_CONFIG = [
    {
        "name": 'name',
        "label": '이름',
        "type": 'text',
        "pattern": '[가-힇]{1,}',
        "placeholder": '한글명을 입력해주세요',
        "class": "required",
    },
    {
        "name": 'email',
        "label": '이메일(슬랙 이메일)',
        "type": 'email',
        "placeholder": '이메일 형식을 확인해주세요',
        "pattern": '.+',
        "class": "required"
    },
    {
        "name": 'dream',
        "label": '포부',
        "type": 'text',
        "placeholder": '자신의 포부를 드러내세요',
        "pattern": '.+',
        "class": "required"
    },
    {
        "name": 'github',
        "label": '깃헙아이디',
        "type": 'text',
        "pattern": '[a-zA-Z]{1,}',
        "placeholder": '깃헙 아이디를 확인해주세요',
        "class": "required"
    },
    {
        "name": 'phone',
        "label": '전화번호',
        "type": 'phone',
        "placeholder": '(-)를 제외한 번호',
    },
    {
        "name": 'major',
        "label": '전공',
        "type": 'text',
        "placeholder": '자신의 전공을 알려보세요!',
    },
    {
        "name": 'preferredMenus',
        "label": '선호하는 음식',
        "type": 'text',
        "placeholder": '선호하는 음식을 알려주세요!',
    },
    {
        "name": 'hatedMenus',
        "label": '불호하는 음식',
        "type": 'text',
        "placeholder": '먹기꺼려하는 음식을 적어주세요!',
    },
    {
        "name": 'hometown',
        "label": '본가',
        "type": 'text',
        "placeholder": '어디에서 오셨나요? 시군구 정도만 알려주세요~',
    },
    {
        "name": 'interests',
        "label": '관심분야',
        "type": 'text',
        "placeholder": '최근 관심사를 알려주세요!',
    },
    {
        "name": 'age',
        "label": '나이',
        "type": 'number',
        "placeholder": '나이가 어떻게 되나요?',
    },
    {
        "name": 'mbti',
        "label": 'mbti',
        "type": 'text',
        "placeholder": 'mbti는요?',
    },
    {
        "name": 'ttfTruth1',
        "label": '진실1',
        "type": 'text',
        "placeholder": '자신에 대한 진실을 알려주세요',
    },
    {
        "name": 'ttfTruth2',
        "label": '진실2',
        "type": 'text',
        "placeholder": '자신에 대한 진실을 알려주세요',
    },
    {
        "name": 'ttfFalse',
        "label": '진짜같은 가짜',
        "type": 'text',
        "placeholder": '자신에 대한 진짜같은 가짜를 알려주세요',
    },
]