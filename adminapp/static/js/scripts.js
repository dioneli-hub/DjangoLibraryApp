clearBtn = document.querySelector('#clear-btn');
nameInput = document.querySelector('#id_first_name');
surInput = document.querySelector('#id_last_name');
numInput = document.querySelector('#id_phone_number');
statusInput = document.querySelector('#id_is_active');

clearBtn.addEventListener("click", function(e){
    e.preventDefault();
    nameInput.defaultValue = " ";
    surInput.defaultValue = " ";
    numInput.defaultValue = " ";
    statusInput.defaultValue = "---------";
})