/* ==========================*/
/* FULLSCREEN TOGGLE FEATURE */
/* ==========================*/
/* Get the documentElement (<html>) to display the page in fullscreen */
var elem = document.documentElement;
var fullscreen = false;

/* View in fullscreen */
function openFullscreen() {
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
        elem.msRequestFullscreen();
    }
}

/* Close fullscreen */
function closeFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.webkitExitFullscreen) { /* Safari */
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { /* IE11 */
        document.msExitFullscreen();
    }
}

function toggle() {
    if (fullscreen) { closeFullscreen() } else { openFullscreen() };
    fullscreen = !fullscreen;
}

/* ========================*/
/* POPUP DESCRIPTION BLOCK */
/* ========================*/
/* Displays central block when mouse is over on of the tile with information related to that tile */
/* Block is hidden when mouse leaves the tile */
const descs = {
    contacts:"<h1>Contacts</h1><p>This app requires the user to be logged in as it carries personal and private data.</p><p>The style is meant for the app to be smartphone-friendly.</p><p>It is based on a tutorial shared by tomitokko on GitHub.</p>",
    calendar:"<h1>Calendar</h1><p>A sober and efficient scheduler.</p><p>Not operational yet. Eventually, will be synchronized with standard calendars from Apple, Google, Microsoft.</p><p>It is entirely based on the Joyous package, which itself requires the Wagtail CMS package. Wagtail is beautiful and I am considering integrating it into my project, however its richness incurs some complexity and may impact negatively the general ease of use by an average user. So to be assessed... </p>",
    birthdays:"<h1>Birthdays</h1><h6>Not active</h6>This is something that I use every day (currently an Excel spreadsheet). It may seem redundant with the calendar but it is not: I experienced lots of issues with my Apple iCal birthdays (they fluctuate !) and I do not trust it. Still, I will indeed connect the my Calendar and my Birthday apps, as well as with my Genealogy app, by the way.<p>I plan to make a full in-house development for this one.</p>",
    newsaggregator:"<h1>News Aggregator</h1><h6>Not active</h6><p>This app will mimic the Google News feature (collecting the latest posts from a list of sources) but without all the nasty tracking going with it. I do not want someone else but me to know that I am interested in daily feeds about weather forecast, cooking, piano, Python and skiing !</p><p>This will possibly be connected to my blog app and will most certainly use the scraping feature I am also working on.</p>",
    photoalbum:"<h1>Photo album</h1><p>This is the number one reason I've created this MOPC project. I want my photos to be 100% under my control. Whenever you want to share a picture on the social networks, it should be sourced from a storage that you can call yours. Otherwise there will always be an intellectual property ambivalence. Ideally the material you share should be 'degraded' (lower resolution, watermarked,...).</p><p>I have used a no-nonsense django package called Photologue.</p>",
    notes:"<h1>Notes</h1><p>A notes taking application, entirely written in-house.</p><p>So far I was addicted to Evernote. They are becoming more and more restrictive with their free users. It is not useable anymore. Alternatively, the Apple Notes is very unreliable. So now I am going for my own.</p><p>Next development step (big) is the synchronization across platforms. Although not essential, it tackles the situation when a device is not connected to the Internet so needing a standalone client app.</p>",
    blog:"<h1>Blog</h1><p>No one escapes the development of a blog when learning Django.</p><p>When posting to social networks platform, the idea is to post a link to your article which would actually be stored in your own blog application. The challenge is not to make the process cumbersome for the reader (such as having to register/sign in into your own blog app).</p>",
    games:"<h1>Games</h1><p>This space will be dedicated to Python interactive games.</p>",
    genealogy:"<h1>Genealogy</h1><p>This is a family tree maker app. It raises complex data modelling questions (multiple partnering situations, for instance), as well as graphical representation challenges (a family tree is a non-linear tree and, yes, that is tricky).</p><p>I have found no satisfatory ready-made solutions, so I'll have to develop my own...</p>",
    biographywriter:"<h1>Biography Writer</h1><p>This app helps develop one's biography. It uses material from other apps such as Photo Album or Genealogy. The idea is to propose a squeleton for a biography. However the help of a professional writer will be required until IA is up to such a crucial legacy job</p>",
    portfolio:"<h1>Portfolio</h1><p>Like all artists and models have a book, coders must have theirs...</p><p>I hope mine conveys how much I enjoy coding.</p>",
    scraping:"<h1>Scraping</h1><p>Scraping (or web crawling) exists since the first web page was ever created. Interestingly, in order to automate the exploitation of information posted on the web, one needs to collect it and strip it out of its publishing layers, to make it back to an original raw data state. A deeply analytical process.</p>",
    blockchain:"<h1>Blockchain</h1><p>I believe that blockchain is an essential technology for the future. It basically secures any transaction one can think of (make an appointment, sign a contract, pay an invoice,...). The infamous BitCoin is a mere application of it. Every one should start to get familiar with this one.</p><p>The app I will post here is a small example found in a tutorial.</p>",
    filesharing:"<h1>File Sharing</h1><p>While it is crucial to store your personal files in a place that you trust, it is equally important to be able to share them when needed. the files' owner must take a particular care in administering who can download what and for how long.</p><p>Many worthy applications exist in this area but they often target a more IT-savvy audience. How do we encourage average users to engage in such administrative tasks (see also 'Export and Backup')?</p>",
    passwords:"<h1>Passwords</h1><p>This app centralizes the passwords an individual uses all across the Internet.</p><p>Let it be clear though that passwords usage will be obsolete soon. Other means of identification should be employed as of now (for instance, receiving a login confirmation code via an SMS (text message on mobile phone).</p>",
    export:"<h1>Export and Backup</h1><p>The drawback in using personal infrastructure and apps is that the owner is entirely responsible for the safe access to and preservation of the data. Hence user-friendly backup app is a fundamental element.</p>",
};
const popup = document.getElementById('cont-popup');

document.getElementById("contacts").onmouseover = function() {mouseOver("contacts")};
document.getElementById("contacts").onmouseout = function() {mouseOut("contacts")};
document.getElementById("calendar").onmouseover = function() {mouseOver("calendar")};
document.getElementById("calendar").onmouseout = function() {mouseOut("calendar")};
document.getElementById("birthdays").onmouseover = function() {mouseOver("birthdays")};
document.getElementById("birthdays").onmouseout = function() {mouseOut("birthdays")};
document.getElementById("newsaggregator").onmouseover = function() {mouseOver("newsaggregator")};
document.getElementById("newsaggregator").onmouseout = function() {mouseOut("newsaggregator")};
document.getElementById("photoalbum").onmouseover = function() {mouseOver("photoalbum")};
document.getElementById("photoalbum").onmouseout = function() {mouseOut("photoalbum")};
document.getElementById("notes").onmouseover = function() {mouseOver("notes")};
document.getElementById("notes").onmouseout = function() {mouseOut("notes")};
document.getElementById("blog").onmouseover = function() {mouseOver("blog")};
document.getElementById("blog").onmouseout = function() {mouseOut("blog")};
document.getElementById("games").onmouseover = function() {mouseOver("games")};
document.getElementById("games").onmouseout = function() {mouseOut("games")};
document.getElementById("genealogy").onmouseover = function() {mouseOver("genealogy")};
document.getElementById("genealogy").onmouseout = function() {mouseOut("genealogy")};
document.getElementById("biographywriter").onmouseover = function() {mouseOver("biographywriter")};
document.getElementById("biographywriter").onmouseout = function() {mouseOut("biographywriter")};
document.getElementById("portfolio").onmouseover = function() {mouseOver("portfolio")};
document.getElementById("portfolio").onmouseout = function() {mouseOut("portfolio")};
document.getElementById("scraping").onmouseover = function() {mouseOver("scraping")};
document.getElementById("scraping").onmouseout = function() {mouseOut("scraping")};
document.getElementById("blockchain").onmouseover = function() {mouseOver("blockchain")};
document.getElementById("blockchain").onmouseout = function() {mouseOut("blockchain")};
document.getElementById("filesharing").onmouseover = function() {mouseOver("filesharing")};
document.getElementById("filesharing").onmouseout = function() {mouseOut("filesharing")};
document.getElementById("passwords").onmouseover = function() {mouseOver("passwords")};
document.getElementById("passwords").onmouseout = function() {mouseOut("passwords")};
document.getElementById("export").onmouseover = function() {mouseOver("export")};
document.getElementById("export").onmouseout = function() {mouseOut("export")};

function mouseOver(app) {
    popup.innerHTML = descs[app];
    popup.style.display = 'block';
}

function mouseOut() {
    popup.innerHTML = "";
    popup.style.display = 'none';
}