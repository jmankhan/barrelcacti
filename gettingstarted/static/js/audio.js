var option = {
    element: document.getElementById('player'),                       // Optional, player element
    narrow: false,                                                     // Optional, narrow style
    autoplay: false,                                                   // Optional, autoplay song(s), not supported by mobile browsers
    showlrc: 0,                                                        // Optional, show lrc, can be 0, 1, 2, see: ###With lrc
    mutex: true,                                                       // Optional, pause other players when this player playing
    theme: '#b7daff',                                                  // Optional, theme color, default: #b7daff
    loop: true,                                                        // Optional, loop play music, default: true
    preload: 'auto',                                               // Optional, the way to load music, can be 'none' 'metadata' 'auto', default: 'metadata' in Desktop, 'none' in mobile
    music: {                                                           // Required, music info, see: ###With playlist
        title: 'One Day',                                          // Required, music title
        author: 'Barrel Cacti',                             // Required, music author
        url: startUrl,  // Required, music url
        pic: startPic,  // Optional, music picture
    }
};


var ap = new APlayer(option);
ap.init();

$('.track-data').on('click', function() {
    var _title = $(this).attr('title');
    var _url = $(this).attr('url');
    var _pic = $(this).attr('pic');
    var _album = $(this).attr('album');

    var play = [];
    var album = albums.filter(function(e){return e.id == _album;});
    var index = -1;
    var filteredtracks = alltracks.filter(function(e) {return e.album==album[0].id;})
    filteredtracks.some(function(e, i, a) {if(e.title == _title) {index=i; return true;}})
    

    if(index != -1) {
        for(var i=index; i<filteredtracks.length; i++) {
            var ele = $('div[title=\"'+filteredtracks[i].title+'\"]');

            var t = {title:ele.attr('title'), author:"Barrel Cacti", url:ele.attr('url'), pic:ele.attr('pic')};
            play.push(t);
        }
    }

    option.music = play;
    ap = new APlayer(option);
    ap.init()
    ap.play()

})

// $('aplayer-icon-menu')
$('#track-splash').on('click', function() {
    ap.play();
})