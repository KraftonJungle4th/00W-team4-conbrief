SIGN_UP = [
    {
        "name": 'studentNo',
        "label": '수강생 번호',
        "example": '(ex.4기-06인 경우 "0406")',
        "type": 'text',
        "pattern": '[0-9]*',
        "placeholder": '형식을 확인해주세요',
    },
    {
        "name": 'password',
        "label": '비밀번호',
        "type": 'password',
        "pattern": '.{4,}',
        "placeholder": '4자리 이상 작성해주세요',
    },
    {
        "name": 'passwordCheck',
        "label": '비밀번호 확인',
        "type": 'password',
        "pattern": '.{4,}',
        "placeholder": '4자리 이상 작성해주세요',
    },
]
