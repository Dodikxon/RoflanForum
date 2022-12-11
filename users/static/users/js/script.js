
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