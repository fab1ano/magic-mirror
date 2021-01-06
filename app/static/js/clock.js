var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

function setClock() {
  var now = new Date();

  var wday = days[now.getDay()];
  var month = months[now.getMonth()];
  var day = now.getDate();
  var th = "th";
  th = (day==1 || day==21 || day==31) ? "st" : th;
  th = (day==2 || day==22) ? "nd" : th;
  th = (day==3 || day==23) ? "rd" : th;

  var hour = now.getHours();
  var minute = now.getMinutes();
  if (hour < 10) { hour = "0" + hour; }
  if (minute < 10) { minute = "0" + minute; }

  var myDate = document.getElementById("time");
  myDate.innerHTML = hour + ":" + minute;

  var myClock = document.getElementById("date");
  myClock.innerHTML = wday;

  var myClock = document.getElementById("day");
  myClock.innerHTML = month + " " + day + "<sup>" + th + "</sup>" ;

  setTimeout("setClock()", 1000);
}

setClock();
