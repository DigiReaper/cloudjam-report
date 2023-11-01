document.addEventListener('DOMContentLoaded', function () {
    var video = document.querySelector('a-video');
    var marker = document.querySelector('a-marker');
    var vid = document.getElementById("greenscreenvideo");


    // Pause video when barcode is not on the screen
    marker.addEventListener('markerLost', function () {
        // video.pause();
        video.pause();

    });

    // Play video when barcode is on the screen
    marker.addEventListener('markerFound', function () {
        video.play();
    });
});