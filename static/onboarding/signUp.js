function submitUserData () {
    const signUpBtn = $('#signUpBtn');
    const hasChecked = $('#dupCheckBtn').data('hasChecked');

    if(hasChecked) {
    } else {
        signUpBtn.prop('disabled', true);
        alert('수강생 번호 중복체크를 해주세요.');
    };

};

function dupCheckFunc () {
    const signUpBtn = $('#signUpBtn');
    const studentNo = $('input[name=studentNo]').val()

    function resetInput () {
        $('input[name=studentNo]').val("")
    };

    function handleResponse(response) {
        if (response?.exists) {
            $('#dupCheckBtn').data('hasChecked', false);
            signUpBtn.prop('disabled', true)
            alert('이미 존재하는 계정입니다.')
            resetInput();
        } else {
            $('#dupCheckBtn').data('hasChecked', true);
            signUpBtn.prop('disabled', false)
            alert('가입할 수 있는 계정입니다 :)')
        }
    };

    function validate(studentNo) {
        if(parseInt(studentNo)) {
            const len = studentNo.length
            if( len === 4) {
                return true
            } else {
                alert('수강생번호 4자리를 적어주세요.')
                resetInput();
            }
        } else {
            alert('숫자 4자리를 적어주세요')
            resetInput();
        }
    }

    
    if (studentNo) {
        if(validate(studentNo)) {
            $.ajax({
                type: "GET",
                url: `/api/students/exist/${studentNo}`,
                data:{},
                success: function(response) {
                    handleResponse(response);
                },
            });    
        }
    } else {
        alert('먼저 수강생 번호를 입력해주세요.')
    }    
}