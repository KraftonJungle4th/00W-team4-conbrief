function setUserGameData() {
    localStorage.setItem("miniGameRound", "0");
    localStorage.setItem("userScore", "0");
}

function closeGameModal() {
    // main doc에 modal temp 빼기
    $("#con-brief-main-page").remove("#miniGameModal");
    localStorage.clear();
}

async function getStudentData(param) {
    const studentNo = localStorage.getItem("studentNo");

    const jwtCookie = document.cookie
        .split("; ")
        .find((cookie) => cookie.startsWith("accessToken="));
    const jwt = jwtCookie ? jwtCookie.split("=")[1] : null;

    if (studentNo) {
        const response = await fetch(
            `/api/students/infor/${studentNo}?param=${param}`,
            {
                method: "GET",
                headers: {
                    Authorization: `Bearer ${jwt}`,
                },
            }
        );

        const result = await response.json();

        return result;
    }
}

async function renderGameModal() {
    let round = parseInt(localStorage.getItem("miniGameRound") || false);
    let score = parseInt(localStorage.getItem("userScore") || false);

    if (!round) {
        setUserGameData();
        round = 0;
        score = 0;
    }

    const studentName = await getStudentData("name");

    $("#con-brief-main-page").append(
        MODAL_TEMP({ ...GAME_DATA[round], studentName, round, score })
    );
}

function nextStep() {
    let round = parseInt(localStorage.getItem("miniGameRound"));
    let score = parseInt(localStorage.getItem("userScore"));

    let studentData = getStudentData(GAME_DATA[round].param);

    localStorage.setItem("miniGameRound", round);
}

const checkFuncs = {
    intro: function () {},
};

const MODAL_TEMP = ({
    studentName,
    id,
    intro,
    textList,
    type,
    round,
    score,
}) => `
        <div id='miniGameModal'>
            <div class='modalOverlay'></div>
            <div class='modalWrapper'>
                <div class="modal">
                    <div id='closeBtn' onclick=${closeGameModal}>
                        <i class="fa-regular fa-circle-xmark"></i>
                    </div>
                    
                    ${round !== 0 ? `<p> [ROUND ${round}/3] </p>` : ""}

                    <h class='introText'>${studentName}${intro}</h>
                    
                    ${
                        textList
                            ? textList.map(
                                (text) => `<p class='gameRule'>${text}</p>`
                            )
                            : ""
                    }

                    ${id !== "intro" ? `<input id=${id} type=${type}>` : ""}

                    <button class='compBtn' id=${id} onclick=${nextStep}>
                        ${id !== "intro" ? "정답 확인" : "게임 시작"}
                    </button>

                    <p>
                        현재 점수: ${score}
                    </p>
                </div>
            </div>
        </div>
      `;

const GAME_DATA = [
    {
        id: "intro",
        param: "name",
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
        param: "age",
        type: "number",
        intro: "의 만 나이, 몇 살일까?",
    },
    {
        id: "mbtiGame",
        param: "mbti",
        type: "select",
        intro: "의 MBTI, E일까 I일까?",
    },
    {
        id: "ttfGame",
        param: "ttf", // back에 ttf 요청하면 ttf set 가져오기
        type: "select",
        intro: "의 가짜 정보, 과연 무엇일까?",
    },
];
