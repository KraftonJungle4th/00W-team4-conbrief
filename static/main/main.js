function searchStudenNo () {
    const searchNo = $('input[name=searchNo]').val();
    const formTag = $('#searchForm')

    function resetInput () {
        searchNo.val("")
    };
    
    function validate(searchNo) {
        if(parseInt(searchNo)) {
            if(searchNo.length) {
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

    if(validate(searchNo)) {
        formTag.submit();
        resetInput();
    }

};


