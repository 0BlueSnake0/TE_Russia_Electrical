function show_contact (to_show) {  
    if (to_show != -1) {
        contact_to_show = document.getElementById(contacts[to_show]);
        contact_to_show.style.display = "flex";
        for (var contact_id in contacts) {
            if (contact_id != to_show) {
                document.getElementById(contacts[contact_id]).style.display = "none";
            } 
        }  
        nav = document.getElementById("site-navigation-750-plus");
        window.scrollTo(
            contact_to_show.offsetLeft,
            contact_to_show.offsetTop - nav.offsetHeight
        );
    }
    else {
        for (var contact_id in contacts) {
            document.getElementById(contacts[contact_id]).style.display = "none"; 
        }
    } 
} 