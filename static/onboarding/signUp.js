function submitUserData (hasChecked) {
    const signUpBtn = $('#signUpBtn');

    if(hasChecked) {
        signUpBtn.setAttribute('type', 'submit');
    } else {
        signUpBtn.prop('disabled', true)
        alert('수강생 번호 중복체크를 해주세요.')
    };

    
};

function dupCheckFunc (hasChecked) {
    const signUpBtn = $('#signUpBtn');
    const studentNo = $('input[name=studentNo]').val()

    function handleResponse(response) {
        if (response?.exists) {
            hasChecked = false;
            signUpBtn.prop('disabled', true)
            alert('이미 존재하는 계정입니다.')
        } else {
            hasChecked = true;
            signUpBtn.prop('disabled', false)
        }
    };

    
    if (studentNo) {
        $.ajax({
            type: "GET",
            url: `/api/students/exist/${studentNo}`,
            data:{},
            success: function(response) {
                handleResponse(response);
            },
        });
    } else {
        alert('먼저 수강생 번호를 입력해주세요.')
    }    
}