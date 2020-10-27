// hamburger button 

const headerBtn = document.querySelector('.header_btn');
let menuOpen = false;
headerBtn.addEventListener('click', () => {
    if (!menuOpen) {
        headerBtn.classList.add('open');
        menuOpen = true;
    } else {
        headerBtn.classList.remove('open');
        menuOpen = false;
    }
});

function toggleSideBar() {
    document.getElementById('fixednav').classList.toggle('active');
}

function toggleSideDown() {
    document.getElementById('products').classList.toggle('active');
}

$(".purchase-button").click(function () {
    $(".purchase-form").slideToggle("fast");
    var $this = $(this);
    $this.toggleClass("open");

    if ($this.hasClass("open")) {
        $this.css("display", "none");
    } else {
        $this.html("Read more");
    }
});



let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    const slides = document.getElementsByClassName("mySlides");
    const dots = document.getElementsByClassName("dot");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length;
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}