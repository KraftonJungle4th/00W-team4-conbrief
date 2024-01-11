const requiredFields = document.getElementsByClassName("required");
const saveBtn = document.getElementById("saveForm");

saveBtn.addEventListener("submit", function (event) {
    for (const field of requiredFields) {
        inputValue = field.value;
        if (!new RegExp(field.pattern).test(inputValue)) {
            alert("이름, 이메일, 포부, 깃헙아이디는 필수 항목입니다.");
            event.preventDefault();
            return;
        }
    }
});

function closePreviewModal () {
    $("#previewModal").remove();
}

function openPreview() {
    const inputTags = document.getElementsByTagName("input");
    let inputList = [];
    for (const tag of inputTags) {
        if (tag.value) {
            inputList = [...inputList, {
                                        name: $(`label[for='${tag.name}']`).text().trim(),
                                        value: tag.value
                                    }
                        ]
        }
    }
    $("#con-brief-my-page").append(MODAL_TEMP(inputList));
}

const MODAL_TEMP = (inputList) => `
        <div id='previewModal'>
            <div class='modalOverlay'></div>
            <div class='modalWrapper'>
                <div class="modal">
                    <div id='closeBtn' onclick='closePreviewModal()'>
                        <i class="fa-regular fa-circle-xmark"></i>
                    </div>
                    <ul class='flexVertical'>
                        ${inputList.map(
                            item =>
                                `<li class='infoLine'>
                                      <div class='flexHorizontal lineElement'>
                                          <div class='labelText'>
                                              ${item.name}
                                          </div>
                                          <div class='valueText'>
                                              ${item.value}
                                          </div>
                                      </div>     
                                   </li>
                                  `
                            )                                
                        }
                    </ul>
                </div>
            </div>
        </div>
      `.replace(/,/g, '');
