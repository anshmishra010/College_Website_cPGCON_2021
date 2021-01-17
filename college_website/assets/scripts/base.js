

function about_developer_onclick(){
    document.getElementById("body").style.overflow = "hidden";
    document.getElementById("wrapper").style.filter ="blur(30px)";
    document.getElementById("footer-wrapper").style.filter ="blur(30px)";
    document.getElementById("developer-popup").style.visibility = "visible";
}

function developer_popup_close_btn(){
    document.getElementById("body").style.overflow = "visible";
    document.getElementById("wrapper").style.filter ="none";
    document.getElementById("footer-wrapper").style.filter ="none";
    document.getElementById("developer-popup").style.visibility = "hidden";
}