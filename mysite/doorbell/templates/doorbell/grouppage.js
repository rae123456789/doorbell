// modal

const search = document.querySelector('#search');
const modalBg = document.querySelector('.modal-background');
const modal = document.querySelector('.modal');

search.addEventListener('click', () =>{
    modal.classList.add('is-active')
})

modalBg.addEventListener('click', () =>{
    modalBg.classList.remove('is-active')
})