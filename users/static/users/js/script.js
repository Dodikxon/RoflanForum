
function popup_logout(){
    $.ajax(
        $(".popup-logout").css("display", "block"),
        $(".container").css("filter", "blur(5px)"),
    );

}

function popup_exit(){
    $(".popup-logout").css("display", "none");
}