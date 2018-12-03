<<<<<<< HEAD
document.getElementById('toggle_click').addEventListener('click', function (e) {
    var curDom = e.target;
    selectBar = curDom.parentNode.parentNode;
    selectBar.classList.toggle('open');
=======
/*
name : pageSet.js
*/
document.getElementById('toggle_click').addEventListener('click', function (e) {
    var curDom = e.target;
    selectBar = curDom.parentNode.parentNode;
    selectBar.classList.toggle('open');
>>>>>>> 2d59e8dc177bc3601e522e51c4a30e26b37e1ac6
});