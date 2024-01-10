export const MODAL_TEMP = ({
    id, intro, textList, type, roundNum, score, closeGameModal
}) => `
<div id='miniGameModal'>
    <div class='modalOverlay'></div>
    <div class='modalWrapper'>
        <div id='closeBtn' onclick=${closeGameModal()}>
            <i class="fa-regular fa-circle-xmark"></i>
        </div>
        
        <p> [ROUND ${roundNum}/3]</p>

        <h class='introText'>${intro}</h>
        
        ${textList && textList.map(
            text => 
                `<p class='gameRule'>${text}</p>`
        )}

        ${id !== 'intro' && 
            `<input id=${id} type=${type}></input>`
        }

        <button class='compBtn' id=${id}>
            ${id !== 'intro' ? '정답 확인' : '게임 시작'}
        </button>

        <p>
            현재 점수: ${score}
        </p>
    </div>
</div>
`;

