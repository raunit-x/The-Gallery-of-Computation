// hamburger button 

const headerBtn = document.querySelector('.header_btn');
let menuOpen = false;
headerBtn.addEventListener('click', () => {
    if(!menuOpen){
        headerBtn.classList.add('open');
        menuOpen = true;
    }else{
        headerBtn.classList.remove('open');
        menuOpen = false;
    }
})

function toggleSideBar(){
    document.getElementById('fixednav').classList.toggle('active');
}

function toggleSideDown(){
    document.getElementById('products').classList.toggle('active');
}

