// const img = document.querySelector('img');
// img.style.float = 'right';

document.getElementById('downloadBtn').addEventListener('click', function() {
    const link = document.createElement('a');
    link.href = "../assets/icons/facebook.svg";
    link.download = "myDocument.svg";
    link.click();
});