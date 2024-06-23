// This file is used to add keyboard and swipe support to the navigation links in item pages.

// Keyboard support

document.addEventListener("keydown", function (event) {
  if (event.key === "ArrowLeft") {
    var prevlink = document.getElementById("prevlink");
    if (prevlink) {
      var link = prevlink.querySelector("a");
      if (link) {
        link.click();
      }
    }
  } else if (event.key === "ArrowRight") {
    var nextlink = document.getElementById("nextlink");
    if (nextlink) {
      var link = nextlink.querySelector("a");
      if (link) {
        link.click();
      }
    }
  }
});

// Swipe support

document.addEventListener("touchstart", handleTouchStart, false);
document.addEventListener("touchmove", handleTouchMove, false);

var xDown = null;
var yDown = null;

function handleTouchStart(event) {
  xDown = event.touches[0].clientX;
  yDown = event.touches[0].clientY;
}

function handleTouchMove(event) {
  if (!xDown || !yDown) {
    return;
  }

  var xUp = event.touches[0].clientX;
  var yUp = event.touches[0].clientY;

  var xDiff = xDown - xUp;
  var yDiff = yDown - yUp;

  if (Math.abs(xDiff) > Math.abs(yDiff)) {
    if (xDiff > 0) {
      // Swipe left
      var prevlink = document.getElementById("prevlink");
      if (prevlink) {
        var link = prevlink.querySelector("a");
        if (link) {
          link.click();
        }
      }
    } else {
      // Swipe right
      var nextlink = document.getElementById("nextlink");
      if (nextlink) {
        var link = nextlink.querySelector("a");
        if (link) {
          link.click();
        }
      }
    }
  }

  xDown = null;
  yDown = null;
}
