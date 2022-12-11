
function popup_logout(){
    $.ajax(
        $(".popup").css("display", "flex"),
        $(".popup-logout").css("display", "flex"),
        $(".container").css("filter", "blur(5px)"),
    );

}

function popup_exit(){
    $(".popup-logout").css("display", "none");
}

function moderator_icon(){
    help_staff = $(".help-staff");
    help_staff.css("display", "block");
    help_staff.click( function() {
        $(".help-staff").css("display", "none");
    });
}