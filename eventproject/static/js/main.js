// Navigation
const navbarEl = document.querySelector(".navigation");

window.addEventListener("scroll", () => {
  if (window.scrollY > 0) {
    navbarEl.classList.add("sticky");
  } else {
    navbarEl.classList.remove("sticky");
  }
});
// End of Navigation

// Event Time
let timesEl = document.querySelector(".times");

function getTime() {
  const timeToday = new Date();
  let seconds = timeToday.getSeconds();
  let minutes = timeToday.getMinutes();
  let hours = timeToday.getHours();

  timesEl.textContent = `${hours}:${minutes < 10 ? "0" + minutes : minutes}:${
    seconds < 10 ? "0" + seconds : seconds
  }`;
  // s
  // if (minute >= 59) {
  //   hour = hour + 1;

  //   if (minute < 10) {
  //     hoursEl.textContent = `0${hour}`;
  //   } else {
  //     hour.textContent = hour;
  //   }
  // }
}
setInterval(() => {
  getTime();
}, 1000);
// end f Event Time
