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
    document.body.style.overflow = 'unset';
    $("#previewModal").remove();
}

function openPreview() {
    document.body.style.overflow = 'hidden';
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

    const imageUrl = 'https://cataas.com/cat';
    const name = inputList.filter(item => item.name==='이름')[0].value;
    const dream = inputList.filter(item => item.name==='포부')[0].value;

    $("#con-brief-my-page").append(MODAL_TEMP(inputList, imageUrl, name, dream));
}

const MODAL_TEMP = (inputList, imageUrl, name, dream) => `
        <div id='previewModal'>
            <div class='modalOverlay'></div>
            <div class='modalWrapper'>
                <div class="modal">
                    <div id='closeBtn' onclick='closePreviewModal()'>
                        <i class="fa-regular fa-circle-xmark"></i>
                    </div>
                    <div class='flexVertical flexCenter'>
                        <img
                            class="profileImg"
                            src=${imageUrl}
                        />

                        <p class='introText'>
                            ${name}
                        </p>

                        <p class='dreamText'>
                            ${dream}
                        </p>
                    </div>
                    <div class="separatorLine"></div>
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
