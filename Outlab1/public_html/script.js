// AUTHOR: ASHWIN ABRAHAM

var music = false;
var tv = false;
var movie = false;
var novel = false;

function MusicSelect()
{
    music = !music;
}

function TVSelect()
{
    tv = !tv;
}

function MovieSelect()
{
    movie = !movie;
}

function NovelSelect()
{
    novel = !novel;
}

function mySubmit()
{
    var alert_str = "You have selected:\n\n";
    var any_selected = music || tv || movie || novel;
    var music_disp = "none";
    var tv_disp = "none";
    var movie_disp = "none";
    var novel_disp = "none";

    if(music)
    {
        alert_str += "Listening to Music\n";
        music_disp = "block";
    }
    if(tv)
    {
        alert_str += "Watching TV Series\n";
        tv_disp = "block";
    }
    if(movie)
    {
        alert_str += "Watching Movies\n";
        movie_disp = "block";
    }
    if(novel)
    {
        alert_str += "Reading Novels\n";
        novel_disp = "block";
    }
    
    if(!any_selected)
    {
        alert("Select at least one hobby before submitting");
    }
    else
    {
        alert(alert_str);
    }

    document.getElementById("Music Description").style.display = music_disp;
    document.getElementById("TV Description").style.display = tv_disp;
    document.getElementById("Movies Description").style.display = movie_disp;
    document.getElementById("Novels Description").style.display = novel_disp;
}

function swagf()
{
    alert("lmao");
}