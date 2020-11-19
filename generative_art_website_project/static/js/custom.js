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




// let span = document.getElementsByClassName("close")[0];
// span.onclick = function() {
//     modal.style.display = "none";
// }

function openUpModal(product_id, image_url, title) {
    let modal = document.getElementById("modal-" + product_id);
    let modalImg = document.getElementById(product_id);
    let captionText = document.getElementById("caption-" + product_id);
    modal.style.display = "block";
    modalImg.src = image_url;
    captionText.innerHTML = title;
}

function closeModal(product_id) {
    // let span = document.getElementById('close-' + product_id);
    let modal = document.getElementById("modal-" + product_id);
    modal.style.display = "none";
}