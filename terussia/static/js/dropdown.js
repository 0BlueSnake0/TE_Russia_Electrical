function PressDropdown()
{
    var isActive = $("#dropdown-check").prop('checked');
    if (isActive) {
        $("#dropdown-check").prop('checked', false); 
        $("#open").css("display", "flex");
        $("#mobile-dropdown").css("transform", "translateX(-100%)");
    }
    else {
        $("#dropdown-check").prop('checked', true);
        $("#open").css("display", "none"); 
        $("#mobile-dropdown").css("transform", "translateX(0%)");
    }
}