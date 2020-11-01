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

$(".payment").click(function () {
    $(".payment-now").slideToggle("fast");
    var $this = $(this);
    $this.toggleClass("open");

    if ($this.hasClass("open")) {
        $this.css("display", "none");
    } else {
        $this.html("Read more");
    }
});




