var listContent = document.querySelectorAll(".list-content")
var deleteIcons = document.querySelectorAll(".delete")
var checkIcons = document.querySelectorAll(".check")

for (let i = 0; i < listContent.length; i++){
    var listContentChildren = listContent[i].children;
    var statusChild = listContentChildren[1];
    if(statusChild.classList.contains("status-uncompleted")){
        checkIcons[i].innerHTML = "<i class='fa fa-circle-thin fa-lg click' style='color: #fff' aria-hidden='true'></i>";
        listContent[i].style.backgroundColor = "#5b8dee";
        listContent[i].addEventListener('mouseenter', mouseEnterUncompleted)
        listContent[i].addEventListener('mouseleave', mouseLeave)
    } else{
        checkIcons[i].innerHTML = "<i class='fa fa-check-circle fa-lg click' style='color:#fff' aria-hidden='true'></i>";
        listContent[i].style.backgroundColor = "#57eba3";
        listContent[i].addEventListener('mouseenter', mouseEnterCompleted)
        listContent[i].addEventListener('mouseleave', mouseLeave)
    }
}

function mouseEnterCompleted(){
    this.style.boxShadow ="7px 7px 1px #05c270";
}
function mouseEnterUncompleted(){
    this.style.boxShadow ="7px 7px 1px #0063f8";
}

function mouseLeave(){
    this.style.boxShadow = "none";
}


