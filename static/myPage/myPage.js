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