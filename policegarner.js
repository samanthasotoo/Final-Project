/// 2. This code loads the IFrame Player API code asynchronously.
      var tag = document.createElement('script');

      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
//This function creates an iframe after the API downloads
      // 3. This function creates an <iframe> (and YouTube player)
      //    after the API code downloads.
      var player;
      function onYouTubeIframeAPIReady() {
        player = new YT.Player('player', {// whats the id of the video
          height: '390',
          width: '640',
          videoId: 'v=RyM9Z2HHfog',
          events: {
            'onReady': onPlayerReady,

          }
        });
      }
      // 4. The API will call this function when the video player is ready.
        function onPlayerReady(event) {


        }

        function play(){
          player.playVideo();
        }

        function stop(){
          player.stopVideo();
        }

        function pause(){
            player.pauseVideo();
        }

         // 5. The API calls this function when the player's state changes.
   //    The function indicates that when playing a video (state=1),
   //    the player should play for six seconds and then stop.
