export const GAME_DATA = [
    {
        id: "intro",
        param:'name',
        intro: "의 진짜 모습 알아맞히기!",
        textList: [
            "마이 페이지 게임 정보 입력 후 참여 가능",
            "총 3라운드 진행",
            "무제한 참여 가능",
            "랭킹 반영은 딱 한 번",
        ],
    },
    {
        id: "ageGame",
        param:'age',
        type: "number",
        intro: "의 만 나이, 몇 살일까?",
    },
    {
        id: "mbtiGame",
        param:'mbti',
        type: "select",
        intro: "의 MBTI, E일까 I일까?",
    },
    {
        id: "ttfGame",
        param:'ttf', // back에 ttf 요청하면 ttf set 가져오기
        type: "select",
        intro: "의 가짜 정보, 과연 무엇일까?",
    },
];
