function submitUserData () {
    const signUpBtn = $('#signUpBtn');
    signUpBtn.setAttribute('type', 'submit');
};

function dupCheckFunc () {
    const dupCheckBtn = $('#dupCheckBtn');
    const studentNo = $('input[name=studentNo]').val()

    function handleResponse(response) {
        if (response?.exists) {
            dupCheckBtn.prop('disabled', false)
            alert('이미 존재하는 계정입니다.')
        } else {
            dupCheckBtn.prop('disabled', true)
        }
    };
    
    $.ajax({
        type: "GET",
        url: `/api/students/exist/${studentNo}`,
        data:{},
        success: function(response) {
            handleResponse(response);
        },
    });
}