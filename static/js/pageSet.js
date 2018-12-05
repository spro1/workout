/*
name : pageSet.js
*/
document.getElementById('toggle_click').addEventListener('click', function (e) {
    var curDom = e.target;
    selectBar = curDom.parentNode.parentNode;
    selectBar.classList.toggle('open');
});
