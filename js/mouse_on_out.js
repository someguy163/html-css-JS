
function showMovie() {
    var show = document.querySelector('.showMovie');
    show.style.display = 'block';
    // console.log("showMovie show" + show);
    var hide = document.querySelector('.expectedMovie');
    hide.style.display = 'none';
    // console.log("showMovie hide" + hide);
}
function expectedMovie() {
    var hide = document.querySelector('.expectedMovie');
    hide.style.display = 'block';
    // console.log("expectedMovie hide" + hide);
    var show = document.querySelector('.showMovie');
    show.style.display = 'none';
    // console.log("expectedMovie show" + show);

}

// 이미지에 마우스 올려놓을시 영화 설명
function movie_info(n) {
    let show = document.querySelectorAll('.movie_info');
    show[n].style.display = 'block';
    // show[n].style.backgroundColor = 'rgb(68, 75, 82)';
    // console.log(show[n]);
    // show.style.backdrop-filter;= blur('10px');
    // show.style.width = '220px';
    // show.style.height = '350px';
}
// 이미지에 마우스 올려놔서 영화 설명이 나오는데 마우스 떼면 설명 닫기
function movie_info_close(n) {
    let show_close = document.querySelectorAll('.movie_info');
    show_close[n].style.display = 'none';
    
}
