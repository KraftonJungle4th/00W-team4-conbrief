
const requiredFields = document.getElementsByClassName('required')
const saveBtn = document.getElementById("saveForm")

saveBtn.addEventListener('submit', function (event) {
    for (const field of requiredFields) {
        inputValue = field.value
        if (!new RegExp(field.pattern).test(inputValue)) {
            alert("이름, 이메일, 포부, 깃헙아이디는 필수 항목입니다.");
            event.preventDefault();
            return;
        }
    }
});

// 팝업 열기 버튼에 이벤트 리스너 추가
document.getElementById('previewBtn').addEventListener('click', function() {
    // 팝업과 오버레이를 보이게 설정
    document.getElementById('popup').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
    const previewContent = document.getElementById('previewContent');

    const inputTags = document.getElementsByTagName('input')
    for (const tag of inputTags) {
        if (tag.value) {
            const info = document.createElement('li');
            info.className = 'infoLine';
            const korTagName = $(`label[for='${tag.name}']`).text()
            info.innerHTML = `
                <span class='labelText'>${korTagName}</span>
                <span class='valueText'>${tag.value}</span>
            `;
            previewContent.appendChild(info)
        }
    }
});

// 팝업 닫기 버튼에 이벤트 리스너 추가
document.getElementById('closePopupBtn').addEventListener('click', function() {
    // 팝업과 오버레이를 감추게 설정
    document.getElementById('popup').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
    document.getElementById('previewContent').innerHTML = '';
});