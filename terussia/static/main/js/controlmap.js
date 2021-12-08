function show_contact (contact_to_show) {  
    if (contact_to_show != -1) {
        document.getElementById(contacts[contact_to_show]).style.display = "flex";
        for (var contact_id in contacts) {
            if (contact_id != contact_to_show) {
                document.getElementById(contacts[contact_id]).style.display = "none";
            } 
        }
        window.scrollTo(100,document.body.scrollHeight);
    }
    else {
        for (var contact_id in contacts) {
            document.getElementById(contacts[contact_id]).style.display = "none"; 
        }
    } 
} 