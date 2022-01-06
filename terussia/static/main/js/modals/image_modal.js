function OpenModal() {   
    $(modalBackgroundID).css("display", "block");
}

function CloseModal() {   
    $(modalBackgroundID).css("display", "none");
}
$(modalID).on("click", OpenModal);  
$(modalCloseID).on("click", CloseModal); 