var tag = document.createElement('script');
    
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
var player;
  
//This function creates an <iframe> (and YouTube player)
//after the API code downloads.
function onYouTubeIframeAPIReady() {
      player = new YT.Player('youtubevideo', {
      videoId: 'PZO_mYyKemI',
      playerVars: {
          autoplay: 1
      },
      events: {
          'onReady': onPlayerReady,
          'onStateChange': onPlayerStateChange
      }
  });
}
//The API will call this function when the video player is ready.
function onPlayerReady(event) {
  player.play();
}
var done = false;
  function onPlayerStateChange(event) {        
}
function playVideo() {
  player.playVideo();
}

function pauseVideo() {
  player.pauseVideo();
}

function stopVideo() {
  player.stopVideo();
}