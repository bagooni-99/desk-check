var files=[
          "./static/null.jpg",
          "./static/유재석.jpg",
          "./static/정준하.jpg",
          "./static/정형돈.jpg",
          "./static/박명수.jpg",
          "./static/하하.jpg",
          "./static/노홍철.jpg",
          "./static/양세형.jpg",
          "./static/황광희.jpg",
          "./static/조세호.jpg",
          "./static/곰.jpg"];

var imgs = new Array();

for(var i=0; i<files.length;i++){
    imgs[i] = new Image();
    imgs[i].src = files[i];
}

function changeImage(){
    var sel = document.getElementById("sel");
    var img = document.getElementById("myImg");
    
    var index=sel.selectedIndex;
    var mySpan = document.getElementById("mySpan");

    mySpan.innerHTML ="연락처 : "+ sel.options[index].value;
    img.src = imgs[index].src;
}